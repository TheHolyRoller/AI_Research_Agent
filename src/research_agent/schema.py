from __future__ import annotations

from dataclasses import dataclass, fields
from datetime import datetime, timezone
from typing import Any

SOURCE_TYPES = frozenset({"web", "docs", "paper", "news", "dataset", "other"})
CONFIDENCE = frozenset({"high", "medium", "low"})
STAGES = frozenset({"extract", "verify"})

CSV_COLUMNS = (
    "id",
    "topic",
    "question",
    "finding",
    "evidence",
    "source_title",
    "source_url",
    "source_type",
    "published_date",
    "retrieved_at",
    "confidence",
    "tags",
    "notes",
    "stage",
    "brief_slug",
)


@dataclass(slots=True)
class Finding:
    id: str
    topic: str
    question: str
    finding: str
    evidence: str
    source_title: str
    source_url: str
    source_type: str
    published_date: str
    retrieved_at: str
    confidence: str
    tags: str
    notes: str
    stage: str
    brief_slug: str

    def to_row(self) -> dict[str, str]:
        return {name: getattr(self, name) for name in CSV_COLUMNS}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _require_str(record: dict[str, Any], key: str, index: int) -> str:
    value = record.get(key, "")
    if value is None:
        value = ""
    if not isinstance(value, str):
        raise ValueError(f"findings[{index}].{key} must be a string")
    return value.strip()


def _require_nonempty(record: dict[str, Any], key: str, index: int) -> str:
    value = _require_str(record, key, index)
    if not value:
        raise ValueError(f"findings[{index}].{key} is required")
    return value


def finding_from_dict(record: dict[str, Any], *, brief_slug: str, index: int) -> Finding:
    source_type = _require_nonempty(record, "source_type", index)
    if source_type not in SOURCE_TYPES:
        raise ValueError(
            f"findings[{index}].source_type must be one of {sorted(SOURCE_TYPES)}"
        )
    confidence = _require_nonempty(record, "confidence", index)
    if confidence not in CONFIDENCE:
        raise ValueError(
            f"findings[{index}].confidence must be one of {sorted(CONFIDENCE)}"
        )
    stage = _require_nonempty(record, "stage", index)
    if stage not in STAGES:
        raise ValueError(f"findings[{index}].stage must be one of {sorted(STAGES)}")

    tags = record.get("tags", [])
    if isinstance(tags, str):
        tag_text = tags.strip()
    elif isinstance(tags, list):
        parts = []
        for tag in tags:
            if not isinstance(tag, str) or not tag.strip():
                raise ValueError(f"findings[{index}].tags must be strings")
            parts.append(tag.strip())
        tag_text = ";".join(parts)
    else:
        raise ValueError(f"findings[{index}].tags must be a list or string")

    finding_id = _require_nonempty(record, "id", index)
    if not finding_id.startswith("F"):
        raise ValueError(f"findings[{index}].id must start with 'F'")

    return Finding(
        id=finding_id,
        topic=_require_nonempty(record, "topic", index),
        question=_require_nonempty(record, "question", index),
        finding=_require_nonempty(record, "finding", index),
        evidence=_require_nonempty(record, "evidence", index),
        source_title=_require_nonempty(record, "source_title", index),
        source_url=_require_nonempty(record, "source_url", index),
        source_type=source_type,
        published_date=_require_str(record, "published_date", index),
        retrieved_at=_require_nonempty(record, "retrieved_at", index),
        confidence=confidence,
        tags=tag_text,
        notes=_require_str(record, "notes", index),
        stage=stage,
        brief_slug=brief_slug,
    )


def parse_findings_file(payload: dict[str, Any]) -> list[Finding]:
    for key in ("brief_slug", "topic", "question", "generated_at", "findings"):
        if key not in payload:
            raise ValueError(f"Missing top-level key: {key}")
    brief_slug = payload["brief_slug"]
    if not isinstance(brief_slug, str) or not brief_slug.strip():
        raise ValueError("brief_slug must be a non-empty string")
    findings = payload["findings"]
    if not isinstance(findings, list):
        raise ValueError("findings must be a list")
    rows = []
    seen: set[str] = set()
    for index, record in enumerate(findings):
        if not isinstance(record, dict):
            raise ValueError(f"findings[{index}] must be an object")
        item = finding_from_dict(record, brief_slug=brief_slug.strip(), index=index)
        if item.id in seen:
            raise ValueError(f"Duplicate finding id: {item.id}")
        seen.add(item.id)
        rows.append(item)
    return rows


def unused_field_guard() -> tuple[str, ...]:
    names = tuple(f.name for f in fields(Finding))
    if names != CSV_COLUMNS:
        raise RuntimeError("Finding fields and CSV_COLUMNS are out of sync")
    return names
