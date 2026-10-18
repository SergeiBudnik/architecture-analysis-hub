---
title: API Example — Employee Bulk Update
sidebar_position: 12
---

# API Contract Example: Partial Bulk Update of Employees

**Source:** `API_EXAMPLE.docx` from STORAGE, second operation `PATCH /api/employees/bulk-update`. The existing [Employee Export API](employee-export-api.md) covers the first operation from the same source. The original sample contains example employee names, document details, contacts, salary information and token-shaped strings; this public edition uses **synthetic records only**.

## 1. Business behavior from the source

Users edit employee fields in a table, then select **Actions → Save All**. The GUI collects changed employee rows and sends a single request containing only fields that have changed. The operation accepts one or many employees and returns a required `updated` field even if no rows succeed. The `errors` field is present in partial-failure scenarios.

The source specifies **client-side validation** for completeness, type and format before submission. **Public design correction:** the server must also validate permissions and data; client-only validation is insufficient.

## 2. HTTP contract

```http
PATCH /api/employees/bulk-update
Authorization: Bearer <access_token>
Content-Type: application/json
```

Synthetic request:

```json
{
  "employees": [
    {"id": "EMP-101", "department": "Operations"},
    {"id": "EMP-102", "workPhone": "+0000000000"}
  ]
}
```

The `employees` collection field is a **public illustrative schema**. It is not claimed to match the original's field naming exactly.

## 3. Response contract

Illustrative success:

```json
{
  "updated": ["EMP-101", "EMP-102"]
}
```

Illustrative partial error:

```json
{
  "updated": ["EMP-101"],
  "errors": [
    {"employeeId": "EMP-102", "code": "VALIDATION_ERROR", "field": "workPhone"}
  ]
}
```

The source describes mandatory `updated` and conditional `errors`; the **precise error JSON shown here is newly designed** to illustrate the semantics.

## 4. Processing and failure rules

| Condition | Expected contract |
|---|---|
| One or more valid changes | Update identified rows and return `updated` |
| Field omitted | Do not overwrite unchanged field |
| Invalid type/format | Reject affected row with correlated error |
| No modified rows | `updated` must still appear |
| Unauthorized employee | Do not disclose or update record |
| Concurrent edits | Define version or optimistic-lock conflict response |
| Retry after unknown response | Define idempotency/concurrency to prevent repeated non-idempotent effects |

**Source vs recommendations:** Partial updates, multi-row processing, front-side validation and response fields are from the original. Concurrency policy, server-side validation, idempotency and audit requirements are explicit additional recommendations for reuse.

## 5. Editability and attribution

Editable DOCX versions are collected on the [Source-Based Examples Downloads page](source-examples-downloads.md). Related reference: [Backend SRS template](../templates/backend-srs-template.md).

**Licence:** [CC BY 4.0](../license.md).
