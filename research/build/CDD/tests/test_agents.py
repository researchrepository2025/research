"""Unit tests for agent definitions.

These tests verify agent structure without making any API calls.
"""

import pytest
from claude_agent_sdk import AgentDefinition

from agents import (
    get_all_agents,
    AgentRegistry,
    get_orchestration_agents,
    get_research_agents,
    get_domain_agents,
    get_quality_agents,
    get_synthesis_agents,
    get_output_agents,
)


class TestAgentRegistry:
    """Tests for the agent registry."""

    def test_registry_creation(self):
        """Verify registry can be created."""
        registry = get_all_agents()
        assert isinstance(registry, AgentRegistry)

    def test_total_agent_count(self):
        """Verify we have exactly 46 agents."""
        registry = get_all_agents()
        all_agents = registry.get_all()
        assert len(all_agents) == 46, f"Expected 46 agents, got {len(all_agents)}"

    def test_layer_counts(self):
        """Verify agent counts per layer."""
        registry = get_all_agents()

        expected_counts = {
            "orchestration": 6,
            "research": 4,
            "domain": 19,
            "quality": 4,
            "synthesis": 8,
            "output": 5,
        }

        for layer, expected in expected_counts.items():
            actual = len(registry.get_by_layer(layer))
            assert actual == expected, f"{layer}: expected {expected}, got {actual}"

    def test_get_all_returns_flat_dict(self):
        """Verify get_all() returns a flat dictionary."""
        registry = get_all_agents()
        all_agents = registry.get_all()

        assert isinstance(all_agents, dict)
        for name, defn in all_agents.items():
            assert isinstance(name, str)
            assert isinstance(defn, AgentDefinition)


class TestAgentDefinitions:
    """Tests for individual agent definitions."""

    @pytest.fixture
    def all_agents(self) -> dict[str, AgentDefinition]:
        """Get all agents as a flat dict."""
        return get_all_agents().get_all()

    def test_all_agents_have_description(self, all_agents):
        """Every agent must have a description."""
        for name, defn in all_agents.items():
            assert defn.description, f"Agent '{name}' missing description"
            assert len(defn.description) > 10, f"Agent '{name}' description too short"

    def test_all_agents_have_prompt(self, all_agents):
        """Every agent must have a system prompt."""
        for name, defn in all_agents.items():
            assert defn.prompt, f"Agent '{name}' missing prompt"
            assert len(defn.prompt) > 50, f"Agent '{name}' prompt too short"

    def test_agent_names_are_kebab_case(self, all_agents):
        """Agent names should be kebab-case."""
        for name in all_agents.keys():
            assert "-" in name or name.islower(), f"Agent name '{name}' not kebab-case"
            assert " " not in name, f"Agent name '{name}' contains spaces"
            assert name == name.lower(), f"Agent name '{name}' not lowercase"

    def test_agents_have_valid_tools(self, all_agents):
        """Agent tools should be valid tool names."""
        valid_tools = {
            "Read", "Write", "Edit", "Glob", "Grep",
            "WebSearch", "WebFetch", "Bash",
            "Task", "TodoWrite", "AskUserQuestion",
        }

        for name, defn in all_agents.items():
            if defn.tools:
                for tool in defn.tools:
                    assert tool in valid_tools, f"Agent '{name}' has invalid tool: {tool}"

    def test_agents_have_valid_models(self, all_agents):
        """Agent models should be valid model names."""
        valid_models = {"sonnet", "opus", "haiku", None}

        for name, defn in all_agents.items():
            assert defn.model in valid_models, f"Agent '{name}' has invalid model: {defn.model}"

    def test_orchestration_agents_have_task_tool(self):
        """Orchestration agents that delegate should have Task tool."""
        orchestration = get_orchestration_agents()

        delegating_agents = [
            "main-orchestrator",
            "market-supervisor",
            "customer-supervisor",
            "company-supervisor",
            "competitor-supervisor",
        ]

        for name in delegating_agents:
            defn = orchestration[name]
            assert "Task" in (defn.tools or []), f"{name} should have Task tool"

    def test_research_agents_have_web_tools(self):
        """Research agents should have web search capabilities."""
        research = get_research_agents()

        for name, defn in research.items():
            tools = defn.tools or []
            has_web = "WebSearch" in tools or "WebFetch" in tools
            assert has_web, f"Research agent '{name}' missing web tools"

    def test_quality_agents_are_read_focused(self):
        """Quality agents should primarily be read-focused."""
        quality = get_quality_agents()

        for name, defn in quality.items():
            tools = defn.tools or []
            # Quality agents shouldn't have Edit or Bash (destructive)
            assert "Bash" not in tools, f"Quality agent '{name}' shouldn't have Bash"

    def test_output_agents_have_write_capability(self):
        """Output agents should be able to write files."""
        output = get_output_agents()

        writers = ["report-writer-agent", "slide-designer-agent"]
        for name in writers:
            defn = output[name]
            assert "Write" in (defn.tools or []), f"{name} should have Write tool"


