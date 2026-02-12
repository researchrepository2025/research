"""Unit tests for CDD runner.

These tests verify runner structure without making API calls.
"""

import pytest
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

from cdd_runner import CDDRunner, CDDState, run_cdd
from agents import AgentRegistry


class TestCDDState:
    """Tests for CDD state container."""

    def test_state_initialization(self):
        """State should initialize with company name."""
        state = CDDState(company_name="Test Corp")

        assert state.company_name == "Test Corp"
        assert state.market_definition is None
        assert state.competitor_set == []
        assert state.research_complete is False
        assert state.analysis_complete is False
        assert state.synthesis_complete is False
        assert state.output_complete is False
        assert state.checkpoints_passed == []
        assert state.findings == {}
        assert state.errors == []

    def test_state_is_mutable(self):
        """State should be mutable for tracking progress."""
        state = CDDState(company_name="Test Corp")

        state.market_definition = "B2B SaaS"
        state.competitor_set = ["Competitor A", "Competitor B"]
        state.research_complete = True
        state.checkpoints_passed.append("scope_approved")
        state.findings["market_size"] = "$10B"

        assert state.market_definition == "B2B SaaS"
        assert len(state.competitor_set) == 2
        assert state.research_complete is True
        assert "scope_approved" in state.checkpoints_passed
        assert state.findings["market_size"] == "$10B"


class TestCDDRunnerStructure:
    """Tests for CDDRunner structure (no API calls)."""

    def test_runner_initialization(self, mock_settings):
        """Runner should initialize with company name."""
        runner = CDDRunner(company_name="Test Corp")

        assert runner.company_name == "Test Corp"
        assert runner.settings is not None
        assert runner.console is not None
        assert isinstance(runner.agents, AgentRegistry)
        assert isinstance(runner.state, CDDState)

    def test_runner_output_dir(self, mock_settings, tmp_path):
        """Runner should set output directory correctly."""
        runner = CDDRunner(
            company_name="Test Corp",
            output_dir=tmp_path / "test_output"
        )

        assert runner.output_dir == tmp_path / "test_output"

    def test_runner_default_output_dir(self, mock_settings):
        """Runner should create default output dir from company name."""
        runner = CDDRunner(company_name="Test Corp With Spaces")

        # Should replace spaces with underscores
        assert "Test_Corp_With_Spaces" in str(runner.output_dir)

    def test_runner_has_all_agents(self, mock_settings):
        """Runner should have all 46 agents loaded."""
        runner = CDDRunner(company_name="Test Corp")

        all_agents = runner.agents.get_all()
        assert len(all_agents) == 46

    def test_get_cdd_options_returns_valid_config(self, mock_settings):
        """_get_cdd_options should return valid ClaudeAgentOptions."""
        runner = CDDRunner(company_name="Test Corp")
        options = runner._get_cdd_options()

        # Check required fields
        assert options.allowed_tools is not None
        assert "Task" in options.allowed_tools
        assert options.agents is not None
        assert len(options.agents) == 46
        assert options.permission_mode is not None

    def test_build_orchestration_prompt(self, mock_settings):
        """Orchestration prompt should contain company name."""
        runner = CDDRunner(company_name="Test Corp")
        prompt = runner._build_orchestration_prompt()

        assert "Test Corp" in prompt
        assert "Commercial Due Diligence" in prompt
        assert "Phase 1" in prompt  # Should have workflow phases
        assert "CHECKPOINT" in prompt  # Should mention checkpoints

    def test_compile_results_structure(self, mock_settings):
        """_compile_results should return proper structure."""
        runner = CDDRunner(company_name="Test Corp")

        # Set some state
        runner.state.market_definition = "B2B SaaS"
        runner.state.findings["test"] = "value"

        results = runner._compile_results()

        assert results["company"] == "Test Corp"
        assert "state" in results
        assert "findings" in results
        assert "errors" in results
        assert "output_dir" in results
        assert "completed" in results


class TestCDDRunnerMocked:
    """Tests for CDDRunner with mocked SDK (no API calls)."""

    @pytest.fixture
    def mock_client(self):
        """Create a mock ClaudeSDKClient."""
        client = AsyncMock()
        client.query = AsyncMock()
        client.receive_messages = AsyncMock(return_value=iter([]))
        return client

    @pytest.mark.asyncio
    async def test_runner_creates_output_dir(self, mock_settings, tmp_path):
        """Runner should create output directory."""
        output_dir = tmp_path / "test_output"
        runner = CDDRunner(company_name="Test Corp", output_dir=output_dir)

        # Mock the SDK client
        with patch("cdd_runner.ClaudeSDKClient") as mock_client_class:
            mock_client = AsyncMock()
            mock_client.__aenter__ = AsyncMock(return_value=mock_client)
            mock_client.__aexit__ = AsyncMock(return_value=None)
            mock_client.query = AsyncMock()

            # Return a mock ResultMessage to end the loop
            from claude_agent_sdk import ResultMessage
            mock_result = MagicMock(spec=ResultMessage)
            mock_result.is_error = False
            mock_result.result = "Analysis complete"

            async def mock_receive():
                yield mock_result

            mock_client.receive_messages = mock_receive
            mock_client_class.return_value = mock_client

            await runner.run()

        assert output_dir.exists()

    @pytest.mark.asyncio
    async def test_runner_handles_errors(self, mock_settings, tmp_path):
        """Runner should capture errors in state."""
        runner = CDDRunner(company_name="Test Corp", output_dir=tmp_path / "output")

        with patch("cdd_runner.ClaudeSDKClient") as mock_client_class:
            mock_client = AsyncMock()
            mock_client.__aenter__ = AsyncMock(return_value=mock_client)
            mock_client.__aexit__ = AsyncMock(return_value=None)
            mock_client.query = AsyncMock()

            # Return an error ResultMessage
            from claude_agent_sdk import ResultMessage
            mock_result = MagicMock(spec=ResultMessage)
            mock_result.is_error = True
            mock_result.result = "Something went wrong"

            async def mock_receive():
                yield mock_result

            mock_client.receive_messages = mock_receive
            mock_client_class.return_value = mock_client

            results = await runner.run()

        assert "Something went wrong" in results["errors"]


class TestRunCDDFunction:
    """Tests for the convenience run_cdd function."""

    @pytest.mark.asyncio
    async def test_run_cdd_creates_runner(self, mock_settings, tmp_path):
        """run_cdd should create and run a CDDRunner."""
        with patch("cdd_runner.CDDRunner") as mock_runner_class:
            mock_runner = MagicMock()
            mock_runner.run = AsyncMock(return_value={"completed": True})
            mock_runner_class.return_value = mock_runner

            results = await run_cdd("Test Corp", output_dir=tmp_path)

            mock_runner_class.assert_called_once()
            mock_runner.run.assert_called_once()
            assert results["completed"] is True
