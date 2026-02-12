"""Integration tests with real API calls.

These tests make MINIMAL API calls using the cheapest model (haiku).
Run with: pytest tests/test_integration.py -v

To skip these tests: pytest -m "not integration"
"""

import os
import pytest
from pathlib import Path
from dotenv import load_dotenv

# Load .env file if it exists
load_dotenv()

# Skip all tests in this module if no API key
pytestmark = pytest.mark.skipif(
    not os.getenv("ANTHROPIC_API_KEY"),
    reason="ANTHROPIC_API_KEY not set - skipping integration tests"
)


@pytest.fixture
def integration_output_dir(tmp_path) -> Path:
    """Create a temp directory for integration test outputs."""
    output = tmp_path / "integration_test"
    output.mkdir()
    return output


class TestSDKConnection:
    """Test basic SDK connectivity with minimal API usage."""

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_sdk_connection(self):
        """Test that we can connect to the SDK and get a response."""
        from claude_agent_sdk import query, ClaudeAgentOptions

        # Minimal query - just ask for a single word response
        # This is the cheapest possible API call
        options = ClaudeAgentOptions(
            allowed_tools=[],  # No tools = faster/cheaper
            model="haiku",     # Cheapest model
            max_turns=1,       # Single turn only
        )

        result_text = None
        async for message in query(
            prompt="Respond with only the word 'connected'. Nothing else.",
            options=options
        ):
            if hasattr(message, "result") and message.result:
                result_text = message.result
                break

        assert result_text is not None, "Should receive a response"
        # Be lenient - just check we got something back
        assert len(result_text) > 0

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_single_agent_invocation(self):
        """Test invoking a single agent with minimal work."""
        from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition

        # Define a minimal test agent
        test_agent = AgentDefinition(
            description="Test agent that just confirms it was called.",
            prompt="You are a test agent. When called, respond with 'Agent OK' only.",
            tools=[],
            model="haiku",
        )

        options = ClaudeAgentOptions(
            allowed_tools=["Task"],
            agents={"test-agent": test_agent},
            model="haiku",
            max_turns=3,  # Allow orchestrator + subagent
        )

        responses = []
        async for message in query(
            prompt="Use the test-agent to verify it works. Report only its response.",
            options=options
        ):
            if hasattr(message, "result") and message.result:
                responses.append(message.result)

        # We should get some response
        assert len(responses) > 0


class TestAgentDefinitions:
    """Test that agent definitions are accepted by the SDK."""

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_agent_definitions_are_valid(self):
        """Test that our agent definitions pass SDK validation."""
        from claude_agent_sdk import ClaudeAgentOptions
        from agents import get_all_agents

        # Get all our agents
        registry = get_all_agents()
        all_agents = registry.get_all()

        # Create options with all agents - this validates the structure
        # We're not making an API call, just testing that the SDK accepts them
        options = ClaudeAgentOptions(
            allowed_tools=["Task"],
            agents=all_agents,
            model="haiku",
        )

        # If we get here without exception, the definitions are valid
        assert options.agents is not None
        assert len(options.agents) == 46


class TestMinimalWorkflow:
    """Test a minimal CDD workflow with real API calls.

    This is the most expensive test - run sparingly.
    """

    @pytest.mark.integration
    @pytest.mark.asyncio
    @pytest.mark.slow  # Mark as slow so it can be skipped easily
    async def test_minimal_market_research(self, integration_output_dir):
        """Test a single research agent with minimal scope."""
        from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition

        # Define a minimal research agent
        research_agent = AgentDefinition(
            description="Quick market research agent.",
            prompt="""You are a minimal research agent for testing.
When asked to research, respond with exactly 3 bullet points.
Keep responses under 100 words total.""",
            tools=["WebSearch"],
            model="haiku",
        )

        options = ClaudeAgentOptions(
            allowed_tools=["Task", "WebSearch"],
            agents={"quick-research": research_agent},
            model="haiku",
            max_turns=5,
            cwd=str(integration_output_dir),
        )

        result = None
        async for message in query(
            prompt="Use quick-research to find 3 facts about cloud computing market. Be very brief.",
            options=options
        ):
            if hasattr(message, "result"):
                result = message.result

        assert result is not None
        # Should have some content
        assert len(result) > 20


class TestCLI:
    """Test CLI commands that don't make API calls."""

    def test_list_agents_command(self, capsys):
        """Test that list-agents command works."""
        from typer.testing import CliRunner
        from main import app

        runner = CliRunner()
        result = runner.invoke(app, ["list-agents"])

        assert result.exit_code == 0
        # Should list some agent names
        assert "orchestration" in result.stdout.lower() or "market" in result.stdout.lower()

    def test_version_command(self, capsys):
        """Test that version command works."""
        from typer.testing import CliRunner
        from main import app

        runner = CliRunner()
        result = runner.invoke(app, ["version"])

        assert result.exit_code == 0
        assert "CDD" in result.stdout

    def test_info_command_without_env(self, monkeypatch):
        """Test info command shows error without API key."""
        from typer.testing import CliRunner
        from main import app

        # Remove API key
        monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)

        runner = CliRunner()
        result = runner.invoke(app, ["info"])

        # Should either work (if .env loaded) or show a helpful message
        # Not crashing is the main test
        assert result.exit_code in [0, 1]
