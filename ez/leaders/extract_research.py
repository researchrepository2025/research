#!/usr/bin/env python3
"""Extract research outputs from subagent .jsonl transcripts into markdown files."""

import json
import os
import re
from pathlib import Path

SUBAGENTS_DIR = Path(
    "/Users/nicholaspate/.claude/projects/"
    "-Users-nicholaspate-Documents-01-Active-Corp-Strat-ezAI-leaders/"
    "97d79e70-4737-4e6b-9e6a-aba4f9fbbc59/subagents"
)
OUTPUT_DIR = Path("/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/leaders/research")

# Keyword-to-filename mapping. Order matters: more specific patterns first.
SEGMENT_MAP = [
    # Seed
    (["menlo", "vc", "venture"], "00-seed-menlo-vc.md"),
    # Horizontal
    (["copilot"], "01-horizontal-copilots.md"),
    (["agent platform", "agentic platform"], "02-horizontal-agent-platforms.md"),
    (["note-taking", "note taking", "notetaking", "meeting assistant"], "03-horizontal-note-taking.md"),
    (["presentation"], "04-horizontal-presentations.md"),
    # Departmental
    (["code", "software dev", "sw dev", "developer tool", "coding assistant"], "05-departmental-code-sw-dev.md"),
    (["it operation", "it ops", "itsm", "it service"], "06-departmental-it.md"),
    (["marketing"], "07-departmental-marketing.md"),
    (["customer success", "customer support", "cx ", "customer service"], "08-departmental-customer-success.md"),
    (["sales"], "09-departmental-sales.md"),
    (["hr ", "human resource", "talent", "recruiting", "people ops"], "10-departmental-hr.md"),
    (["data science", "data analytics", "ml ops", "mlops"], "11-departmental-data-science.md"),
    (["finance op", "accounting", "finops", "finance & accounting", "financial operations"], "12-departmental-finance-ops.md"),
    (["market research", "competitive intelligence"], "13-departmental-market-research.md"),
    # Vertical
    (["healthcare", "health care", "clinical", "medical"], "14-vertical-healthcare.md"),
    (["legal", "law firm", "contract"], "15-vertical-legal.md"),
    (["creator", "content creation", "creative"], "16-vertical-creators.md"),
    (["government", "govtech", "public sector", "federal"], "17-vertical-government.md"),
    (["education", "edtech", "learning"], "18-vertical-education.md"),
    (["home service", "field service", "plumbing", "hvac"], "19-vertical-home-services.md"),
    (["real estate"], "21-vertical-real-estate.md"),
    (["insurance", "insurtech"], "22-vertical-insurance.md"),
    (["manufacturing", "supply chain"], "23-vertical-manufacturing-supply-chain.md"),
    (["financial service", "fintech", "banking", "wealth management"], "20-vertical-finance.md"),
    # Synthesis / validation
    (["synthesis", "horizontal", "cross-cutting"], None),  # handled specially
    (["glean"], "validation-glean.md"),
    (["validat"], "validation-report.md"),
]


def get_text_from_content(content):
    """Extract text from message content (list of blocks or string)."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        texts = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                texts.append(item["text"])
        return "\n".join(texts)
    return ""


def identify_segment(first_user_text):
    """Match first user message text to a segment filename."""
    text_lower = first_user_text.lower()

    # Check for synthesis messages
    if "synthesis" in text_lower or "synthesize" in text_lower:
        if "horizontal" in text_lower:
            return "synthesis-horizontal.md"
        if "departmental" in text_lower:
            return "synthesis-departmental.md"
        if "vertical" in text_lower:
            return "synthesis-vertical.md"
        return "synthesis-general.md"

    for keywords, filename in SEGMENT_MAP:
        if filename is None:
            continue
        for kw in keywords:
            if kw in text_lower:
                return filename

    return None


def process_file(filepath):
    """Process a single .jsonl file and return (segment_filename, text_content, first_user_text)."""
    first_user_text = None
    last_assistant_text = None

    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue

            msg = obj.get("message", {})
            role = msg.get("role")
            content = msg.get("content", [])
            text = get_text_from_content(content)

            if role == "user" and first_user_text is None and text.strip():
                first_user_text = text
            elif role == "assistant" and text.strip():
                last_assistant_text = text

    return first_user_text, last_assistant_text


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    jsonl_files = sorted(SUBAGENTS_DIR.glob("agent-a[0-9a-f]*.jsonl"))
    # Skip compact files
    jsonl_files = [f for f in jsonl_files if "compact" not in f.name]

    print(f"Found {len(jsonl_files)} subagent transcript files (excluding compact files)")
    print()

    created = []
    unmatched = []
    filename_collisions = {}

    for filepath in jsonl_files:
        first_user, last_assistant = process_file(filepath)

        if not first_user:
            print(f"  SKIP (no user message): {filepath.name}")
            continue
        if not last_assistant:
            print(f"  SKIP (no assistant output): {filepath.name}")
            continue

        segment_file = identify_segment(first_user)
        if not segment_file:
            # Show first 200 chars of user message for debugging
            preview = first_user[:200].replace("\n", " ")
            unmatched.append((filepath.name, preview))
            continue

        # Handle collisions: append agent ID
        out_path = OUTPUT_DIR / segment_file
        if segment_file in filename_collisions:
            # Already used this filename, make unique
            base, ext = os.path.splitext(segment_file)
            agent_id = filepath.stem.split("-")[-1][:8]
            segment_file = f"{base}-{agent_id}{ext}"
            out_path = OUTPUT_DIR / segment_file

        filename_collisions[segment_file] = filepath.name

        with open(out_path, "w") as f:
            f.write(last_assistant)

        size_kb = out_path.stat().st_size / 1024
        created.append((segment_file, size_kb))
        print(f"  CREATED: {segment_file} ({size_kb:.1f} KB) <- {filepath.name}")

    print()
    print(f"=== SUMMARY ===")
    print(f"Files created: {len(created)}")
    total_kb = sum(s for _, s in created)
    print(f"Total size: {total_kb:.1f} KB")
    print()

    if unmatched:
        print(f"UNMATCHED ({len(unmatched)}):")
        for name, preview in unmatched:
            print(f"  {name}: {preview}")
        print()

    print("All files:")
    for fname, size in sorted(created):
        print(f"  {fname:50s} {size:7.1f} KB")


if __name__ == "__main__":
    main()
