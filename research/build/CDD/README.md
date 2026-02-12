# CDD - Commercial Due Diligence Multi-Agent System

A sophisticated 46-agent system for conducting institutional-quality commercial due diligence analysis, similar to Bain, McKinsey, or L.E.K. Consulting.

## Overview

CDD is built on the Claude Agent SDK and uses a hierarchical multi-agent architecture to perform comprehensive commercial due diligence across four key domains:

- **Market Analysis**: Size, growth drivers, projections, value chain, segmentation
- **Customer Analysis**: Segments, preferences, purchasing criteria, trends
- **Company Analysis**: Products, strategy, financials, market position
- **Competitor Analysis**: Profiles, positioning, dynamics, threats

## Architecture

The system consists of **46 agents** organized into **6 layers**:

```
Layer 1: Orchestration (6 agents)
├── Main Orchestrator - Coordinates entire workflow
├── Checkpoint Manager - Human-in-the-loop approval gates
├── Market Supervisor - Oversees market analysis
├── Customer Supervisor - Oversees customer analysis
├── Company Supervisor - Oversees company analysis
└── Competitor Supervisor - Oversees competitive analysis

Layer 2: Research (4 agents)
├── Web Research Agent - General information gathering
├── Financial Data Agent - Public filings and metrics
├── News & Press Agent - Recent developments
└── Industry Research Agent - Market reports and frameworks

Layer 3: Domain Analysis (19 agents)
├── Market: Definition, Sizing, Growth Drivers, Projections, Value Chain, Segmentation
├── Customer: Segmentation, Preferences/KPC, Economics, Trends
├── Company: Profile, Products, Strategy, Financials, Position
└── Competitor: Identification, Profiler, Dynamics, Positioning

Layer 4: Quality (4 agents)
├── Fact Checker - Verifies accuracy
├── Consistency Agent - Checks contradictions
├── Gap Identifier - Finds missing information
└── Assumption Validator - Tests assumptions

Layer 5: Synthesis (8 agents)
├── Section Synthesizers (Market, Customer, Company, Competitor)
├── Cross-Section Synthesizer - Connects insights
├── Executive Summary Agent - Distills findings
├── Recommendations Agent - Formulates guidance
└── "So What" Agent - Ensures actionable insights

Layer 6: Output (5 agents)
├── Report Writer - Compiles final document
├── Data Visualization Agent - Creates charts
├── Slide Content Agent - Structures presentation
├── Slide Designer Agent - HTML slide templates
└── Design QA Agent - Quality checks visuals
```

## Installation

### Prerequisites

- Python 3.10+
- Anthropic API key

### Setup

```bash
# Clone or navigate to the project
cd CDD

# Create virtual environment with uv (recommended)
uv venv
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt

# Or with pip
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your API key
ANTHROPIC_API_KEY=your_api_key_here
```

## Usage

### Run Analysis

```bash
# Basic usage
python main.py analyze "Company Name"

# With custom output directory
python main.py analyze "Company Name" --output ./my-analysis

# With specific model
python main.py analyze "Company Name" --model opus
```

### Other Commands

```bash
# List all available agents
python main.py list-agents

# Show configuration
python main.py info

# Version information
python main.py version
```

## Workflow

The CDD analysis follows six phases with human checkpoints:

1. **Intake & Scoping**
   - Define market boundaries
   - Identify competitor set
   - ⛔ CHECKPOINT: Approve scope

2. **Research** (parallel execution)
   - Web research
   - Financial data gathering
   - News monitoring
   - Industry reports

3. **Domain Analysis**
   - Market analysis
   - Customer analysis
   - Company analysis
   - Competitive analysis
   - ⛔ CHECKPOINT: Review findings

4. **Quality Assurance**
   - Fact checking
   - Consistency validation
   - Gap identification
   - Assumption testing

5. **Synthesis**
   - Section writing
   - Cross-domain insights
   - Executive summary
   - Recommendations
   - ⛔ CHECKPOINT: Review draft

6. **Output Generation**
   - Final report
   - Data visualizations
   - Presentation slides
   - ⛔ CHECKPOINT: Final approval

## Output

The system generates:

- **Narrative Report**: Complete CDD document
- **Executive Summary**: 2-3 page distillation
- **Data Exhibits**: Charts, tables, visualizations
- **Presentation**: HTML slides (convertible to PowerPoint)
- **Recommendations**: Investment assessment and next steps

## Configuration Options

| Setting | Default | Description |
|---------|---------|-------------|
| `ANTHROPIC_API_KEY` | (required) | Your Anthropic API key |
| `ORCHESTRATOR_MODEL` | opus | Model for orchestration |
| `RESEARCH_MODEL` | sonnet | Model for research agents |
| `ANALYSIS_MODEL` | sonnet | Model for analysis agents |
| `SYNTHESIS_MODEL` | opus | Model for synthesis agents |
| `PERMISSION_MODE` | acceptEdits | Auto-accept file changes |
| `ENABLE_CHECKPOINTS` | true | Enable human review gates |

## Project Structure

```
CDD/
├── main.py              # CLI entry point
├── cdd_runner.py        # Core runner logic
├── agents/              # Agent definitions
│   ├── orchestration/   # Layer 1
│   ├── research/        # Layer 2
│   ├── domain/          # Layer 3
│   ├── quality/         # Layer 4
│   ├── synthesis/       # Layer 5
│   └── output/          # Layer 6
├── config/              # Configuration
├── templates/           # Output templates
├── outputs/             # Generated outputs
├── requirements.txt     # Dependencies
└── pyproject.toml       # Project config
```

## Built With

- [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-python) - Multi-agent framework
- [Typer](https://typer.tiangolo.com/) - CLI framework
- [Rich](https://rich.readthedocs.io/) - Terminal formatting
- [Pydantic](https://docs.pydantic.dev/) - Configuration management
- [Plotly](https://plotly.com/python/) - Data visualization
- [python-pptx](https://python-pptx.readthedocs.io/) - PowerPoint generation

## License

MIT
