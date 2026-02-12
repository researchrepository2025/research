"""API routes for CDD CopilotKit backend.

Provides endpoints for:
- Starting CDD analysis (SSE streaming)
- Checkpoint approval/rejection
- Session management
"""

from typing import Optional

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from backend.adapters.analysis_scanner import AnalysisScanner
from backend.adapters.cdd_agent_adapter import CDDAgentAdapter
from backend.adapters.session_manager import SessionManager


# Initialize components (will be overridden in main.py with proper config)
session_manager = SessionManager()
adapter = CDDAgentAdapter(session_manager)
analysis_scanner = AnalysisScanner()

router = APIRouter(prefix="/api/cdd", tags=["cdd"])


class StartAnalysisRequest(BaseModel):
    """Request body for starting a CDD analysis."""
    company_name: str
    session_id: Optional[str] = None


class CheckpointResponse(BaseModel):
    """Request body for checkpoint response."""
    checkpoint_id: str
    approved: bool
    feedback: Optional[str] = None


def set_session_manager(sm: SessionManager):
    """Set the session manager for routes.

    Args:
        sm: Configured SessionManager instance.
    """
    global session_manager, adapter
    session_manager = sm
    adapter = CDDAgentAdapter(session_manager)


@router.post("/analyze")
async def start_analysis(request: StartAnalysisRequest) -> StreamingResponse:
    """Start a new CDD analysis or resume an existing one.

    Args:
        request: Analysis request with company name and optional session ID.

    Returns:
        SSE stream of AG-UI events.

    Raises:
        HTTPException: If session_id provided but not found.
    """
    try:
        return await adapter.handle_run(
            company_name=request.company_name,
            session_id=request.session_id,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/sessions/{session_id}/checkpoint")
async def respond_to_checkpoint(
    session_id: str,
    response: CheckpointResponse,
) -> StreamingResponse:
    """Respond to a pending checkpoint (approve/reject).

    Args:
        session_id: Session with pending checkpoint.
        response: Approval response with feedback.

    Returns:
        SSE stream of continued AG-UI events (if approved) or completion.

    Raises:
        HTTPException: If session or checkpoint not found.
    """
    try:
        return await adapter.handle_checkpoint_response(
            session_id=session_id,
            checkpoint_id=response.checkpoint_id,
            approved=response.approved,
            feedback=response.feedback,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/sessions/{session_id}")
async def get_session_state(session_id: str):
    """Get current state of a session.

    Args:
        session_id: Session to retrieve.

    Returns:
        CDDAgentState as JSON.

    Raises:
        HTTPException: If session not found.
    """
    state = await session_manager.get_session(session_id)
    if not state:
        raise HTTPException(status_code=404, detail="Session not found")
    return state.model_dump(mode="json")


@router.get("/sessions")
async def list_sessions():
    """List all active sessions.

    Returns:
        Dictionary with list of session IDs.
    """
    sessions = await session_manager.list_sessions()
    return {"sessions": sessions}


@router.delete("/sessions/{session_id}")
async def delete_session(session_id: str):
    """Delete a session.

    Args:
        session_id: Session to delete.

    Returns:
        Confirmation message.
    """
    await session_manager.delete_session(session_id)
    return {"status": "deleted", "session_id": session_id}


@router.get("/analyses")
async def list_analyses():
    """List all previous analyses from the outputs directory.

    Returns:
        List of PreviousAnalysis summaries.
    """
    analyses = analysis_scanner.list_analyses()
    return {
        "analyses": [a.model_dump(mode="json") for a in analyses],
        "count": len(analyses),
    }


@router.get("/analyses/{company_name}")
async def get_analysis(company_name: str):
    """Load a previous analysis state from disk.

    Args:
        company_name: Name of the company (directory name).

    Returns:
        Reconstructed CDDAgentState from disk files.

    Raises:
        HTTPException: If analysis not found.
    """
    state = analysis_scanner.load_analysis(company_name)
    if not state:
        raise HTTPException(status_code=404, detail=f"Analysis not found: {company_name}")
    return state.model_dump(mode="json")


@router.get("/health")
async def health_check():
    """Health check endpoint.

    Returns:
        Service status.
    """
    return {
        "status": "healthy",
        "service": "cdd-backend",
        "version": "0.1.0",
    }
