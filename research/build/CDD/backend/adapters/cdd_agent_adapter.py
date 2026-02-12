"""Adapter that wraps CDDRunner for AG-UI protocol compatibility.

This adapter bridges the existing CDD multi-agent system with
CopilotKit's frontend by translating Claude SDK messages to
AG-UI protocol events streamed via SSE.
"""

import sys
import uuid
from datetime import datetime
from typing import AsyncIterator

from fastapi.responses import StreamingResponse

# Add parent directory to path to import CDD modules
sys.path.insert(0, "..")

from backend.adapters.event_translator import EventTranslator
from backend.adapters.session_manager import SessionManager
from backend.models.events import AGUIEvent
from backend.models.state import CDDAgentState, PhaseProgress, PhaseStatus


class CDDAgentAdapter:
    """Adapts CDDRunner to AG-UI protocol for CopilotKit integration.

    This adapter wraps the existing CDDRunner class and:
    1. Creates/manages session state
    2. Streams AG-UI events via SSE
    3. Handles checkpoint pause/resume flow
    """

    def __init__(self, session_manager: SessionManager):
        """Initialize adapter with session manager.

        Args:
            session_manager: SessionManager for state persistence.
        """
        self.session_manager = session_manager

    async def handle_run(
        self,
        company_name: str,
        session_id: str | None = None,
    ) -> StreamingResponse:
        """Handle a new CDD analysis run with SSE streaming.

        Args:
            company_name: Name of company to analyze.
            session_id: Optional session ID to resume.

        Returns:
            StreamingResponse with AG-UI events.

        Raises:
            ValueError: If session_id provided but not found.
        """
        # Create or restore session
        if session_id:
            state = await self.session_manager.get_session(session_id)
            if not state:
                raise ValueError(f"Session {session_id} not found")
        else:
            session_id = str(uuid.uuid4())
            state = CDDAgentState.create_new(session_id, company_name)
            await self.session_manager.save_session(session_id, state)

        return StreamingResponse(
            self._run_stream(state),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "X-Session-ID": session_id,
                "X-Accel-Buffering": "no",
            },
        )

    async def _run_stream(self, state: CDDAgentState) -> AsyncIterator[str]:
        """Stream CDD analysis as AG-UI events.

        Args:
            state: CDDAgentState for this analysis.

        Yields:
            SSE-formatted AG-UI event strings.
        """
        translator = EventTranslator(state)

        # Emit run started event
        yield AGUIEvent.run_started(state.session_id).to_sse()

        # Emit initial state snapshot
        yield AGUIEvent.state_snapshot(state.model_dump(mode="json")).to_sse()

        try:
            # Import CDD modules
            from cdd_runner import CDDRunner
            from config import get_settings

            settings = get_settings()

            # Create CDDRunner
            runner = CDDRunner(
                company_name=state.company_name,
                settings=settings,
            )

            # Create output directory before running (must exist for SDK cwd)
            runner.output_dir.mkdir(parents=True, exist_ok=True)

            # Build options and run
            options = runner._get_cdd_options()
            prompt = runner._build_orchestration_prompt()

            # Import SDK client
            from claude_agent_sdk import ClaudeSDKClient, ResultMessage

            async with ClaudeSDKClient(options=options) as client:
                await client.query(prompt)

                async for message in client.receive_messages():
                    # Translate Claude SDK message to AG-UI events
                    async for event in translator.translate(message):
                        yield event.to_sse()

                        # Save state periodically
                        await self.session_manager.save_session(
                            state.session_id, state
                        )

                        # Check for checkpoint - pause if needed
                        if (
                            state.current_checkpoint
                            and state.current_checkpoint.requires_approval
                            and state.current_checkpoint.approved is None
                        ):
                            # Wait for approval (handled via resume endpoint)
                            await self.session_manager.save_session(
                                state.session_id, state
                            )
                            return  # Stop streaming, wait for resume

                    # Check for completion
                    if isinstance(message, ResultMessage):
                        state.final_report_ready = True
                        yield AGUIEvent.state_snapshot(
                            state.model_dump(mode="json")
                        ).to_sse()
                        yield AGUIEvent.run_finished(
                            state.session_id, success=True
                        ).to_sse()
                        break

        except ImportError as e:
            # CDD modules not available - emit error
            error_msg = f"CDD system not available: {e}"
            state.errors.append(error_msg)
            yield AGUIEvent.run_error(error_msg).to_sse()

        except Exception as e:
            # General error
            error_msg = str(e)
            state.errors.append(error_msg)
            yield AGUIEvent.state_snapshot(state.model_dump(mode="json")).to_sse()
            yield AGUIEvent.run_error(error_msg).to_sse()

        finally:
            await self.session_manager.save_session(state.session_id, state)

    async def handle_checkpoint_response(
        self,
        session_id: str,
        checkpoint_id: str,
        approved: bool,
        feedback: str | None = None,
    ) -> StreamingResponse:
        """Handle checkpoint approval and resume analysis.

        Args:
            session_id: Session to resume.
            checkpoint_id: ID of checkpoint being responded to.
            approved: Whether checkpoint was approved.
            feedback: Optional feedback from user.

        Returns:
            StreamingResponse with continued AG-UI events.

        Raises:
            ValueError: If session or checkpoint not found.
        """
        state = await self.session_manager.get_session(session_id)
        if not state:
            raise ValueError(f"Session {session_id} not found")

        if not state.current_checkpoint:
            raise ValueError("No pending checkpoint")

        if state.current_checkpoint.checkpoint_id != checkpoint_id:
            raise ValueError("Checkpoint ID mismatch")

        # Record approval
        state.current_checkpoint.approved = approved
        state.current_checkpoint.feedback = feedback

        # Move to history
        state.checkpoint_history.append(state.current_checkpoint)
        state.current_checkpoint = None

        await self.session_manager.save_session(session_id, state)

        if approved:
            # Resume analysis
            return await self.handle_run(
                company_name=state.company_name,
                session_id=session_id,
            )
        else:
            # Analysis stopped
            return StreamingResponse(
                self._rejection_stream(state),
                media_type="text/event-stream",
            )

    async def _rejection_stream(
        self, state: CDDAgentState
    ) -> AsyncIterator[str]:
        """Stream rejection notification.

        Args:
            state: Current session state.

        Yields:
            SSE-formatted rejection event.
        """
        yield AGUIEvent.state_snapshot(state.model_dump(mode="json")).to_sse()
        yield AGUIEvent.run_finished(state.session_id, success=False).to_sse()

    async def get_session_state(self, session_id: str) -> CDDAgentState | None:
        """Get current state of a session.

        Args:
            session_id: Session to retrieve.

        Returns:
            CDDAgentState if found, None otherwise.
        """
        return await self.session_manager.get_session(session_id)
