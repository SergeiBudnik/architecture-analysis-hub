#!/usr/bin/env python3
"""Prefer browser-downloadable native DOCX links throughout the documentation."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PAGES_BASE = "https://sergeibudnik.github.io/architecture-analysis-hub/"
GITHUB_RAW = "https://github.com/SergeiBudnik/architecture-analysis-hub/raw/refs/heads/main/static/"
matcher = re.compile(re.escape(GITHUB_RAW) + r"(downloads|editable)/([\w.-]+)\.(rtf|docx)")

count = 0
for file in list(DOCS.rglob("*.md")) + [ROOT / "README.md"]:
    old = file.read_text(encoding="utf-8")
    def replace(match):
        subdir, name, extension = match.groups()
        target = ROOT / "static" / subdir / (name + ".docx")
        if not target.is_file():
            raise RuntimeError(f"Broken DOCX target: {target}")
        return PAGES_BASE + subdir + "/" + name + ".docx"
    new, changed = matcher.subn(replace, old)
    if file == DOCS / "downloads.md":
        new = new.replace(
            "Eight **Word-compatible RTF** templates are available. These are sanitized, newly formatted adaptations of the author's original documentation structures, not copies of source documents.\n\nRTF files can be edited in Microsoft Word or LibreOffice and saved as DOCX.",
            "Eight **native Microsoft Word (DOCX)** templates are ready to download and edit. These are sanitized, newly formatted adaptations of the author's original documentation structures, not copies of source documents.\n\n**Click Download to save a Word document (.docx)**; open it in Microsoft Word or LibreOffice. The original RTF editions are still retained in the GitHub repository as optional source versions."
        )
        new = new.replace("Word-compatible RTF", "Microsoft Word DOCX").replace(
            "The eight published, sanitized RTF files", "The published, sanitized DOCX files"
        )
        new = new.replace("downloadable CSV with original ten columns and sorting example; native XLSX edition prepared separately.",
            "downloadable native XLSX and CSV editions with the original ten columns and sorting example.")
    if file == DOCS / "templates/catalogue.md":
        new = new.replace(
            "**Want an editable Word-compatible file?** Start with [eight downloadable RTF templates](../downloads.md). These open in Word or LibreOffice and can be saved as DOCX.",
            "**Want an editable Word file?** Start with [eight downloadable DOCX templates](../downloads.md). These open directly in Microsoft Word or LibreOffice."
        ).replace("editable RTF", "editable DOCX").replace("new RTF templates", "new DOCX templates").replace(
            "**12 public materials** are available in web-readable form. Original Word, Excel, BPMN, draw.io and Visio downloads remain under individual review; they are **not yet published**.",
            "Public web-readable templates, worked examples and reviewed native DOCX/XLSX/Draw.io/BPMN downloads are available. The unreviewed private source originals remain unpublished."
        ).replace("User Stories editable spreadsheet (CSV)", "User Stories editable spreadsheet (XLSX and CSV)")
    if file == DOCS / "examples/source-examples-downloads.md":
        new = new.replace(
            "These source-grounded examples are available as public Markdown pages **and downloadable Word-compatible RTF editions** (editable in Microsoft Word and convertible to DOCX). The original private Word files are not published.",
            "These source-grounded examples are available as public Markdown pages **and native editable DOCX downloads**. The original private Word files are not published."
        ).replace(
            "These RTF versions are separate, editable **sanitized public editions**.",
            "These Word documents are separate, editable **sanitized public editions**."
        ).replace("Editable RTF", "Download DOCX").replace("· [RTF]", "· [DOCX]").replace("| [RTF]", "| [DOCX]")
    if file == DOCS / "intro.md":
        new = new.replace("Word-compatible RTF", "Word DOCX")
    if new != old:
        file.write_text(new, encoding="utf-8")
        count += changed
        print("Repaired Word links:", file.relative_to(ROOT), "direct links:", changed)
print("Native DOCX links repaired:", count)
if count < 20:
    raise RuntimeError(f"Too few Word links repaired ({count}); check downloads index and original URLs")
