"""CDD Multi-Agent Runner.

Coordinates the multi-agent CDD analysis workflow.
"""

import asyncio
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, AsyncIterator, Literal

from claude_agent_sdk import (
    ClaudeSDKClient,
    ClaudeAgentOptions,
    AgentDefinition,
    AssistantMessage,
    TextBlock,
    ToolUseBlock,
    ResultMessage,
)
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

from agents import get_all_agents, AgentRegistry
from config import get_settings, Settings


@dataclass
class CDDState:
    """State container for CDD analysis progress."""

    company_name: str
    market_definition: str | None = None
    competitor_set: list[str] = field(default_factory=list)
    research_complete: bool = False
    analysis_complete: bool = False
    synthesis_complete: bool = False
    output_complete: bool = False
    checkpoints_passed: list[str] = field(default_factory=list)
    findings: dict[str, Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)


class CDDRunner:
    """Runs the Commercial Due Diligence multi-agent system."""

    def __init__(
        self,
        company_name: str,
        settings: Settings | None = None,
        output_dir: Path | None = None,
    ):
        self.company_name = company_name
        self.settings = settings or get_settings()
        self.output_dir = output_dir or self.settings.output_dir / company_name.replace(" ", "_")
        self.console = Console()
        self.state = CDDState(company_name=company_name)

        # Build agent registry
        self.agents: AgentRegistry = get_all_agents(
            orchestrator_model=self.settings.orchestrator_model,
            research_model=self.settings.research_model,
            analysis_model=self.settings.analysis_model,
            synthesis_model=self.settings.synthesis_model,
        )

    def _get_cdd_options(self) -> ClaudeAgentOptions:
        """Build ClaudeAgentOptions with all agents configured."""
        return ClaudeAgentOptions(
            allowed_tools=[
                "Read", "Write", "Edit", "Glob", "Grep",
                "WebSearch", "WebFetch",
                "Task", "TodoWrite", "AskUserQuestion",
            ],
            agents=self.agents.get_all(),
            permission_mode=self.settings.permission_mode,
            cwd=str(self.output_dir),
            model=self.settings.orchestrator_model,
        )

    async def run(self) -> dict[str, Any]:
        """Execute the full CDD analysis workflow."""
        self.console.print(Panel(
            f"[bold blue]Commercial Due Diligence Analysis[/bold blue]\n"
            f"Company: [bold]{self.company_name}[/bold]\n"
            f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            title="CDD Runner",
        ))

        # Ensure output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Build the orchestration prompt
        prompt = self._build_orchestration_prompt()

        options = self._get_cdd_options()

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console,
        ) as progress:
            task = progress.add_task("Running CDD analysis...", total=None)

            async with ClaudeSDKClient(options=options) as client:
                await client.query(prompt)

                async for message in client.receive_messages():
                    self._handle_message(message, progress, task)

                    # Check for result
                    if isinstance(message, ResultMessage):
                        self.state.output_complete = True
                        break

        return self._compile_results()

    def _build_orchestration_prompt(self) -> str:
        """Build the main orchestration prompt."""
        return f"""Conduct a comprehensive Commercial Due Diligence (CDD) analysis for:

**Company: {self.company_name}**

## Workflow Instructions

Execute the CDD workflow in phases:

### Phase 1: Intake & Scoping
1. Use the market-definition-agent to define the relevant market
2. Use the competitor-identification-agent to identify the competitor set
3. **CHECKPOINT**: Present market definition and competitor set for human approval

### Phase 2: Research (Parallel)
Delegate to research agents in parallel:
- web-research-agent: General market and company information
- financial-data-agent: Financial metrics and performance data
- news-press-agent: Recent news and developments
- industry-research-agent: Industry reports and frameworks

### Phase 3: Domain Analysis
Coordinate with domain supervisors:
- market-supervisor: Oversee all market analysis
- customer-supervisor: Oversee all customer analysis
- company-supervisor: Oversee target company analysis
- competitor-supervisor: Oversee competitive analysis

**CHECKPOINT**: Present key findings for human review

### Phase 4: Quality Assurance
Run quality checks:
- fact-checker-agent: Verify accuracy
- consistency-agent: Check for contradictions
- gap-identifier-agent: Identify missing information
- assumption-validator-agent: Surface and test assumptions

### Phase 5: Synthesis
Coordinate synthesis:
- market-synthesizer-agent: Write market section
- customer-synthesizer-agent: Write customer section
- company-synthesizer-agent: Write company section
- competitor-synthesizer-agent: Write competitor section
- cross-section-synthesizer-agent: Connect insights
- executive-summary-agent: Write executive summary
- recommendations-agent: Formulate recommendations

**CHECKPOINT**: Review draft report sections

### Phase 6: Output Generation
Generate deliverables:
- report-writer-agent: Compile final report
- data-visualization-agent: Create charts and exhibits
- slide-content-agent: Structure presentation
- slide-designer-agent: Create HTML slides
- design-qa-agent: Quality check outputs

**FINAL CHECKPOINT**: Review and approve final deliverables

## Quality Standards
- Institutional quality (Bain, McKinsey, L.E.K. standard)
- All findings sourced and verifiable
- Assumptions clearly stated
- Actionable insights with clear implications

## Output Location
Save all outputs to the current working directory.

Begin the analysis now."""

    def _handle_message(
        self,
        message: Any,
        progress: Progress,
        task: Any,
    ) -> None:
        """Handle incoming messages from the agent."""
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    # Log significant text updates
                    text = block.text.strip()
                    if len(text) > 50:
                        progress.update(task, description=f"[cyan]{text[:80]}...[/cyan]")
                elif isinstance(block, ToolUseBlock):
                    tool_name = block.name
                    if tool_name == "Task":
                        agent_type = block.input.get("subagent_type", "unknown")
                        progress.update(task, description=f"[yellow]Running {agent_type}...[/yellow]")
                    else:
                        progress.update(task, description=f"[blue]Using {tool_name}...[/blue]")

        elif isinstance(message, ResultMessage):
            if message.is_error:
                self.state.errors.append(message.result or "Unknown error")
                self.console.print(f"[red]Error: {message.result}[/red]")
            else:
                self.console.print(f"[green]Analysis complete![/green]")
                if message.result:
                    self.state.findings["final_result"] = message.result

    def _compile_results(self) -> dict[str, Any]:
        """Compile final results."""
        return {
            "company": self.company_name,
            "state": {
                "market_definition": self.state.market_definition,
                "competitor_set": self.state.competitor_set,
                "checkpoints_passed": self.state.checkpoints_passed,
            },
            "findings": self.state.findings,
            "errors": self.state.errors,
            "output_dir": str(self.output_dir),
            "completed": self.state.output_complete,
        }


async def run_cdd(company_name: str, output_dir: Path | None = None) -> dict[str, Any]:
    """Convenience function to run CDD analysis."""
    runner = CDDRunner(company_name=company_name, output_dir=output_dir)
    return await runner.run()
