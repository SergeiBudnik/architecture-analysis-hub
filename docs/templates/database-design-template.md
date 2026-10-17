---
title: Database Design Template
---

# Database Design Template

*Adapted from Sergei Budnik's authored source library, `DATABASE_DESIGN_TEMPLATE.docx` (v1.0.0, September 2025). This is a public Markdown adaptation; placeholder fields and technical example values are illustrative.*

## Data requirements
Describe new tables and relationships. Link to any pre-existing tables used by the solution.

## Table definition
**Table / service:** [Name]  
**Purpose:** [Why it exists]  
**Existing related tables:** [Names and references]

| Business name | DB field | Data type | Mandatory | Key | Description |
|---|---|---|---|---|---|
| Identifier | id | int | Yes | PK | Unique record identifier |
| Code | code | varchar(64) | Yes | Unique | Business code |
| Display name | name | varchar(255) | No | — | Human-readable label |

## Relationships
| From | To | Cardinality | FK / association |
|---|---|---|---|
| [Entity A] | [Entity B] | 1:N / N:M | [Column or link table] |

## Integrity and change controls
- Define nullability and uniqueness explicitly.
- State expected referential integrity behavior.
- Describe defaults, migration, index and data retention decisions if relevant.
- Include the ER diagram or a link to it.
