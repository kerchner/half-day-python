#!/usr/bin/env python3
"""Create the student ("fill-in") versions of the workshop notebooks.

Reads each instructor notebook in `jupyter notebooks/` (the "filled out"
versions), keeps every markdown cell as-is, and empties every code cell
(source and outputs) so that learners type the code themselves during the
workshop.  Output goes to `notebooks/`, with `_filled out` stripped from the
filename and `_student` appended.

Usage:  python3 scripts/make_student_notebooks.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "notebooks"
OUT_DIR = ROOT / "notebooks"


def blank_code_cells(nb: dict) -> dict:
    for cell in nb["cells"]:
        if cell["cell_type"] == "code":
            cell["source"] = []
            cell["outputs"] = []
            cell["execution_count"] = None
            # drop Colab-specific per-cell execution metadata
            cell["metadata"] = {}
    return nb


def student_name(path: Path) -> str:
    stem = re.sub(r"[ _-]*filled[ _-]*out", "", path.stem, flags=re.I)
    return f"{stem}.ipynb"


def main() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    for src in sorted(SRC_DIR.glob("*.ipynb")):
        nb = json.loads(src.read_text(encoding="utf-8"))
        nb = blank_code_cells(nb)
        dest = OUT_DIR / student_name(src)
        dest.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n",
                        encoding="utf-8")
        n_code = sum(c["cell_type"] == "code" for c in nb["cells"])
        print(f"{src.name} -> {dest.relative_to(ROOT)}  ({n_code} code cells blanked)")


if __name__ == "__main__":
    main()
