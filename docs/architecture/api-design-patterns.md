---
title: REST API Design — Practical Review Guide
sidebar_position: 2
---
# REST API Design: Problems, Solutions and Review Questions

**Source:** Sergei Budnik's authored `API_PARAMETERIZATION.docx` (v1.0.0, 2025-09-04). This page is a concise web adaptation, not a full reproduction.

## 1. Design the API as a contract

An API is a contract used by other developers. Predictability, security, performance and usability should be considered at the start, not patched into individual endpoints later.

## 2. Resource naming vs verb naming

| Style | Illustrative path | Advantages | Risks |
|---|---|---|---|
| Resource-oriented | `GET /users/{id}` | Consistent with HTTP and common tooling | Complex commands may not map cleanly to CRUD |
| Action-oriented | `POST /users/{id}/activate` | Explicit command semantics | Proliferation of ad-hoc actions |
| Mixed, deliberate | `GET /users/{id}` and `POST /users/{id}/activate` | Practical balance | Requires written conventions |

Avoid inconsistent paths such as `/getUsers`, `/addNewPost`, and `/user/12-3/updateEmail` unless an existing contract must be maintained.

## 3. Parameter design review

| Concern | Question |
|---|---|
| Naming | Are fields and paths consistent across endpoints? |
| HTTP semantics | Do methods reflect safe and idempotent behavior correctly? |
| Pagination | Are limits, cursors and sorting clearly documented? |
| Validation | Are mandatory fields, types and ranges explicit? |
| Error response | Can consumers distinguish business rejection, validation error and technical failure? |
| Versioning | Can existing consumers survive incremental change? |
| Security | Are permissions and field-level exposure modeled? |
| Idempotency | Can a consumer safely recover from an uncertain outcome? |

## 4. Example request contract

```http
POST /payment-intents
Idempotency-Key: 48f17955-88b9-4c13-8152-2669dbefc3de
Content-Type: application/json
```

```json
{
  "merchantOrderId": "order-101",
  "amountMinor": 1500,
  "currency": "EUR"
}
```

This request is an **independently constructed teaching example**, not a source-system endpoint. Actual amount and currency rules depend on the system.

## 5. Related resources

[Integration specification template](../templates/integration-specification.md), [Employee export API worked example](../examples/employee-export-api.md), and [Payment idempotency reference](../payments/state-machine.md).

For implementation, publish an OpenAPI contract with precise schema, authentication, error codes and examples.