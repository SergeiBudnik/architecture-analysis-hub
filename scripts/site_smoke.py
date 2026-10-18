#!/usr/bin/env python3
"""Verify selected Docusaurus pages and public downloads after build."""
from pathlib import Path
import sys
build=Path(__file__).resolve().parents[1]/"build"
pages=["index","search","docs/intro","docs/downloads","docs/architecture/api-design-patterns","docs/architecture/bpmn-practical-faq","docs/templates/full-stack-srs-outline","docs/examples/source-examples-downloads","docs/library-versioning","docs/source-inventory"]
assets=["downloads/User_Stories_Template_Public.xlsx","editable/HLD_Request_Management_Public.docx","editable/food-delivery-process.bpmn","editable/payment-intents-reference-openapi.json"]
errors=[]
for name in pages:
    opts=[build/(name+".html"),build/name/"index.html"]
    if not any(p.is_file() for p in opts):errors.append("Missing page "+name)
for name in assets:
    if not (build/name).is_file():errors.append("Missing public asset "+name)
count=len(list(build.rglob("*.html")))
if count<35:errors.append("Too few HTML pages: "+str(count))
print("HTML pages:",count,"Checked routes:",len(pages),"Checked assets:",len(assets))
for err in errors:print("ERROR",err)
sys.exit(bool(errors))
