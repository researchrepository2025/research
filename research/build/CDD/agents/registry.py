"""Agent registry for managing all CDD agents."""

from dataclasses import dataclass, field
from typing import Literal
from claude_agent_sdk import AgentDefinition


@dataclass
class AgentRegistry:
    """Registry of all agents organized by layer."""

    orchestration: dict[str, AgentDefinition] = field(default_factory=dict)
    research: dict[str, AgentDefinition] = field(default_factory=dict)
    domain: dict[str, AgentDefinition] = field(default_factory=dict)
    quality: dict[str, AgentDefinition] = field(default_factory=dict)
    synthesis: dict[str, AgentDefinition] = field(default_factory=dict)
    output: dict[str, AgentDefinition] = field(default_factory=dict)

    def get_all(self) -> dict[str, AgentDefinition]:
        """Get all agents as a flat dictionary for SDK consumption."""
        all_agents: dict[str, AgentDefinition] = {}
        all_agents.update(self.orchestration)
        all_agents.update(self.research)
        all_agents.update(self.domain)
        all_agents.update(self.quality)
        all_agents.update(self.synthesis)
        all_agents.update(self.output)
        return all_agents

    def get_by_layer(
        self, layer: Literal["orchestration", "research", "domain", "quality", "synthesis", "output"]
    ) -> dict[str, AgentDefinition]:
        """Get agents for a specific layer."""
        return getattr(self, layer)


def get_all_agents(
    orchestrator_model: Literal["sonnet", "opus", "haiku"] = "opus",
    research_model: Literal["sonnet", "opus", "haiku"] = "sonnet",
    analysis_model: Literal["sonnet", "opus", "haiku"] = "sonnet",
    synthesis_model: Literal["sonnet", "opus", "haiku"] = "opus",
) -> AgentRegistry:
    """Build complete agent registry with all layers."""
    from .orchestration import get_orchestration_agents
    from .research import get_research_agents
    from .domain import get_domain_agents
    from .quality import get_quality_agents
    from .synthesis import get_synthesis_agents
    from .output import get_output_agents

    return AgentRegistry(
        orchestration=get_orchestration_agents(model=orchestrator_model),
        research=get_research_agents(model=research_model),
        domain=get_domain_agents(model=analysis_model),
        quality=get_quality_agents(model=analysis_model),
        synthesis=get_synthesis_agents(model=synthesis_model),
        output=get_output_agents(model=synthesis_model),
    )
