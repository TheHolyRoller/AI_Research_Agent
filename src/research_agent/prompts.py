from __future__ import annotations

from pathlib import Path

from research_agent.paths import PROMPTS_DIR

STAGE_FILES = {
    "main": "main.md",
    "system": "00_system.md",
    "intake": "01_intake.md",
    "plan": "02_plan.md",
    "gather": "03_gather.md",
    "extract": "04_extract.md",
    "verify": "05_verify.md",
    "synthesize": "06_synthesize.md",
    "export": "07_export.md",
    "icebreaker": "icebreaker.md",
}

PIPELINE_ORDER = [
    "system",
    "intake",
    "plan",
    "gather",
    "extract",
    "verify",
    "synthesize",
    "export",
]

STAGE_CHOICES = ["main", *PIPELINE_ORDER, "icebreaker"]


def prompt_path(stage: str) -> Path:
    key = stage.lower()
    if key not in STAGE_FILES:
        known = ", ".join(STAGE_CHOICES)
        raise ValueError(f"Unknown stage {stage!r}. Known: {known}")
    path = PROMPTS_DIR / STAGE_FILES[key]
    if not path.exists():
        raise FileNotFoundError(path)
    return path


def load_stage(stage: str) -> str:
    return prompt_path(stage).read_text(encoding="utf-8")


def stitch(include_index: bool = False) -> str:
    parts: list[str] = []
    if include_index:
        index = PROMPTS_DIR / "_index.md"
        if index.exists():
            parts.append(index.read_text(encoding="utf-8").rstrip())
    parts.append(load_stage("main").rstrip())
    return "\n\n---\n\n".join(parts) + "\n"
