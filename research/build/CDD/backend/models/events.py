"""AG-UI protocol event types for streaming to frontend.

The AG-UI (Agent-UI) protocol defines a standard format for streaming
agent events to frontend applications. CopilotKit uses this protocol
for real-time updates.
"""

import json
from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel


class AGUIEventType(str, Enum):
    """AG-UI protocol event types."""

    # Lifecycle events
    RUN_STARTED = "RUN_STARTED"
    RUN_FINISHED = "RUN_FINISHED"
    RUN_ERROR = "RUN_ERROR"

    # Message streaming
    TEXT_MESSAGE_START = "TEXT_MESSAGE_START"
    TEXT_MESSAGE_CONTENT = "TEXT_MESSAGE_CONTENT"
    TEXT_MESSAGE_END = "TEXT_MESSAGE_END"

    # Tool execution
    TOOL_CALL_START = "TOOL_CALL_START"
    TOOL_CALL_ARGS = "TOOL_CALL_ARGS"
    TOOL_CALL_END = "TOOL_CALL_END"

    # State synchronization
    STATE_SNAPSHOT = "STATE_SNAPSHOT"
    STATE_DELTA = "STATE_DELTA"

    # Custom events
    CUSTOM = "CUSTOM"

    # Checkpoint (human-in-the-loop)
    CHECKPOINT_PENDING = "CHECKPOINT_PENDING"
    CHECKPOINT_APPROVED = "CHECKPOINT_APPROVED"
    CHECKPOINT_REJECTED = "CHECKPOINT_REJECTED"

    # File operations
    FILE_CREATED = "FILE_CREATED"


class AGUIEvent(BaseModel):
    """Base class for AG-UI protocol events.

    Events are serialized as Server-Sent Events (SSE) for streaming
    to the frontend.
    """

    type: AGUIEventType
    data: dict[str, Any]
    timestamp: datetime = None

    def __init__(self, **data):
        if "timestamp" not in data or data["timestamp"] is None:
            data["timestamp"] = datetime.utcnow()
        super().__init__(**data)

    def to_sse(self) -> str:
        """Format as Server-Sent Event string."""
        payload = {
            "type": self.type.value,
            "data": self.data,
            "timestamp": self.timestamp.isoformat(),
        }
        return f"data: {json.dumps(payload)}\n\n"

    @classmethod
    def run_started(cls, session_id: str) -> "AGUIEvent":
        """Create a RUN_STARTED event."""
        return cls(
            type=AGUIEventType.RUN_STARTED,
            data={"session_id": session_id},
        )

    @classmethod
    def run_finished(cls, session_id: str, success: bool = True) -> "AGUIEvent":
        """Create a RUN_FINISHED event."""
        return cls(
            type=AGUIEventType.RUN_FINISHED,
            data={"session_id": session_id, "success": success},
        )

    @classmethod
    def run_error(cls, error: str) -> "AGUIEvent":
        """Create a RUN_ERROR event."""
        return cls(
            type=AGUIEventType.RUN_ERROR,
            data={"error": error},
        )

    @classmethod
    def text_message(cls, content: str, role: str = "assistant") -> "AGUIEvent":
        """Create a TEXT_MESSAGE_CONTENT event."""
        return cls(
            type=AGUIEventType.TEXT_MESSAGE_CONTENT,
            data={"content": content, "role": role},
        )

    @classmethod
    def tool_call_start(
        cls,
        tool_id: str,
        tool_name: str,
        arguments: dict[str, Any],
    ) -> "AGUIEvent":
        """Create a TOOL_CALL_START event."""
        return cls(
            type=AGUIEventType.TOOL_CALL_START,
            data={
                "tool_id": tool_id,
                "tool_name": tool_name,
                "arguments": arguments,
            },
        )

    @classmethod
    def tool_call_end(
        cls,
        tool_id: str,
        result: Any,
        success: bool = True,
    ) -> "AGUIEvent":
        """Create a TOOL_CALL_END event."""
        return cls(
            type=AGUIEventType.TOOL_CALL_END,
            data={
                "tool_id": tool_id,
                "result": result,
                "success": success,
            },
        )

    @classmethod
    def state_snapshot(cls, state: dict[str, Any]) -> "AGUIEvent":
        """Create a STATE_SNAPSHOT event with full state."""
        return cls(
            type=AGUIEventType.STATE_SNAPSHOT,
            data=state,
        )

    @classmethod
    def state_delta(cls, path: str, value: Any) -> "AGUIEvent":
        """Create a STATE_DELTA event for incremental update."""
        return cls(
            type=AGUIEventType.STATE_DELTA,
            data={"path": path, "value": value},
        )

    @classmethod
    def checkpoint_pending(cls, checkpoint_data: dict[str, Any]) -> "AGUIEvent":
        """Create a CHECKPOINT_PENDING event."""
        return cls(
            type=AGUIEventType.CHECKPOINT_PENDING,
            data=checkpoint_data,
        )

    @classmethod
    def custom(cls, event_name: str, data: dict[str, Any]) -> "AGUIEvent":
        """Create a CUSTOM event for application-specific data."""
        return cls(
            type=AGUIEventType.CUSTOM,
            data={"event_name": event_name, **data},
        )

    @classmethod
    def file_created(
        cls,
        file_path: str,
        filename: str,
        size: int,
        preview: str,
        file_type: str = "markdown",
    ) -> "AGUIEvent":
        """Create a FILE_CREATED event when an output file is generated."""
        return cls(
            type=AGUIEventType.FILE_CREATED,
            data={
                "file_path": file_path,
                "filename": filename,
                "size": size,
                "preview": preview,
                "file_type": file_type,
            },
        )
