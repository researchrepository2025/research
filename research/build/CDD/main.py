#!/usr/bin/env python3
"""CDD - Commercial Due Diligence Multi-Agent System.

A sophisticated multi-agent system for conducting institutional-quality
commercial due diligence analysis, similar to Bain, McKinsey, or L.E.K.
"""

import asyncio
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from cdd_runner import CDDRunner, run_cdd
from agents import get_all_agents
from config import get_settings

app = typer.Typer(
    name="cdd",
    help="Commercial Due Diligence Multi-Agent System",
    add_completion=False,
)
console = Console()


@app.command()
def analyze(
    company: str = typer.Argument(..., help="Name of the company to analyze"),
    output_dir: Optional[Path] = typer.Option(
        None,
        "--output", "-o",
        help="Output directory for analysis results",
    ),
    model: str = typer.Option(
        "opus",
        "--model", "-m",
        help="Model for orchestration (sonnet, opus, haiku)",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose", "-v",
        help="Enable verbose output",
    ),
) -> None:
    """Run Commercial Due Diligence analysis on a company."""
    console.print(Panel(
        f"[bold]CDD Analysis[/bold]\n\nCompany: {company}",
        title="Starting Analysis",
    ))

    async def _run():
        runner = CDDRunner(company_name=company, output_dir=output_dir)
        return await runner.run()

    try:
        results = asyncio.run(_run())

        if results.get("completed"):
            console.print("\n[bold green]Analysis Complete![/bold green]")
            console.print(f"Output saved to: {results.get('output_dir')}")
        else:
            console.print("\n[bold yellow]Analysis finished with issues[/bold yellow]")
            for error in results.get("errors", []):
                console.print(f"  [red]• {error}[/red]")

    except KeyboardInterrupt:
        console.print("\n[yellow]Analysis cancelled by user[/yellow]")
        raise typer.Exit(1)
    except Exception as e:
        console.print(f"\n[red]Error: {e}[/red]")
        raise typer.Exit(1)


@app.command()
def list_agents() -> None:
    """List all available agents in the CDD system."""
    agents = get_all_agents()

    for layer_name in ["orchestration", "research", "domain", "quality", "synthesis", "output"]:
        layer_agents = agents.get_by_layer(layer_name)  # type: ignore

        table = Table(title=f"Layer: {layer_name.title()}")
        table.add_column("Agent", style="cyan")
        table.add_column("Description", style="white")

        for name, defn in layer_agents.items():
            # Truncate description for display
            desc = defn.description[:80] + "..." if len(defn.description) > 80 else defn.description
            table.add_row(name, desc)

        console.print(table)
        console.print()


@app.command()
def info() -> None:
    """Show system configuration information."""
    try:
        settings = get_settings()

        table = Table(title="CDD Configuration")
        table.add_column("Setting", style="cyan")
        table.add_column("Value", style="white")

        table.add_row("Default Model", settings.default_model)
        table.add_row("Orchestrator Model", settings.orchestrator_model)
        table.add_row("Research Model", settings.research_model)
        table.add_row("Analysis Model", settings.analysis_model)
        table.add_row("Synthesis Model", settings.synthesis_model)
        table.add_row("Output Directory", str(settings.output_dir))
        table.add_row("Checkpoints Enabled", str(settings.enable_checkpoints))
        table.add_row("Permission Mode", settings.permission_mode)

        console.print(table)

    except Exception as e:
        console.print(f"[red]Error loading configuration: {e}[/red]")
        console.print("[yellow]Ensure ANTHROPIC_API_KEY is set in your environment[/yellow]")


@app.command()
def version() -> None:
    """Show version information."""
    console.print(Panel(
        "[bold]CDD - Commercial Due Diligence System[/bold]\n\n"
        "Version: 0.1.0\n"
        "Built with Claude Agent SDK\n\n"
        "A multi-agent system for institutional-quality\n"
        "commercial due diligence analysis.",
        title="About CDD",
    ))


def main() -> None:
    """Main entry point."""
    app()


if __name__ == "__main__":
    main()
