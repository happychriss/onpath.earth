"""Owner-approved homepage; secondary-page copy stays in the existing content modules."""
from pathlib import Path
ROOT = Path(__file__).resolve().parent
def home(lang="de"):
    if lang not in {"de", "en"}:
        raise ValueError("Unsupported language")
    return (ROOT / f"home_{lang}.html").read_text()
