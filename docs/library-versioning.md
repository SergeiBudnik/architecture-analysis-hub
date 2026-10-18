---
title: Library Document Versioning
sidebar_position: 10
---

# Versioning Policy — Public Edition

**Source:** `VERSIONING_POLICY.docx`, STORAGE v1.0.0 (last updated 27 September 2025). The core rules below are preserved from the original; GitHub implementation guidance is a new addition.

| Component | Meaning in source | Example |
|---|---|---|
| X — major | New structure / significant changes | v1.0.0 → v2.0.0 |
| Y — minor | New artifact introduced | v1.0.0 → v1.1.0 |
| Z — patch | Typo or formatting change | v1.1.0 → v1.1.1 |

**Original three rules:** Update *Last updated*; record changes in release notes; never overwrite a published artifact without incrementing its version.

**Original examples:** v1.0.0 initial release; v1.1.0 new SRS template; v1.1.1 BRD typo correction.

## New implementation guidance for this public repository

1. Use Git commits for immutable change tracking and link major updates to [Release Notes](release-notes.md).
2. Distinguish **content versions** from the Docusaurus site's own build version.
3. Record deprecations or renamed templates clearly so links and third-party citations remain usable.
4. Preserve the public document's provenance and note changes in adapted or translated copies per [CC BY 4.0](license.md).
5. Do not claim all source-file artifacts have been published verbatim: the public library contains selectively sanitized teaching editions.

[How to Use](library-how-to-use.md) · [Source Inventory](source-inventory.md).
