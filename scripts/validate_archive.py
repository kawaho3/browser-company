#!/usr/bin/env python3
"""Validate browser-company continuity archive, without external dependencies."""
from pathlib import Path
from zipfile import ZipFile, BadZipFile
import xml.etree.ElementTree as ET
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / "docs/PROJECT_MASTER_HANDOFF_2026-11-16.docx"
REQUIRED_FILES = (
    "START_HERE_NEXT_SESSION.md",
    "docs/PROJECT_MASTER_HANDOFF_2026-11-16.md",
    "docs/CHAT_AND_DECISION_LOG_2026-11-16.md",
    "docs/archive/ORIGINAL_BROWSER_MASTER_PROMPT_2026-11.md",
    "docs/archive/HISTORICAL_LAUNCH_PLAN_2026-11-12_TEXT.md",
)
REQUIRED_PARTS = {
    "[Content_Types].xml",
    "_rels/.rels",
    "word/document.xml",
    "word/styles.xml",
    "word/_rels/document.xml.rels",
    "docProps/core.xml",
}


def main() -> int:
    for name in REQUIRED_FILES:
        if not (ROOT / name).is_file():
            print("MISSING SOURCE:", name, file=sys.stderr)
            return 1
    original = (ROOT / REQUIRED_FILES[3]).read_text(encoding="utf-8")
    if "MASTER PROMPT" not in original or len(original.splitlines()) < 500:
        print("Original prompt archive looks incomplete", file=sys.stderr)
        return 1
    try:
        with ZipFile(DOCX) as zf:
            if not REQUIRED_PARTS.issubset(set(zf.namelist())):
                print("DOCX has missing OpenXML parts", file=sys.stderr)
                return 1
            invalid = zf.testzip()
            if invalid is not None:
                print("DOCX CRC failed:", invalid, file=sys.stderr)
                return 1
            for path in zf.namelist():
                if path.endswith(".xml") or path.endswith(".rels"):
                    ET.fromstring(zf.read(path))
            document = ET.fromstring(zf.read("word/document.xml"))
            ns = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
            text = " ".join((t.text or "") for t in document.iter(ns + "t"))
            checks = (
                "Brave Core", "Chromium", "REPOSITORIES_TO_STUDY",
                "Windows", "MASTER PROMPT", "HISTORICAL",
                "PROJECT MASTER RESEARCH", "80.4", "74.4",
            )
            missing = [term for term in checks if term not in text]
            if missing:
                print("DOCX missing required material:", missing, file=sys.stderr)
                return 1
            print("DOCX OK:",
                  len(text), "visible text chars,",
                  sum(1 for _ in document.iter(ns + "tbl")), "tables,",
                  sum(1 for _ in document.iter(ns + "hyperlink")), "hyperlinks")
    except (BadZipFile, OSError, ET.ParseError) as exc:
        print("DOCX validation failed:", exc, file=sys.stderr)
        return 1
    print("Continuity archive validated: source Markdown, original prompt and OOXML package")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
