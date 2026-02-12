"""CDD Multi-Agent System - Agent Definitions.

This module provides all agent definitions for the Commercial Due Diligence system.
Agents are organized into six layers:

Layer 1: Orchestration - Main orchestrator, checkpoint manager, domain supervisors
Layer 2: Research - Web research, financial data, news, industry research
Layer 3: Domain Analysis - Market, customer, company, competitor specialists
Layer 4: Quality - Fact checking, consistency, gap identification, assumption validation
Layer 5: Synthesis - Section writers, cross-section synthesis, executive summary
Layer 6: Output - Report writing, visualization, slide generation
"""

from .registry import AgentRegistry, get_all_agents
from .orchestration import get_orchestration_agents
from .research import get_research_agents
from .domain import get_domain_agents
from .quality import get_quality_agents
from .synthesis import get_synthesis_agents
from .output import get_output_agents

__all__ = [
    "AgentRegistry",
    "get_all_agents",
    "get_orchestration_agents",
    "get_research_agents",
    "get_domain_agents",
    "get_quality_agents",
    "get_synthesis_agents",
    "get_output_agents",
]
