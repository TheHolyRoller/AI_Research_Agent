from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROMPTS_DIR = ROOT / "prompts"
TEMPLATES_DIR = ROOT / "templates"
DATA_DIR = ROOT / "data"
BRIEFS_DIR = DATA_DIR / "briefs"
RAW_DIR = DATA_DIR / "raw"
OUTPUT_DIR = DATA_DIR / "output"
DEFAULT_CSV = OUTPUT_DIR / "findings.csv"
DEFAULT_FINDINGS = RAW_DIR / "findings.json"
BRIEF_TEMPLATE = TEMPLATES_DIR / "research_brief.md"