class TestOrchestrationLayer:
    """Tests specific to orchestration layer."""

    def test_main_orchestrator_exists(self):
        """Main orchestrator must exist."""
        orchestration = get_orchestration_agents()
        assert "main-orchestrator" in orchestration

    def test_checkpoint_manager_exists(self):
        """Checkpoint manager must exist."""
        orchestration = get_orchestration_agents()
        assert "checkpoint-manager" in orchestration

    def test_all_supervisors_exist(self):
        """All domain supervisors must exist."""
        orchestration = get_orchestration_agents()

        supervisors = [
            "market-supervisor",
            "customer-supervisor",
            "company-supervisor",
            "competitor-supervisor",
        ]

        for name in supervisors:
            assert name in orchestration, f"Missing supervisor: {name}"

    def test_checkpoint_manager_has_ask_user(self):
        """Checkpoint manager should be able to ask user questions."""
        orchestration = get_orchestration_agents()
        checkpoint = orchestration["checkpoint-manager"]

        assert "AskUserQuestion" in (checkpoint.tools or [])


class TestDomainAgentCoverage:
    """Tests for domain analysis agent coverage."""

    def test_market_agents_coverage(self):
        """Verify all market analysis agents exist."""
        domain = get_domain_agents()

        market_agents = [
            "market-definition-agent",
            "market-sizing-agent",
            "growth-drivers-agent",
            "market-projection-agent",
            "value-chain-agent",
            "segmentation-agent",
        ]

        for name in market_agents:
            assert name in domain, f"Missing market agent: {name}"

    def test_customer_agents_coverage(self):
        """Verify all customer analysis agents exist."""
        domain = get_domain_agents()

        customer_agents = [
            "customer-segmentation-agent",
            "preferences-kpc-agent",
            "customer-economics-agent",
            "customer-trends-agent",
        ]

        for name in customer_agents:
            assert name in domain, f"Missing customer agent: {name}"

    def test_company_agents_coverage(self):
        """Verify all company analysis agents exist."""
        domain = get_domain_agents()

        company_agents = [
            "company-profile-agent",
            "product-portfolio-agent",
            "strategy-differentiation-agent",
            "financial-performance-agent",
            "market-position-agent",
        ]

        for name in company_agents:
            assert name in domain, f"Missing company agent: {name}"

    def test_competitor_agents_coverage(self):
        """Verify all competitor analysis agents exist."""
        domain = get_domain_agents()

        competitor_agents = [
            "competitor-identification-agent",
            "competitor-profiler-agent",
            "competitive-dynamics-agent",
            "competitive-positioning-agent",
        ]

        for name in competitor_agents:
            assert name in domain, f"Missing competitor agent: {name}"


class TestSynthesisAgentCoverage:
    """Tests for synthesis layer coverage."""

    def test_section_synthesizers_exist(self):
        """All section synthesizers must exist."""
        synthesis = get_synthesis_agents()

        synthesizers = [
            "market-synthesizer-agent",
            "customer-synthesizer-agent",
            "company-synthesizer-agent",
            "competitor-synthesizer-agent",
        ]

        for name in synthesizers:
            assert name in synthesis, f"Missing synthesizer: {name}"

    def test_cross_section_exists(self):
        """Cross-section synthesizer must exist."""
        synthesis = get_synthesis_agents()
        assert "cross-section-synthesizer-agent" in synthesis

    def test_executive_summary_exists(self):
        """Executive summary agent must exist."""
        synthesis = get_synthesis_agents()
        assert "executive-summary-agent" in synthesis

    def test_recommendations_exists(self):
        """Recommendations agent must exist."""
        synthesis = get_synthesis_agents()
        assert "recommendations-agent" in synthesis
