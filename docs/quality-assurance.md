---
title: Publication Quality Assurance — October 2026
sidebar_position: 12
---

# Public Library — Publication QA Report

**Review date:** 18 October 2026  
**Maintainer:** Sergei Budnik  
**Scope:** Published educational adaptations and downloadable files in `architecture-analysis-hub`  
**Outcome:** Automated structural/render/deployment checks **passed**. Minor typography/pagination and editor-specific visual caveats are identified below.

This report describes checks actually completed. Successful rendering or automated checks do not prove legal rights in third-party material, confidential-data absence, real-world architecture suitability, scheme certification, or third-party adoption.

## 1. Verification matrix

| Control | Coverage and actual method | Result |
|---|---|---|
| Source manifest | All **44** original STORAGE filenames versus 44 unique source-inventory table rows | PASS — original files are mapped to public adaptations, not republished wholesale |
| Documentation references | **484 links** examined by repository-local Markdown/link audit; broken local and self-hosted repository-file links fail CI | PASS in stage-6 scan; remote third-party sites not included |
| Public site | Docusaurus compile with broken-link failure enabled; generated key-route/asset smoke test; GitHub Pages deployment | PASS on previous successful deployment; latest deployment status must be checked from Actions |
| PlantUML | All **26** source files compiled to SVG using the PlantUML CLI; rendered galleries inspected | PASS; syntax errors corrected in several sequences |
| DOCX | **8** Word downloads converted to PDF with LibreOffice; **16 rendered pages** individually inspected | PASS with minor pagination observations |
| RTF | **21** Word-compatible downloads converted to PDF; **31 rendered pages** individually inspected | PASS |
| Draw.io | **4** public editable diagrams checked as XML, including pages, cell identifiers and edge references | PASS structural; native diagrams.net/editor rendering **not independently certified** |
| BPMN | **1** editable BPMN file checked for XML, diagram interchange and sequence-flow references | PASS structural; external BPMN editor rendering **not independently certified** |
| Spreadsheet | **1** native XLSX structurally checked for ZIP integrity and required workbook parts | PASS structural; Excel desktop appearance **not checked** |
| OpenAPI | **1** new JSON reference parsed and checked for baseline OpenAPI fields | PASS basic structure; full schema validation/provider certification **not claimed** |
| License | Main CC BY 4.0 notice and documentation license scope aligned to author-owned published editions | PASS scope clarification; third-party/client content excluded |
| Privacy | Automated scans for select key-shaped strings and internal addresses; Office package/comment review; review of new public prose | No flags in automated stage-6 review; **not** a comprehensive secret or copyright clearance |

## 2. Visual observations

Reviewed galleries of all **16 DOCX pages**, all **31 RTF pages** and all **26 PlantUML SVGs**.

The rendered text, tables and sequence flows were readable without visible clipping in these previews. Two downloadable Word examples have sparse final pages:

- **HLD_Request_Management_Public.docx** — the third page contains only the final “Linked editable diagrams” section. This is a cosmetic orphan-page layout issue, not missing content.
- **employee-bulk-update-api.docx** — the second page is lightly populated with concluding material. This is a low-severity formatting issue.

Several template RTFs are intentionally one-page compact worksheets rather than completed specifications. Detailed/source-derived RTF guides can span two or three pages.

The visual assessment is based on rendered preview images, not a guarantee of identical display in every installed Microsoft Word version, browser, BPMN editor or Draw.io editor.

## 3. Fixes applied during this QA cycle

- Repaired invalid `..>` arrows in three sequence diagrams (converted to valid sequence message arrows).
- Replaced unsupported `cloud` participant declarations in two sequences.
- Corrected unsupported sequence-note placement.
- Fixed an incorrect false-positive in Word tracked-change detection (table border XML tags are not revision markup).
- Added a standalone source-manifest, Markdown-link, Office, XML and privacy-pattern audit to GitHub Actions.
- Added compiled-page and public-download smoke checks to the Docusaurus deployment.
- Added separate PlantUML + DOCX + RTF render pipelines with downloadable QA preview artifacts.
- Clarified the scope of the public CC BY 4.0 notice for author-owned editable source editions.

## 4. Evidence and repeatability

- [Visual QA: 26 PlantUML, eight DOCX / 16 pages, 21 RTF / 31 pages](https://github.com/SergeiBudnik/architecture-analysis-hub/actions/runs/39145510289) — successful verification; download the preview artifact from the run page.
- [Previous successful Pages build and deployment](https://github.com/SergeiBudnik/architecture-analysis-hub/actions/runs/39139593101) — site compilation and publication.
- [Stage 6 structural audit source](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/scripts/quality_audit.py) and [public source manifest](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/scripts/source_storage_manifest.txt).
- [Pages publishing and smoke checks](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/.github/workflows/deploy.yml).
- [Visual QA workflow](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/.github/workflows/visual-qa.yml).

When updating this report after a later commit, verify the newest **successful** Actions run instead of assuming previous green runs cover newer files.

## 5. Remaining non-blocking checks

1. Open each Draw.io/BPMN diagram once in its native editor, save/export a visual preview and verify that labels, routing and swimlanes remain usable.
2. Optionally rebalance the two sparse last pages in DOCX files as a presentation polish task.
3. Manually inspect the public Excel workbook in Microsoft Excel or a compatible editor for font, sheet dimensions and printable layout.
4. Use a dedicated secrets/copyright review before importing **new** source documents; static regex/metadata checks alone cannot establish publication rights.
5. Validate external third-party URLs separately if a future release relies on them.

These items are explicitly disclosed rather than misrepresented as completed checks.

## 6. Sequence of next project stages

The next planned activity is **Stage 8: independent real-world usage, distribution and genuine feedback**. Only after collecting externally verifiable adoption or recognition should the project proceed to **Stage 7: assembling optional-criterion evidence**. No usage metrics or endorsements should be invented.

[44-file provenance inventory](source-inventory.md) · [Downloads](downloads.md) · [Release notes](release-notes.md) · [License](license.md).
