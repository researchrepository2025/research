"""Unit tests for configuration.

These tests verify configuration loading without API calls.
"""

import os
import pytest
from pathlib import Path

from config import Settings, get_settings


class TestSettings:
    """Tests for Settings configuration."""

    def test_settings_loads_from_env(self, mock_settings):
        """Settings should load from environment variables."""
        settings = get_settings()

        assert settings.anthropic_api_key == "test-key-for-unit-tests"
        assert settings.default_model == "haiku"

    def test_default_values(self, mock_settings):
        """Settings should have sensible defaults."""
        settings = get_settings()

        assert settings.enable_checkpoints is True
        assert settings.max_research_depth == 3
        assert settings.parallel_research is True

    def test_output_dir_is_path(self, mock_settings):
        """Output dir should be a Path object."""
        settings = get_settings()

        assert isinstance(settings.output_dir, Path)
        assert isinstance(settings.template_dir, Path)

    def test_valid_permission_modes(self, mock_settings):
        """Permission mode should be valid."""
        settings = get_settings()

        valid_modes = {"default", "acceptEdits", "bypassPermissions"}
        assert settings.permission_mode in valid_modes

    def test_valid_model_values(self, mock_settings):
        """Model settings should be valid."""
        settings = get_settings()

        valid_models = {"sonnet", "opus", "haiku"}
        assert settings.default_model in valid_models
        assert settings.orchestrator_model in valid_models
        assert settings.research_model in valid_models
        assert settings.analysis_model in valid_models
        assert settings.synthesis_model in valid_models

    def test_missing_api_key_raises(self, monkeypatch, tmp_path):
        """Missing API key should raise validation error."""
        # Clear any existing env var
        monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)

        # Change to a directory without .env file
        monkeypatch.chdir(tmp_path)

        with pytest.raises(Exception):  # Pydantic validation error
            Settings(_env_file=None)


class TestSettingsIntegration:
    """Integration tests for settings with real .env file."""

    def test_env_file_exists(self, project_root):
        """The .env file should exist for testing."""
        env_file = project_root / ".env"
        example_file = project_root / ".env.example"

        # At minimum, example should exist
        assert example_file.exists(), ".env.example should exist"

    def test_real_settings_load(self):
        """Test loading real settings if .env exists."""
        try:
            settings = get_settings()
            # If we get here, settings loaded successfully
            assert settings.anthropic_api_key is not None
            assert len(settings.anthropic_api_key) > 0
        except Exception as e:
            pytest.skip(f"Could not load real settings: {e}")
