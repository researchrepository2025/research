"""Translates Claude Agent SDK messages to AG-UI protocol events.

This module provides the core translation logic for converting
Claude SDK message types (AssistantMessage, ToolUseBlock, ResultMessage)
into AG-UI protocol events that can be streamed to the frontend.
"""

import uuid
from datetime import datetime
from typing import Any, AsyncIterator

from backend.models.events import AGUIEvent
from backend.models.state import (
    AgentProgress,
    AgentStatus,
    CDDAgentState,
    CheckpointData,
    Finding,
    GeneratedFile,
    PhaseStatus,
)


class EventTranslator:
    """Translates Claude SDK messages to AG-UI events.

    Maintains state and tracks active tool calls to properly
    correlate start/end events for agent invocations.
    """

    # Agent to phase mapping (which agents belong to which phase)
    PHASE_AGENTS: dict[int, list[str]] = {
        1: ["market-definition-agent", "competitor-identification-agent"],
        2: [
            "web-research-agent",
            "financial-data-agent",
            "news-press-agent",
            "industry-research-agent",
        ],
        3: [
            "market-supervisor",
            "customer-supervisor",
            "company-supervisor",
            "competitor-supervisor",
            "market-sizing-agent",
            "growth-drivers-agent",
            "market-projection-agent",
            "value-chain-agent",
            "segmentation-agent",
            "customer-segmentation-agent",
            "preferences-kpc-agent",
            "customer-economics-agent",
            "customer-trends-agent",
            "company-profile-agent",
            "product-portfolio-agent",
            "strategy-differentiation-agent",
            "financial-performance-agent",
            "market-position-agent",
            "competitor-profiler-agent",
            "competitive-dynamics-agent",
            "competitive-positioning-agent",
        ],
        4: [
            "fact-checker-agent",
            "consistency-agent",
            "gap-identifier-agent",
            "assumption-validator-agent",
        ],
        5: [
            "market-synthesizer-agent",
            "customer-synthesizer-agent",
            "company-synthesizer-agent",
            "competitor-synthesizer-agent",
            "cross-section-synthesizer-agent",
            "executive-summary-agent",
            "recommendations-agent",
            "so-what-agent",
        ],
        6: [
            "report-writer-agent",
            "data-visualization-agent",
            "slide-content-agent",
            "slide-designer-agent",
            "design-qa-agent",
        ],
    }

    # Agent to layer mapping
    AGENT_LAYERS: dict[str, str] = {
        # Orchestration
        "main-orchestrator": "orchestration",
        "checkpoint-manager": "orchestration",
        "market-supervisor": "orchestration",
        "customer-supervisor": "orchestration",
        "company-supervisor": "orchestration",
        "competitor-supervisor": "orchestration",
        # Research
        "web-research-agent": "research",
        "financial-data-agent": "research",
        "news-press-agent": "research",
        "industry-research-agent": "research",
        # Domain - Market
        "market-definition-agent": "domain",
        "market-sizing-agent": "domain",
        "growth-drivers-agent": "domain",
        "market-projection-agent": "domain",
        "value-chain-agent": "domain",
        "segmentation-agent": "domain",
        # Domain - Customer
        "customer-segmentation-agent": "domain",
        "preferences-kpc-agent": "domain",
        "customer-economics-agent": "domain",
        "customer-trends-agent": "domain",
        # Domain - Company
        "company-profile-agent": "domain",
        "product-portfolio-agent": "domain",
        "strategy-differentiation-agent": "domain",
        "financial-performance-agent": "domain",
        "market-position-agent": "domain",
        # Domain - Competitor
        "competitor-identification-agent": "domain",
        "competitor-profiler-agent": "domain",
        "competitive-dynamics-agent": "domain",
        "competitive-positioning-agent": "domain",
        # Quality
        "fact-checker-agent": "quality",
        "consistency-agent": "quality",
        "gap-identifier-agent": "quality",
        "assumption-validator-agent": "quality",
        # Synthesis
        "market-synthesizer-agent": "synthesis",
        "customer-synthesizer-agent": "synthesis",
        "company-synthesizer-agent": "synthesis",
        "competitor-synthesizer-agent": "synthesis",
        "cross-section-synthesizer-agent": "synthesis",
        "executive-summary-agent": "synthesis",
        "recommendations-agent": "synthesis",
        "so-what-agent": "synthesis",
        # Output
        "report-writer-agent": "output",
        "data-visualization-agent": "output",
        "slide-content-agent": "output",
        "slide-designer-agent": "output",
        "design-qa-agent": "output",
    }

    # Agent to category mapping (for findings)
    AGENT_CATEGORIES: dict[str, str] = {
        "market-definition-agent": "market",
        "market-sizing-agent": "market",
        "growth-drivers-agent": "market",
        "market-projection-agent": "market",
        "value-chain-agent": "market",
        "segmentation-agent": "market",
        "market-synthesizer-agent": "market",
        "customer-segmentation-agent": "customer",
        "preferences-kpc-agent": "customer",
        "customer-economics-agent": "customer",
        "customer-trends-agent": "customer",
        "customer-synthesizer-agent": "customer",
        "company-profile-agent": "company",
        "product-portfolio-agent": "company",
        "strategy-differentiation-agent": "company",
        "financial-performance-agent": "company",
        "market-position-agent": "company",
        "company-synthesizer-agent": "company",
        "competitor-identification-agent": "competitor",
        "competitor-profiler-agent": "competitor",
        "competitive-dynamics-agent": "competitor",
        "competitive-positioning-agent": "competitor",
        "competitor-synthesizer-agent": "competitor",
    }

    def __init__(self, state: CDDAgentState):
        """Initialize translator with state reference.

        Args:
            state: The CDDAgentState to update during translation.
        """
        self.state = state
        self._active_tool_calls: dict[str, str] = {}  # tool_id -> agent_name
        self._current_agent: str | None = None  # Currently executing agent
        self._message_counter: int = 0  # For unique message IDs

    async def translate(self, message: Any) -> AsyncIterator[AGUIEvent]:
        """Translate a Claude SDK message to AG-UI events.

        Args:
            message: Claude SDK message (AssistantMessage, ResultMessage, etc.)

        Yields:
            AGUIEvent instances for each translated event.
        """
        # Import here to avoid circular imports
        try:
            from claude_agent_sdk import AssistantMessage, ResultMessage
            from claude_agent_sdk.types import TextBlock, ToolUseBlock
        except ImportError:
            # Fallback for testing without SDK
            return

        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    # Store streaming message in state for UI display
                    self._message_counter += 1
                    streaming_msg = {
                        "id": str(self._message_counter),
                        "content": block.text,
                        "agent": self._current_agent or "orchestrator",
                        "timestamp": datetime.utcnow().isoformat(),
                    }
                    self.state.streaming_messages.append(streaming_msg)
                    # Keep last 50 messages to prevent memory bloat
                    if len(self.state.streaming_messages) > 50:
                        self.state.streaming_messages = self.state.streaming_messages[-50:]

                    # Emit text content
                    yield AGUIEvent.text_message(content=block.text)
                    yield AGUIEvent.state_delta(
                        path="streaming_messages",
                        value=self.state.streaming_messages,
                    )

                    # Check for checkpoint triggers
                    checkpoint = self._detect_checkpoint(block.text)
                    if checkpoint:
                        self.state.current_checkpoint = checkpoint
                        yield AGUIEvent.checkpoint_pending(
                            checkpoint.model_dump(mode="json")
                        )
                        yield AGUIEvent.state_snapshot(
                            self.state.model_dump(mode="json")
                        )

                elif isinstance(block, ToolUseBlock):
                    tool_id = str(uuid.uuid4())
                    tool_name = block.name

                    # Handle Task tool (agent delegation)
                    if tool_name == "Task":
                        agent_type = block.input.get("subagent_type", "unknown")
                        self._active_tool_calls[tool_id] = agent_type
                        self._current_agent = agent_type  # Track current agent

                        # Update agent status
                        agent_progress = AgentProgress(
                            agent_name=agent_type,
                            layer=self.AGENT_LAYERS.get(agent_type, "unknown"),
                            status=AgentStatus.RUNNING,
                            started_at=datetime.utcnow(),
                        )
                        self.state.active_agents.append(agent_progress)

                        # Update phase progress
                        self._update_phase_progress(agent_type)

                        # Store current tool call in state
                        self.state.current_tool_call = {
                            "tool_id": tool_id,
                            "tool_name": "Task",
                            "agent": agent_type,
                            "started_at": datetime.utcnow().isoformat(),
                        }

                        yield AGUIEvent.tool_call_start(
                            tool_id=tool_id,
                            tool_name="Task",
                            arguments={"agent": agent_type},
                        )
                        yield AGUIEvent.state_delta(
                            path="active_agents",
                            value=[a.model_dump(mode="json") for a in self.state.active_agents],
                        )
                        yield AGUIEvent.state_delta(
                            path="current_tool_call",
                            value=self.state.current_tool_call,
                        )

                    # Handle Write tool (file creation)
                    elif tool_name == "Write":
                        file_path = block.input.get("file_path", "")
                        content = block.input.get("content", "")

                        # Emit file created event
                        async for event in self._handle_file_write(file_path, content):
                            yield event

                        yield AGUIEvent.tool_call_start(
                            tool_id=tool_id,
                            tool_name=tool_name,
                            arguments={"file_path": file_path},
                        )
                    else:
                        yield AGUIEvent.tool_call_start(
                            tool_id=tool_id,
                            tool_name=tool_name,
                            arguments=block.input,
                        )

        elif isinstance(message, ResultMessage):
            if message.is_error:
                self.state.errors.append(message.result or "Unknown error")
                yield AGUIEvent.state_delta(path="errors", value=self.state.errors)
            else:
                # Extract findings from results
                findings = self._extract_findings(message.result)
                if findings:
                    self.state.findings.extend(findings)
                    yield AGUIEvent.state_delta(
                        path="findings",
                        value=[f.model_dump(mode="json") for f in self.state.findings],
                    )

                    # Update coverage metrics
                    self._update_coverage()
                    yield AGUIEvent.state_delta(
                        path="coverage",
                        value=self.state.coverage,
                    )

    async def _handle_file_write(
        self, file_path: str, content: str
    ) -> AsyncIterator[AGUIEvent]:
        """Handle file write operations and emit FILE_CREATED events.

        Args:
            file_path: Path to the file being written.
            content: Content of the file.

        Yields:
            AGUIEvent for file creation.
        """
        import os

        filename = os.path.basename(file_path)
        file_ext = os.path.splitext(filename)[1].lower()

        # Determine file type
        file_type = "text"
        if file_ext in [".md", ".markdown"]:
            file_type = "markdown"
        elif file_ext == ".json":
            file_type = "json"
        elif file_ext in [".py", ".js", ".ts"]:
            file_type = "code"

        # Create preview (first 500 chars)
        preview = content[:500] + ("..." if len(content) > 500 else "")

        # Create GeneratedFile record
        generated_file = GeneratedFile(
            id=str(uuid.uuid4()),
            file_path=file_path,
            filename=filename,
            file_type=file_type,
            size=len(content),
            preview=preview,
            created_at=datetime.utcnow(),
            agent=self._current_agent,
        )
        self.state.generated_files.append(generated_file)

        # Emit file created event
        yield AGUIEvent.file_created(
            file_path=file_path,
            filename=filename,
            size=len(content),
            preview=preview,
            file_type=file_type,
        )

        # Also emit state delta for generated_files
        yield AGUIEvent.state_delta(
            path="generated_files",
            value=[f.model_dump(mode="json") for f in self.state.generated_files],
        )

    def _detect_checkpoint(self, text: str) -> CheckpointData | None:
        """Detect checkpoint triggers in assistant text.

        Args:
            text: Text content from assistant message.

        Returns:
            CheckpointData if a checkpoint is detected, None otherwise.
        """
        text_lower = text.lower()
        checkpoint_triggers = [
            "checkpoint",
            "awaiting approval",
            "human review",
            "please confirm",
            "please approve",
        ]

        if not any(trigger in text_lower for trigger in checkpoint_triggers):
            return None

        # Determine checkpoint type
        if "scope" in text_lower or "market definition" in text_lower:
            return CheckpointData(
                checkpoint_id=str(uuid.uuid4()),
                checkpoint_type="scope",
                title="Scope Approval",
                description="Review and approve market definition and competitor set",
                data={
                    "market_definition": self.state.market_definition,
                    "competitor_set": self.state.competitor_set,
                },
            )
        elif "findings" in text_lower or "research" in text_lower:
            return CheckpointData(
                checkpoint_id=str(uuid.uuid4()),
                checkpoint_type="findings",
                title="Findings Review",
                description="Review key findings before synthesis",
                data={"findings_summary": self._summarize_findings()},
            )
        elif "draft" in text_lower or "synthesis" in text_lower:
            return CheckpointData(
                checkpoint_id=str(uuid.uuid4()),
                checkpoint_type="draft",
                title="Draft Review",
                description="Review synthesized draft before final output",
                data={"sections_ready": list(self.state.report_sections.keys())},
            )
        elif "final" in text_lower or "complete" in text_lower:
            return CheckpointData(
                checkpoint_id=str(uuid.uuid4()),
                checkpoint_type="final",
                title="Final Approval",
                description="Final approval before report generation",
                data={"ready_for_output": True},
            )

        return None

    def _extract_findings(self, result: str | None) -> list[Finding]:
        """Extract structured findings from agent results.

        Args:
            result: Result text from agent.

        Returns:
            List of Finding objects extracted from the result.
        """
        import re

        if not result:
            return []

        # Get current agent metadata
        agent_name = self._current_agent or "unknown"
        layer = self.AGENT_LAYERS.get(agent_name, "unknown")
        category = self.AGENT_CATEGORIES.get(agent_name, "market")

        # Extract URLs from content for sources
        url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'

        # Simple extraction - look for key patterns
        findings = []
        lines = result.split("\n")
        current_finding = None

        for line in lines:
            line = line.strip()
            if line.startswith("**") or line.startswith("##") or line.startswith("###"):
                if current_finding and current_finding.content.strip():
                    findings.append(current_finding)
                current_finding = Finding(
                    id=str(uuid.uuid4()),
                    agent=agent_name,
                    layer=layer,
                    category=category,
                    title=line.strip("*# "),
                    content="",
                    sources=[],
                    timestamp=datetime.utcnow(),
                )
            elif current_finding and line:
                current_finding.content += line + " "
                # Extract URLs as sources
                urls = re.findall(url_pattern, line)
                for url in urls:
                    if url not in current_finding.sources:
                        current_finding.sources.append(url)

        if current_finding and current_finding.content.strip():
            findings.append(current_finding)

        return findings

    def _update_phase_progress(self, agent_name: str):
        """Update phase progress based on active agent.

        Args:
            agent_name: Name of the agent that started.
        """
        for phase_num, agents in self.PHASE_AGENTS.items():
            if agent_name in agents:
                # Find the phase in state
                for phase in self.state.phases:
                    if phase.phase_number == phase_num:
                        if phase.status == PhaseStatus.PENDING:
                            phase.status = PhaseStatus.IN_PROGRESS
                            phase.started_at = datetime.utcnow()
                        self.state.current_phase = phase_num
                        break
                break

    def _update_coverage(self):
        """Update coverage metrics based on findings."""
        categories = ["market", "customer", "company", "competitor"]
        for cat in categories:
            cat_findings = [f for f in self.state.findings if f.category == cat]
            # Heuristic: coverage based on number of findings (max 10)
            self.state.coverage[cat] = min(1.0, len(cat_findings) / 10)

    def _summarize_findings(self) -> dict[str, Any]:
        """Create a summary of findings for checkpoint review.

        Returns:
            Dictionary with findings summary.
        """
        return {
            "total": len(self.state.findings),
            "by_category": {
                cat: len([f for f in self.state.findings if f.category == cat])
                for cat in ["market", "customer", "company", "competitor"]
            },
        }

    def mark_agent_completed(self, agent_name: str):
        """Mark an agent as completed and move to completed list.

        Args:
            agent_name: Name of the agent to mark complete.
        """
        for i, agent in enumerate(self.state.active_agents):
            if agent.agent_name == agent_name:
                agent.status = AgentStatus.COMPLETED
                agent.completed_at = datetime.utcnow()
                self.state.completed_agents.append(agent)
                self.state.active_agents.pop(i)

                # Update phase progress
                for phase in self.state.phases:
                    if phase.phase_number == self.state.current_phase:
                        phase.agents_completed += 1
                        if phase.agents_completed >= phase.agents_total:
                            phase.status = PhaseStatus.COMPLETED
                            phase.completed_at = datetime.utcnow()
                        break
                break
