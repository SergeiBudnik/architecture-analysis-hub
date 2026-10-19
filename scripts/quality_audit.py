#!/usr/bin/env python3
"""Portable public library QA: local links, archive coverage, editable formats."""
import json,re,sys,zipfile
from pathlib import Path
from urllib.parse import urlsplit,unquote
from xml.etree import ElementTree as ET
from collections import Counter
R=Path(__file__).resolve().parents[1];D=R/"docs";S=R/"static"
errors=[];warnings=[];counts=Counter()
def error(where,reason):errors.append(str(where)+": "+str(reason))
def xml(raw,where):
    try:return ET.fromstring(raw)
    except ET.ParseError as ex:error(where,"invalid XML "+str(ex));return None

manifest=(R/"scripts/source_storage_manifest.txt").read_text().splitlines()
inventory=(D/"source-inventory.md").read_text()
entries=re.findall(r"(?m)^\|\s*\x60([^\x60]+)\x60\s*\|",inventory)
if len(manifest)!=44 or len(set(manifest))!=44 or len(entries)!=44 or set(manifest)!=set(entries):
    error("source-inventory.md","44-file manifest mismatch "+str(set(manifest)^set(entries)))
counts["source_files"]=len(manifest)

for f in D.rglob("*.md"):
    data=re.sub(r"(?ms)^\x60{3}.*?^\x60{3}[^\n]*$","",f.read_text())
    links=re.findall(r"!?\[[^\]\n]*\]\(([^)\n]+)\)",data)
    links+=re.findall(r"<img[^>]*src=['\"]([^'\"]+)",data)
    for url in links:
        raw=url.strip().split(" ",1)[0].strip("<>")
        if raw.startswith(("#","mailto:","tel:","data:")):continue
        counts["links"]+=1
        parts=urlsplit(raw);p=unquote(parts.path)
        if raw.startswith("https://github.com/SergeiBudnik/architecture-analysis-hub/"):
            target=None
            for mark in ("/blob/main/","/raw/refs/heads/main/"):
                if mark in p:target=R/p.split(mark,1)[1]
            if target is not None and not target.is_file():
                error(f.relative_to(R),"missing repo asset "+url)
            continue
        if parts.scheme or raw.startswith("//"):continue
        if p.startswith("/architecture-analysis-hub/"): dest=S/p[len("/architecture-analysis-hub/"):]
        elif p.startswith("/docs/"):dest=D/p[len("/docs/"):]
        elif p in ("/","/search"):continue
        elif p.startswith("/"):error(f.relative_to(R),"unexpected absolute URL "+url);continue
        else:dest=f.parent/p
        if not (dest.is_file() or dest.with_suffix(".md").is_file() or (dest/"index.md").is_file()):
            error(f.relative_to(R),"broken reference "+url)

