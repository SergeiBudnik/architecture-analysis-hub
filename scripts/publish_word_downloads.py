#!/usr/bin/env python3
"""Build DOCX downloads from already-public sanitized RTF editions.

The original private STORAGE archive is never used. Native existing DOCX files
are left untouched. Eight baseline templates receive actual editable Word tables.
"""
from __future__ import annotations
import os
import re
import shutil
import subprocess
import tempfile
import zipfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOWNLOADS = ROOT / "static" / "downloads"
EDITABLE = ROOT / "static" / "editable"
BASE_TEMPLATES = {
    "API_Specification_Template",
    "BRD_Template",
    "Backend_SRS_Template",
    "Database_Design_Template",
    "Event_Driven_Integration_Template",
    "Frontend_SRS_Template",
    "HLD_Template",
    "SRS_Template",
}
EXPECTED_RTF_COUNT = 21

def main():
    rtf_sources = sorted(DOWNLOADS.glob("*.rtf")) + sorted(EDITABLE.glob("*.rtf"))
    if len(rtf_sources) != EXPECTED_RTF_COUNT:
        raise RuntimeError(f"Expected {EXPECTED_RTF_COUNT} public RTF sources; found {len(rtf_sources)}")
    pending = [p for p in rtf_sources if not p.with_suffix(".docx").exists()]
    print(f"Public RTF documents: {len(rtf_sources)}; new DOCX needed: {len(pending)}")

    if pending:
        with tempfile.TemporaryDirectory(prefix="hub-word-conversion-") as temp:
            out = Path(temp) / "output"
            out.mkdir()
            profile = (Path(temp) / "office-profile").as_uri()
            command = [
                "libreoffice",
                f"-env:UserInstallation={profile}",
                "--headless",
                "--convert-to",
                "docx:Office Open XML Text",
                "--outdir",
                str(out),
                *map(str, pending),
            ]
            result = subprocess.run(command, check=False, text=True, capture_output=True, timeout=240)
            print(result.stdout)
            if result.returncode:
                raise RuntimeError(f"LibreOffice failed:\n{result.stderr}")
            for source in pending:
                converted = out / source.with_suffix(".docx").name
                if not converted.is_file():
                    raise RuntimeError(f"Conversion missing: {source.name}; {result.stderr}")
                shutil.copy2(converted, source.with_suffix(".docx"))

    for stem in sorted(BASE_TEMPLATES):
        destination = DOWNLOADS / (stem + ".docx")
        improve_template(destination)

    # Full structural and content check for every public counterpart.
    original_count = Counter()
    for source in rtf_sources:
        docx = source.with_suffix(".docx")
        if not docx.is_file():
            raise RuntimeError(f"Missing native Word version: {docx}")
        validate_word(docx)
        original_count[docx.parent.name] += 1

    print("Validated native DOCX for every published Word resource:", dict(original_count))

def improve_template(file: Path):
    from docx import Document
    from docx.shared import Cm, Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn

    document = Document(file)
    sections = document.sections
    for sect in sections:
        sect.top_margin = Cm(1.7)
        sect.bottom_margin = Cm(1.7)
        sect.left_margin = Cm(1.9)
        sect.right_margin = Cm(1.9)
    normal = document.styles["Normal"]
    normal.font.name = "Aptos"
    normal.font.size = Pt(9.5)
    normal.paragraph_format.space_after = Pt(5)

    paragraphs = list(document.paragraphs)
    title_set = False
    for p in paragraphs:
        text = p.text.strip()
        if not text:
            continue
        if not title_set:
            p.style = document.styles["Title"]
            p.paragraph_format.space_after = Pt(9)
            for run in p.runs:
                run.font.name = "Aptos Display"
                run.font.size = Pt(17)
                run.font.bold = True
                run.font.color.rgb = RGBColor(10, 57, 80)
            title_set = True
            continue
        if text == "Document control" or re.match(r"^\d+\.\s+\S", text):
            p.style = document.styles["Heading 1"]
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(5)
            for run in p.runs:
                run.font.name = "Aptos"
                run.font.size = Pt(11)
                run.font.color.rgb = RGBColor(10, 57, 80)
            continue
        for run in p.runs:
            run.font.name = "Aptos"
            if run.font.size and run.font.size.pt > 12:
                run.font.size = Pt(9.5)
        if " | " not in text:
            continue
        columns = [s.strip() for s in text.split(" | ")]
        if len(columns) < 2:
            continue
        table = document.add_table(rows=1, cols=len(columns))
        table.style = "Table Grid"
        table.autofit = True
        for col, value in enumerate(columns):
            cell = table.cell(0, col)
            cell.text = value
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            for par in cell.paragraphs:
                par.paragraph_format.space_after = Pt(2)
                for run in par.runs:
                    run.font.name = "Aptos"
                    run.font.size = Pt(8)
                    if col == 0:
                        run.font.bold = True
            if col == 0:
                tcPr = cell._tc.get_or_add_tcPr()
                shade = OxmlElement("w:shd")
                shade.set(qn("w:fill"), "E7F0F4")
                tcPr.append(shade)
        # Position the native table precisely where the pipe-delimited source was.
        p._p.addnext(table._tbl)
        p._element.getparent().remove(p._element)

    document.core_properties.title = document.paragraphs[0].text
    document.core_properties.author = "Sergei Budnik"
    document.core_properties.last_modified_by = "Architecture & Analysis Hub"
    document.core_properties.comments = "Sanitized educational Word template. CC BY 4.0."
    document.save(file)

def validate_word(file: Path):
    from docx import Document
    with zipfile.ZipFile(file) as z:
        corrupt = z.testzip()
        if corrupt:
            raise RuntimeError(f"Corrupted DOCX: {file}: {corrupt}")
        mandatory = {"[Content_Types].xml", "word/document.xml", "word/styles.xml"}
        if not mandatory.issubset(z.namelist()):
            raise RuntimeError(f"Missing DOCX parts: {file}")
        content = z.read("word/document.xml")
        if b"Personal use by subscriber" in content:
            raise RuntimeError(f"Old use restriction in document: {file}")
    doc = Document(file)
    if not any(p.text.strip() for p in doc.paragraphs) and not doc.tables:
        raise RuntimeError(f"Word document unexpectedly empty: {file}")
    if file.stem in BASE_TEMPLATES:
        if len(doc.tables) == 0:
            raise RuntimeError(f"Template has no native Word table: {file.name}")

if __name__ == "__main__":
    main()
