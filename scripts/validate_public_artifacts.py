#!/usr/bin/env python3
"""Validate public editable artifacts using Python standard library only."""
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile, BadZipFile
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EDITABLE = ROOT / "static" / "editable"
errors = []

def invalid(file, reason):
    errors.append(f"{file.relative_to(ROOT)}: {reason}")

def test_drawio(p):
    try:
        root = ET.parse(p).getroot()
        if root.tag != "mxfile":
            invalid(p, "expected mxfile")
        diagrams = root.findall("diagram")
        if not diagrams:
            invalid(p, "no editable diagram pages")
        for diagram in diagrams:
            if diagram.find("mxGraphModel/root") is None:
                invalid(p, f"page {diagram.get('name')} missing graph root")
                continue
            cells = diagram.findall(".//mxCell")
            ids = [c.get("id") for c in cells]
            idset = set(ids)
            if len(ids) != len(idset):
                invalid(p, f"duplicate cell ID in {diagram.get('name')}")
            for c in cells:
                if c.get("edge") == "1" and (c.get("source") not in idset or c.get("target") not in idset):
                    invalid(p, f"edge has unknown endpoint in {diagram.get('name')}")
    except Exception as exc:
        invalid(p, f"invalid Draw.io XML: {exc}")

def test_bpmn(p):
    try:
        root = ET.parse(p).getroot()
        ns = {"b": "http://www.omg.org/spec/BPMN/20100524/MODEL",
              "d": "http://www.omg.org/spec/BPMN/20100524/DI"}
        all_ids = {n.get("id") for n in root.iter() if n.get("id")}
        if root.find(".//d:BPMNDiagram", ns) is None:
            invalid(p, "no BPMN diagram interchange section")
        flows = root.findall(".//b:sequenceFlow", ns)
        if not flows:
            invalid(p, "no sequence flows")
        for f in flows:
            if f.get("sourceRef") not in all_ids or f.get("targetRef") not in all_ids:
                invalid(p, f"unresolved sequence flow {f.get('id')}")
    except Exception as exc:
        invalid(p, f"invalid BPMN XML: {exc}")

def test_docx(p):
    try:
        with ZipFile(p) as z:
            bad = z.testzip()
            if bad:
                invalid(p, f"invalid zip member {bad}")
            required = ["[Content_Types].xml", "_rels/.rels",
                        "word/document.xml", "word/styles.xml"]
            if any(x not in z.namelist() for x in required):
                invalid(p, "missing required Word document parts")
            for x in required:
                if x.endswith(".xml") or x.endswith(".rels"):
                    ET.fromstring(z.read(x))
            document = z.read("word/document.xml").decode("utf-8")
            if "Personal use by subscriber; no redistribution" in document:
                invalid(p, "outdated subscriber license text in public document")
    except (BadZipFile, Exception) as exc:
        invalid(p, f"invalid DOCX: {exc}")

def test_rtf(p):
    s = p.read_text(encoding="utf-8")
    depth = 0
    for i, ch in enumerate(s):
        if ch == "{" and (i == 0 or s[i - 1] != "\\"):
            depth += 1
        if ch == "}" and (i == 0 or s[i - 1] != "\\"):
            depth -= 1
        if depth < 0:
            invalid(p, "unbalanced RTF braces")
            break
    if depth or not s.startswith("{\\rtf1"):
        invalid(p, "invalid RTF header or unbalanced groups")

def test_xlsx(p):
    try:
        with ZipFile(p) as z:
            if z.testzip():
                invalid(p, "corrupted ZIP member")
            members = set(z.namelist())
            required = {"[Content_Types].xml", "xl/workbook.xml"}
            if not required.issubset(members):
                invalid(p, "missing required XLSX workbook parts")
            if not any(n.startswith("xl/worksheets/sheet") and n.endswith(".xml") for n in members):
                invalid(p, "missing XLSX worksheet")
            if any(n.startswith("xl/externalLinks/") for n in members):
                invalid(p, "external workbook links must be removed from public files")
            for n in ["xl/workbook.xml", "xl/sharedStrings.xml"]:
                if n in members:
                    data = z.read(n)
                    ET.fromstring(data)
                    if b"Personal use by subscriber; no redistribution" in data:
                        invalid(p, "old subscriber-use notice is still present")
    except Exception as exc:
        invalid(p, f"invalid XLSX: {exc}")

for file in EDITABLE.rglob("*"):
    if not file.is_file():
        continue
    ext = file.suffix.lower()
    if ext == ".drawio":
        test_drawio(file)
    elif ext == ".bpmn":
        test_bpmn(file)
    elif ext == ".docx":
        test_docx(file)
    elif ext == ".rtf":
        test_rtf(file)

DOWNLOADS = ROOT / "static" / "downloads"
for file in DOWNLOADS.glob("*.xlsx"):
    test_xlsx(file)

print("Checked editable Word, diagram, BPMN and XLSX download files")
if errors:
    for e in errors:
        print("ERROR", e, file=sys.stderr)
    sys.exit(1)
print("All public editable artifacts passed structural validation.")
