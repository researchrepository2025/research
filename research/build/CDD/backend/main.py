"""FastAPI application for CDD CopilotKit backend.

This is the main entry point for the backend server that:
1. Provides CDD analysis API with AG-UI event streaming
2. Manages session state for checkpoint flow
3. Integrates with existing CDD multi-agent system
"""

import os
import sys
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Add parent directory to path for CDD imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.adapters.session_manager import SessionManager
from backend.api.routes import router, set_session_manager


# Get Redis URL from environment (optional)
REDIS_URL = os.getenv("REDIS_URL")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager.

    Handles startup (connecting to Redis) and shutdown (disconnecting).
    """
    # Startup
    session_manager = SessionManager(redis_url=REDIS_URL)
    connected = await session_manager.connect()
    if connected:
        print("Connected to Redis for session storage")
    else:
        print("Using in-memory session storage")

    set_session_manager(session_manager)

    yield

    # Shutdown
    await session_manager.disconnect()


app = FastAPI(
    title="CDD Multi-Agent System API",
    description="Commercial Due Diligence analysis with CopilotKit integration",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS configuration for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Next.js dev server
        "http://127.0.0.1:3000",
        "http://localhost:3001",  # Next.js fallback port
        "http://127.0.0.1:3001",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Session-ID"],
)

# Include API routes
app.include_router(router)


@app.get("/")
async def root():
    """Root endpoint with API info."""
    return {
        "message": "CDD Multi-Agent System API",
        "version": "0.1.0",
        "docs": "/docs",
        "openapi": "/openapi.json",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
