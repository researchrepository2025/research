"""Pytest configuration and shared fixtures."""

import os
import pytest
from pathlib import Path

# Ensure we're in the project directory
PROJECT_ROOT = Path(__file__).parent.parent
os.chdir(PROJECT_ROOT)


@pytest.fixture
def project_root() -> Path:
    """Return the project root directory."""
    return PROJECT_ROOT


@pytest.fixture
def sample_company_name() -> str:
    """Sample company name for testing."""
    return "Acme Corp"


@pytest.fixture
def mock_settings(monkeypatch):
    """Mock settings with test values."""
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key-for-unit-tests")
    monkeypatch.setenv("DEFAULT_MODEL", "haiku")
    monkeypatch.setenv("ORCHESTRATOR_MODEL", "haiku")
    monkeypatch.setenv("RESEARCH_MODEL", "haiku")
    monkeypatch.setenv("ANALYSIS_MODEL", "haiku")
    monkeypatch.setenv("SYNTHESIS_MODEL", "haiku")
