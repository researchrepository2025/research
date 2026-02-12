"""Session management for CDD analysis state persistence.

Provides both Redis-backed and in-memory storage options for
checkpoint state persistence across requests.
"""

import json
from datetime import timedelta
from typing import Optional

from backend.models.state import CDDAgentState


class SessionManager:
    """Manages CDD session state with optional Redis persistence.

    Falls back to in-memory storage if Redis is not available.
    """

    def __init__(self, redis_url: str | None = None):
        """Initialize session manager.

        Args:
            redis_url: Redis connection URL. If None, uses in-memory storage.
        """
        self.redis_url = redis_url
        self._redis = None
        self._memory_store: dict[str, str] = {}
        self._ttl = timedelta(hours=24)

    async def connect(self) -> bool:
        """Connect to Redis if URL is provided.

        Returns:
            True if connected to Redis, False if using memory storage.
        """
        if not self.redis_url:
            return False

        try:
            import aioredis
            self._redis = await aioredis.from_url(self.redis_url)
            # Test connection
            await self._redis.ping()
            return True
        except Exception:
            # Fall back to memory storage
            self._redis = None
            return False

    async def disconnect(self):
        """Disconnect from Redis."""
        if self._redis:
            await self._redis.close()
            self._redis = None

    def _key(self, session_id: str) -> str:
        """Generate storage key for session."""
        return f"cdd:session:{session_id}"

    async def save_session(self, session_id: str, state: CDDAgentState):
        """Save session state.

        Args:
            session_id: Unique session identifier.
            state: Current CDDAgentState to persist.
        """
        data = state.model_dump_json()

        if self._redis:
            await self._redis.setex(
                self._key(session_id),
                int(self._ttl.total_seconds()),
                data,
            )
        else:
            self._memory_store[self._key(session_id)] = data

    async def get_session(self, session_id: str) -> Optional[CDDAgentState]:
        """Retrieve session state.

        Args:
            session_id: Session identifier to retrieve.

        Returns:
            CDDAgentState if found, None otherwise.
        """
        if self._redis:
            data = await self._redis.get(self._key(session_id))
            if data:
                return CDDAgentState.model_validate_json(data)
        else:
            data = self._memory_store.get(self._key(session_id))
            if data:
                return CDDAgentState.model_validate_json(data)

        return None

    async def delete_session(self, session_id: str):
        """Delete a session.

        Args:
            session_id: Session identifier to delete.
        """
        if self._redis:
            await self._redis.delete(self._key(session_id))
        else:
            self._memory_store.pop(self._key(session_id), None)

    async def list_sessions(self) -> list[str]:
        """List all active session IDs.

        Returns:
            List of session identifiers.
        """
        if self._redis:
            keys = await self._redis.keys("cdd:session:*")
            return [k.decode().split(":")[-1] for k in keys]
        else:
            return [
                k.split(":")[-1]
                for k in self._memory_store.keys()
                if k.startswith("cdd:session:")
            ]

    async def session_exists(self, session_id: str) -> bool:
        """Check if a session exists.

        Args:
            session_id: Session identifier to check.

        Returns:
            True if session exists, False otherwise.
        """
        if self._redis:
            return await self._redis.exists(self._key(session_id)) > 0
        else:
            return self._key(session_id) in self._memory_store
