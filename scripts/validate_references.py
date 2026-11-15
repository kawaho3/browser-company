#!/usr/bin/env python3
"""Offline structural validation for the M0 browser research index.

This verifies inventory shape, not external repository availability, licenses,
or successful builds. It performs no network requests.
"""

from pathlib import Path
import argparse
import re
import sys

REPO_ENTRY = re.compile(r"(?m)^(\d{2})\.\s+([^\n]+)\n\s+URL:\s+(https://github\.com/[^\s/]+/[^\s/]+)\s*$")
REQUIRED_DOCUMENTS = (
    "AGENTS.md", "README.md", "CONTRIBUTING.md", "SECURITY.md",
    "docs/VISION.md", "docs/ARCHITECTURE.md", "docs/DECISIONS.md",
    "docs/FEATURE_MATRIX.md", "docs/ROADMAP.md", "docs/BACKLOG.md",
    "docs/BUILD_AND_COST.md", "docs/REUSE_CATALOG.md",
    "docs/SECURITY_AND_PRIVACY.md", "docs/LEGAL_AND_BRANDING.md",
    "docs/ONBOARDING.md",
)


def check(root: Path) -> list[str]:
    problems: list[str] = []
    for name in REQUIRED_DOCUMENTS:
        if not (root / name).is_file():
            problems.append(f"Missing required document: {name}")
    index = root / "REPOSITORIES_TO_STUDY.txt"
    if not index.is_file():
        return problems + ["Missing REPOSITORIES_TO_STUDY.txt"]
    entries = REPO_ENTRY.findall(index.read_text(encoding="utf-8"))
    numbers = [int(number) for number, _, _ in entries]
    if numbers != list(range(1, 19)):
        problems.append(f"Expected sequential entries 01..18; found {numbers!r}")
    urls = [url.rstrip("/").lower() for _, _, url in entries]
    if len(urls) != len(set(urls)):
        problems.append("Duplicate repository URLs in study list")
    required = {"https://github.com/brave/brave-core", "https://github.com/chromium/chromium"}
    if not required.issubset(set(urls)):
        problems.append("The two foundation candidates must both be listed")
    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    problems = check(args.root)
    for problem in problems:
        print(f"ERROR: {problem}", file=sys.stderr)
    if problems:
        return 1
    print("M0 reference structure OK: 18 unique repositories and required documents present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
