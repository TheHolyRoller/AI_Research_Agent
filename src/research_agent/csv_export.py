from __future__ import annotations

import csv
from pathlib import Path

from research_agent.schema import CSV_COLUMNS, Finding


def write_csv(path: Path, findings: list[Finding]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        for item in findings:
            writer.writerow(item.to_row())
    return len(findings)
