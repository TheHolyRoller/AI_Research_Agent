from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from research_agent.csv_export import write_csv
from research_agent.paths import BRIEF_TEMPLATE, BRIEFS_DIR, DEFAULT_CSV, DEFAULT_FINDINGS
from research_agent.prompts import PIPELINE_ORDER, load_stage, stitch
from research_agent.schema import parse_findings_file, unused_field_guard

SLUG_RE = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    slug = SLUG_RE.sub("-", text.lower()).strip("-")
    return slug or "research-brief"


def cmd_prompts(args: argparse.Namespace) -> int:
    if args.stage:
        text = load_stage(args.stage)
        sys.stdout.write(text if text.endswith("\n") else text + "\n")
        return 0
    sys.stdout.write(stitch(include_index=args.index))
    return 0


def cmd_init_brief(args: argparse.Namespace) -> int:
    unused_field_guard()
    topic = args.topic.strip()
    slug = args.slug.strip() if args.slug else slugify(topic)
    BRIEFS_DIR.mkdir(parents=True, exist_ok=True)
    dest = BRIEFS_DIR / f"{slug}.md"
    if dest.exists() and not args.force:
        print(f"Brief already exists: {dest}", file=sys.stderr)
        return 1
    template = BRIEF_TEMPLATE.read_text(encoding="utf-8")
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    filled = (
        template.replace("replace-me", slug)
        .replace("- topic:\n", f"- topic: {topic}\n")
        .replace("- created_at:\n", f"- created_at: {now}\n")
        .replace("## Core question\n", f"## Core question\n\n{topic}\n")
    )
    dest.write_text(filled, encoding="utf-8")
    print(dest)
    return 0


def cmd_export(args: argparse.Namespace) -> int:
    unused_field_guard()
    source = Path(args.input)
    dest = Path(args.output)
    if not source.exists():
        print(f"Missing findings file: {source}", file=sys.stderr)
        return 1
    payload = json.loads(source.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        print("Findings file must be a JSON object", file=sys.stderr)
        return 1
    try:
        findings = parse_findings_file(payload)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    count = write_csv(dest, findings)
    print(f"Wrote {count} row(s) to {dest}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="research-agent",
        description="Load research prompts and export findings to CSV.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    prompts_cmd = sub.add_parser("prompts", help="Print prompt files")
    prompts_cmd.add_argument(
        "--stage",
        choices=PIPELINE_ORDER,
        help="Print a single stage instead of the full chain",
    )
    prompts_cmd.add_argument(
        "--index",
        action="store_true",
        help="Include prompts/_index.md at the top of the stitched chain",
    )
    prompts_cmd.set_defaults(func=cmd_prompts)

    brief_cmd = sub.add_parser("init-brief", help="Create a brief from the template")
    brief_cmd.add_argument("--topic", required=True)
    brief_cmd.add_argument("--slug")
    brief_cmd.add_argument("--force", action="store_true")
    brief_cmd.set_defaults(func=cmd_init_brief)

    export_cmd = sub.add_parser("export", help="Write findings JSON to CSV")
    export_cmd.add_argument("--input", default=str(DEFAULT_FINDINGS))
    export_cmd.add_argument("--output", default=str(DEFAULT_CSV))
    export_cmd.set_defaults(func=cmd_export)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)
