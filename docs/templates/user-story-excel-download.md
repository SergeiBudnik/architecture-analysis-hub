---
title: User Story Excel Template — Editable Sheet
sidebar_position: 18
---

# User Stories: Source-Based Spreadsheet Template

This template is adapted from Sergei Budnik's original `USER_STORY_TEMPLATE.xlsx` (STORAGE v1.0.0, September 2025). The public edition preserves the **ten original planning fields** and the illustrative product-catalog sorting story.

**[Download spreadsheet as CSV — opens in Excel](https://github.com/SergeiBudnik/architecture-analysis-hub/raw/refs/heads/main/static/downloads/User_Stories_Template_Public.csv)**

The CSV is an immediately reusable, platform-neutral table. A styled native XLSX edition with dropdowns is prepared separately; unlike CSV, XLSX can retain validation and formatting. The original source workbook with old subscriber-use notice and embedded metadata has not been uploaded.

## Original spreadsheet columns

| Column | Intended content |
|---|---|
| User Story ID | Unique story identifier |
| Epic Name | Product capability or epic |
| Name | Short story title |
| Story | As a user, I want ..., so that ... |
| Acceptance Criteria | Specific, testable acceptance conditions |
| Priority | 1/2/3 or MVP/Backlog |
| Comments | Analyst questions and decisions |
| Linked UCs | Related use case references |
| Linked task in jira/conf | Project work item URL |
| Status | Implemented, In testing, Cancelled, Planned etc. |

## Example retained from the source

An example catalog story asks for sorting products by price, age/newness and rating, with the current sort selection shown in the UI. The public copy keeps the business intent but consolidates the acceptance text to avoid misleading duplicates and to improve readability.

## Recommended completion check

- Does each story deliver specific actor value?
- Can a tester unambiguously verify its acceptance criteria?
- Is the epic and related use case reference correct?
- Are priorities and statuses mutually agreed?
- Are links public-safe before sharing a completed sheet?

This public adaptation is shared under [CC BY 4.0](../license.md). The spreadsheet is **not evidence of third-party usage or adoption**.