for p in S.rglob("*"):
    if not p.is_file():continue
    ext=p.suffix.lower();counts[ext]+=1
    try:
        if ext in (".docx",".xlsx"):
            with zipfile.ZipFile(p) as z:
                bad=z.testzip()
                if bad:error(p.relative_to(R),"bad ZIP member "+bad)
                names=set(z.namelist())
                needed={"[Content_Types].xml","word/document.xml","word/styles.xml"} if ext==".docx" else {"[Content_Types].xml","xl/workbook.xml"}
                if not needed.issubset(names):error(p.relative_to(R),"missing Office member")
                if ext==".xlsx" and not any(x.startswith("xl/worksheets/sheet") and x.endswith(".xml") for x in names):
                    error(p.relative_to(R),"no spreadsheet tabs")
                for entry in names:
                    if entry.endswith((".xml",".rels")):
                        content=z.read(entry)
                        xml(content,str(p.relative_to(R))+":"+entry)
                        if b"Personal use by subscriber" in content:
                            error(p.relative_to(R),"unlicensed private notice")
                        if ext==".docx" and re.search(rb"<w:(ins|del|commentReference)(?=[\s>/])",content):
                            error(p.relative_to(R),"tracked changes/comment markup")
                if any(x.startswith(("xl/externalLinks/","word/embeddings/")) for x in names):
                    error(p.relative_to(R),"embedded/external data")
                custom={x for x in names if x.startswith("customXml/")}
                if custom:
                    # The python-docx standard blank document has one empty
                    # Microsoft bibliography item. Whitelist only this exact
                    # harmless shape, never third-party/custom embedded data.
                    allowed={"customXml/item1.xml","customXml/itemProps1.xml","customXml/_rels/item1.xml.rels"}
                    data=z.read("customXml/item1.xml") if "customXml/item1.xml" in names else b""
                    safe=(custom==allowed and b'officeDocument/2006/bibliography' in data
                          and not re.search(rb'<b:Source(?=[\s>/])',data))
                    if not safe:
                        error(p.relative_to(R),"unreviewed custom XML data")
                if any(re.search(r"(comments|people)\d*\.xml$",x) for x in names):
                    error(p.relative_to(R),"review metadata")
        elif ext==".drawio":
            root=xml(p.read_bytes(),p.relative_to(R))
            if root is None:continue
            if root.tag!="mxfile":error(p.relative_to(R),"invalid drawio root")
            for page in root.findall("diagram"):
                model=page.find("mxGraphModel/root")
                if model is None:error(p.relative_to(R),"empty drawing page");continue
                cells=model.findall("mxCell");ids={c.get("id") for c in cells}
                for c in cells:
                    if c.get("edge")=="1" and (c.get("source") not in ids or c.get("target") not in ids):
                        error(p.relative_to(R),"edge without connected endpoint")
        elif ext==".bpmn":
            root=xml(p.read_bytes(),p.relative_to(R))
            if root is None:continue
            ns={"b":"http://www.omg.org/spec/BPMN/20100524/MODEL","di":"http://www.omg.org/spec/BPMN/20100524/DI"}
            ids={n.get("id") for n in root.iter()}
            if root.find(".//di:BPMNDiagram",ns) is None:error(p.relative_to(R),"no BPMN diagram")
            for flow in root.findall(".//b:sequenceFlow",ns):
                if flow.get("sourceRef") not in ids or flow.get("targetRef") not in ids:
                    error(p.relative_to(R),"invalid BPMN flow reference")
        elif ext==".rtf":
            txt=p.read_text()
            if not txt.startswith("{\\rtf1"):error(p.relative_to(R),"invalid RTF header")
            if "Personal use by subscriber" in txt:error(p.relative_to(R),"private notice")
            depth=0
            for part in re.findall(r"(?<!\\)[{}]",txt):
                depth+=1 if part=="{" else -1
                if depth<0:error(p.relative_to(R),"unbalanced RTF");break
            if depth:error(p.relative_to(R),"unbalanced RTF")
        elif ext==".svg":
            root=xml(p.read_bytes(),p.relative_to(R))
            if root is not None and not root.tag.endswith("svg"):error(p.relative_to(R),"invalid SVG")
        elif ext==".json":
            x=json.loads(p.read_text())
            if "openapi" in x and not all(y in x for y in ("info","paths","components")):
                error(p.relative_to(R),"invalid OpenAPI skeleton")
    except (OSError,zipfile.BadZipFile,json.JSONDecodeError,UnicodeError) as ex:
        error(p.relative_to(R),str(ex))

for p in (R/"diagrams").glob("*.puml"):
    txt=p.read_text();counts["puml"]+=1
    if txt.count("@startuml")!=1 or txt.count("@enduml")!=1:error(p.relative_to(R),"bad PlantUML markers")

for p in list(D.rglob("*.md"))+list((R/"diagrams").glob("*.puml"))+list(S.rglob("*.rtf")):
    t=p.read_text(errors="replace")
    if re.search(r"AKIA[0-9A-Z]{16}\b",t):warnings.append(str(p.relative_to(R))+": AWS key-shaped data")
    if re.search(r"\b192\.168\.\d{1,3}\.\d{1,3}\b",t):warnings.append(str(p.relative_to(R))+": private network address")
    if re.search(r"(?i)[\w.+-]+@(?!example\.invalid)(?!example\.com)[\w.-]+\.[a-z]{2,}",t):
        warnings.append(str(p.relative_to(R))+": email contact to review")

report={"passed":not errors,"counts":dict(counts),"errors":errors,"warnings":warnings}
(R/"reports").mkdir(exist_ok=True)
(R/"reports/quality_audit.json").write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps(report,indent=2))
sys.exit(bool(errors))
