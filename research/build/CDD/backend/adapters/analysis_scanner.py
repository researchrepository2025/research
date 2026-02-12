"""Scans the outputs directory for previous CDD analyses.

This module provides functionality to discover and load previous analyses
from the outputs/ directory structure.
"""

import os
import uuid
from datetime import datetime
from pathlib import Path

from backend.models.state import (
    CDDAgentState,
    GeneratedFile,
    PhaseProgress,
    PhaseStatus,
    PreviousAnalysis,
)


class AnalysisScanner:
    """Scans outputs directory for previous CDD analyses."""

    def __init__(self, outputs_dir: str | Path = "outputs"):
        """Initialize scanner with outputs directory path.

        Args:
            outputs_dir: Path to the outputs directory.
        """
        self.outputs_dir = Path(outputs_dir)

    def list_analyses(self) -> list[PreviousAnalysis]:
        """List all previous analyses in the outputs directory.

        Returns:
            List of PreviousAnalysis summaries.
        """
        analyses = []

        if not self.outputs_dir.exists():
            return analyses

        for item in self.outputs_dir.iterdir():
            if item.is_dir() and not item.name.startswith("."):
                analysis = self._scan_analysis_directory(item)
                if analysis:
                    analyses.append(analysis)

        # Sort by last modified (most recent first)
        analyses.sort(key=lambda a: a.last_modified, reverse=True)
        return analyses

    def _scan_analysis_directory(self, directory: Path) -> PreviousAnalysis | None:
        """Scan a single analysis directory.

        Args:
            directory: Path to the company analysis directory.

        Returns:
            PreviousAnalysis summary or None if empty.
        """
        files = []
        total_size = 0
        last_modified = datetime.min
        has_report = False

        for item in directory.iterdir():
            if item.is_file():
                files.append(item.name)
                stat = item.stat()
                total_size += stat.st_size
                mod_time = datetime.fromtimestamp(stat.st_mtime)
                if mod_time > last_modified:
                    last_modified = mod_time

                # Check for report files
                if item.name.lower() in ["readme.md", "index.md", "00_index.txt"]:
                    has_report = True

        if not files:
            return None

        return PreviousAnalysis(
            company_name=directory.name.replace("_", " "),
            directory_path=str(directory),
            file_count=len(files),
            total_size=total_size,
            last_modified=last_modified,
            has_report=has_report,
            files=sorted(files),
        )

    def load_analysis(self, company_name: str) -> CDDAgentState | None:
        """Load a previous analysis state from disk.

        Args:
            company_name: Name of the company (directory name).

        Returns:
            CDDAgentState reconstructed from disk files, or None if not found.
        """
        # Normalize company name to directory format
        dir_name = company_name.replace(" ", "_")
        directory = self.outputs_dir / dir_name

        if not directory.exists():
            # Try without underscore conversion
            directory = self.outputs_dir / company_name
            if not directory.exists():
                return None

        # Scan for files
        generated_files = []
        for item in directory.iterdir():
            if item.is_file():
                generated_file = self._create_generated_file(item)
                generated_files.append(generated_file)

        # Sort files by modification time
        generated_files.sort(key=lambda f: f.created_at, reverse=True)

        # Create reconstructed state
        return CDDAgentState(
            session_id=str(uuid.uuid4()),
            company_name=company_name,
            started_at=generated_files[-1].created_at if generated_files else datetime.utcnow(),
            current_phase=6,  # Assume completed
            phases=self._create_completed_phases(),
            active_agents=[],
            completed_agents=[],
            findings=[],
            current_checkpoint=None,
            checkpoint_history=[],
            coverage={
                "market": 1.0,
                "customer": 1.0,
                "company": 1.0,
                "competitor": 1.0,
            },
            streaming_messages=[],
            current_tool_call=None,
            generated_files=generated_files,
            final_report_ready=True,
            errors=[],
        )

    def _create_generated_file(self, file_path: Path) -> GeneratedFile:
        """Create a GeneratedFile from a file path.

        Args:
            file_path: Path to the file.

        Returns:
            GeneratedFile with metadata and preview.
        """
        stat = file_path.stat()
        ext = file_path.suffix.lower()

        # Determine file type
        file_type = "text"
        if ext in [".md", ".markdown"]:
            file_type = "markdown"
        elif ext == ".json":
            file_type = "json"
        elif ext == ".txt":
            file_type = "text"

        # Read preview (first 500 chars)
        preview = ""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read(500)
                preview = content + ("..." if len(content) >= 500 else "")
        except Exception:
            preview = "[Unable to read file preview]"

        return GeneratedFile(
            id=str(uuid.uuid4()),
            file_path=str(file_path),
            filename=file_path.name,
            file_type=file_type,
            size=stat.st_size,
            preview=preview,
            created_at=datetime.fromtimestamp(stat.st_mtime),
            agent=None,
        )

    def _create_completed_phases(self) -> list[PhaseProgress]:
        """Create phase progress for a completed analysis.

        Returns:
            List of completed PhaseProgress objects.
        """
        return [
            PhaseProgress(
                phase_name="Intake & Scoping",
                phase_number=1,
                status=PhaseStatus.COMPLETED,
                agents_total=2,
                agents_completed=2,
            ),
            PhaseProgress(
                phase_name="Research",
                phase_number=2,
                status=PhaseStatus.COMPLETED,
                agents_total=4,
                agents_completed=4,
            ),
            PhaseProgress(
                phase_name="Domain Analysis",
                phase_number=3,
                status=PhaseStatus.COMPLETED,
                agents_total=19,
                agents_completed=19,
            ),
            PhaseProgress(
                phase_name="Quality Assurance",
                phase_number=4,
                status=PhaseStatus.COMPLETED,
                agents_total=4,
                agents_completed=4,
            ),
            PhaseProgress(
                phase_name="Synthesis",
                phase_number=5,
                status=PhaseStatus.COMPLETED,
                agents_total=8,
                agents_completed=8,
            ),
            PhaseProgress(
                phase_name="Output Generation",
                phase_number=6,
                status=PhaseStatus.COMPLETED,
                agents_total=5,
                agents_completed=5,
            ),
        ]
