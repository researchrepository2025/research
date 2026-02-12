"""State models for CDD analysis tracking.

These Pydantic models define the complete state that is synchronized
between the backend and frontend via AG-UI protocol events.
"""

from datetime import datetime
from enum import Enum
from typing import Any, Literal

from pydantic import BaseModel, Field


class PhaseStatus(str, Enum):
    """Status of a CDD analysis phase."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    AWAITING_APPROVAL = "awaiting_approval"
    COMPLETED = "completed"
    ERROR = "error"


class AgentStatus(str, Enum):
    """Status of an individual agent."""
    IDLE = "idle"
    RUNNING = "running"
    COMPLETED = "completed"
    ERROR = "error"


CheckpointType = Literal["scope", "findings", "draft", "final"]


class PhaseProgress(BaseModel):
    """Progress tracking for a single CDD phase."""
    phase_name: str
    phase_number: int
    status: PhaseStatus = PhaseStatus.PENDING
    started_at: datetime | None = None
    completed_at: datetime | None = None
    agents_total: int = 0
    agents_completed: int = 0


class AgentProgress(BaseModel):
    """Progress tracking for an individual agent."""
    agent_name: str
    layer: str
    status: AgentStatus = AgentStatus.IDLE
    started_at: datetime | None = None
    completed_at: datetime | None = None
    message: str | None = None
    findings_count: int = 0


class Finding(BaseModel):
    """A research finding from an agent."""
    id: str
    agent: str
    layer: str
    category: Literal["market", "customer", "company", "competitor"]
    title: str
    content: str
    sources: list[str] = Field(default_factory=list)
    confidence: float | None = None
    timestamp: datetime


class CheckpointData(BaseModel):
    """Data for a human-in-the-loop checkpoint."""
    checkpoint_id: str
    checkpoint_type: CheckpointType
    title: str
    description: str
    data: dict[str, Any] = Field(default_factory=dict)
    requires_approval: bool = True
    approved: bool | None = None
    feedback: str | None = None


class GeneratedFile(BaseModel):
    """A file generated during CDD analysis."""
    id: str
    file_path: str
    filename: str
    file_type: str = "markdown"
    size: int
    preview: str  # First ~500 chars of content
    created_at: datetime
    agent: str | None = None  # Which agent created this file


class PreviousAnalysis(BaseModel):
    """Summary of a previous CDD analysis stored on disk."""
    company_name: str
    directory_path: str
    file_count: int
    total_size: int  # bytes
    last_modified: datetime
    has_report: bool  # Has README.md or INDEX.md
    files: list[str] = Field(default_factory=list)  # List of filenames


class CDDAgentState(BaseModel):
    """Complete state for CDD analysis - synced with frontend via AG-UI.

    This is the main state object that gets serialized and sent to the
    frontend. It tracks all aspects of the multi-agent CDD workflow.
    """

    # Session identification
    session_id: str
    company_name: str
    started_at: datetime

    # Phase tracking (6 phases)
    current_phase: int = 1
    phases: list[PhaseProgress] = Field(default_factory=list)

    # Agent tracking (46 agents across 6 layers)
    active_agents: list[AgentProgress] = Field(default_factory=list)
    completed_agents: list[AgentProgress] = Field(default_factory=list)

    # Research findings (streaming)
    findings: list[Finding] = Field(default_factory=list)

    # Checkpoint state (4 checkpoints)
    current_checkpoint: CheckpointData | None = None
    checkpoint_history: list[CheckpointData] = Field(default_factory=list)

    # Analysis metadata
    market_definition: str | None = None
    competitor_set: list[str] = Field(default_factory=list)

    # Coverage metrics (0.0 - 1.0)
    coverage: dict[str, float] = Field(default_factory=lambda: {
        "market": 0.0,
        "customer": 0.0,
        "company": 0.0,
        "competitor": 0.0,
    })

    # Streaming output
    streaming_messages: list[dict[str, str]] = Field(default_factory=list)  # Live agent output
    current_tool_call: dict[str, Any] | None = None  # Active tool being executed

    # Generated files
    generated_files: list[GeneratedFile] = Field(default_factory=list)

    # Output state
    report_sections: dict[str, str] = Field(default_factory=dict)
    final_report_ready: bool = False

    # Error tracking
    errors: list[str] = Field(default_factory=list)

    @classmethod
    def create_new(cls, session_id: str, company_name: str) -> "CDDAgentState":
        """Factory method to create a new state with initialized phases."""
        return cls(
            session_id=session_id,
            company_name=company_name,
            started_at=datetime.utcnow(),
            phases=[
                PhaseProgress(
                    phase_name="Intake & Scoping",
                    phase_number=1,
                    agents_total=2,
                ),
                PhaseProgress(
                    phase_name="Research",
                    phase_number=2,
                    agents_total=4,
                ),
                PhaseProgress(
                    phase_name="Domain Analysis",
                    phase_number=3,
                    agents_total=19,
                ),
                PhaseProgress(
                    phase_name="Quality Assurance",
                    phase_number=4,
                    agents_total=4,
                ),
                PhaseProgress(
                    phase_name="Synthesis",
                    phase_number=5,
                    agents_total=8,
                ),
                PhaseProgress(
                    phase_name="Output Generation",
                    phase_number=6,
                    agents_total=5,
                ),
            ],
        )
