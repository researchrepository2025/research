"""Configuration settings for CDD multi-agent system."""

from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Literal
from pathlib import Path


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # API Configuration
    anthropic_api_key: str = Field(..., alias="ANTHROPIC_API_KEY")

    # Model Configuration
    default_model: Literal["sonnet", "opus", "haiku"] = "sonnet"
    orchestrator_model: Literal["sonnet", "opus", "haiku"] = "opus"
    research_model: Literal["sonnet", "opus", "haiku"] = "sonnet"
    analysis_model: Literal["sonnet", "opus", "haiku"] = "sonnet"
    synthesis_model: Literal["sonnet", "opus", "haiku"] = "opus"

    # Paths
    output_dir: Path = Path("outputs")
    template_dir: Path = Path("templates")

    # Workflow Configuration
    enable_checkpoints: bool = True
    max_research_depth: int = 3
    parallel_research: bool = True

    # Permission Mode
    permission_mode: Literal["default", "acceptEdits", "bypassPermissions"] = "acceptEdits"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


def get_settings() -> Settings:
    """Get application settings singleton."""
    return Settings()
