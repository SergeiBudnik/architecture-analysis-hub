---
title: Clearing & Settlement — ADR, Contracts, Tests
sidebar_position: 12
---

# Clearing, Settlement and Reconciliation — Architecture Decisions

**Author:** Sergei Budnik · **Educational supplement** to the [payment financial lifecycle](clearing-settlement-reconciliation.md).

## 1. Architecture decision records

| Decision | Proposed pattern | Reason / trade-off |
|---|---|---|
| CSR-ADR-01 | Independent lifecycle entities for auth, capture, clearing and payout | Extra references/joins, but avoids false “paid/settled” status |
| CSR-ADR-02 | Durable capture command with unique business key | Avoid double financial presentment when callers retry |
| CSR-ADR-03 | Treat provider file acknowledgement separately from item acceptance | File transport success ≠ accepted financial rows |
| CSR-ADR-04 | Store source report identity, checksum, row and revision | Auditable replay and correction |
| CSR-ADR-05 | Reconcile external scheme positions at aggregate level | Scheme netting is not one-to-one per purchase |
| CSR-ADR-06 | Append-only financial ledger with balanced postings | Evidence and controlled corrections |
| CSR-ADR-07 | Explicit cut-offs, time zones and value dates per provider | Avoid false positive “missing settlement” breaks |
| CSR-ADR-08 | Split scheme settlement from acquirer-to-merchant payout | Funding agreement, fees and reserves differ |
| CSR-ADR-09 | Exception queue with operator ownership, SLA and trail | Make unresolved money breaks actionable |
| CSR-ADR-10 | Route refunds/chargebacks as independent adjustment events | Original sale and capture history remains traceable |

## 2. Data contracts (generic)

### Clearing file / batch metadata

| Field | Example | Rule |
|---|---|---|
| batchId | batch-demo-17 | Unique in processor/channel scope |
| sourceProvider | demo-acquirer | Known authenticated origin |
| creationTime | 2026-10-17T17:00:00Z | UTC event time, record source zone/cut-off |
| settlementCurrency | GBP | Currency must be explicit |
| recordCount | 1 | Compare with parsed rows |
| controlTotalMinor | 10000 | Compare accepted gross entries, accounting for sign and adjustments |
| checksum | [sha256 digest] | Detect corruption and duplicate import |

### Clearing row (not a scheme format)

\`\`\`json
{
  "batchId": "batch-demo-17",
  "rowId": "row-001",
  "captureId": "CAP-301",
  "acquirerReference": "ACQ-401",
  "recordType": "SALE",
  "amountMinor": 10000,
  "currency": "GBP",
  "transactionDate": "2026-10-17"
}
\`\`\`

### Merchant funding (not a scheme format)

\`\`\`json
{
  "merchantId": "merchant-demo",
  "payoutId": "PAY-701",
  "currency": "GBP",
  "grossMinor": 10000,
  "feeMinor": 220,
  "adjustmentMinor": 0,
  "reserveMinor": 0,
  "netMinor": 9780,
  "valueDate": "2026-10-19"
}
\`\`\`

The dates are illustrative, not a promise of any T+N settlement schedule.

## 3. Financial invariants

\`\`\`text
Captured_total <= eligible_authorized_amount
  (unless explicit scheme/provider adjustments apply)

Expected_merchant_net = gross
  - fees + credits - debits - reserves
  (all in a declared currency and payout period)

Ledger_journal: sum(debits) = sum(credits)
  (per currency and accounting rules)

One authorized business event -> no duplicate financial side effect
  (despite duplicate messages and processing retries)
\`\`\`

Where partial/multiple capture is supported, define the precise capture balance and concurrency control.

## 4. Batch and retry safety

1. Receive / transmit a file with a stable **batch ID** and checksum.
2. Acknowledge **transport** separately from financial acceptance of each row.
3. Record each \`batchId + rowId + sourceProvider + revision\` and scoped financial key.
4. For partial acceptance, identify accepted and rejected rows; never replay an entire batch blindly.
5. Persist outbox/inbox records and use idempotent row posting.
6. Move unresolved differences into a case-management queue with immutable history.

## 5. Failure-injection test matrix

| Test | Injected fault | Expected control |
|---|---|---|
| CSR-T01 | Duplicate capture API request | One captured financial effect |
| CSR-T02 | Approved authorization, no capture | Not marked settled |
| CSR-T03 | Clearing upload acknowledged but 1 row rejected | Item-level mismatch detected |
| CSR-T04 | Clearing file delivered twice | Deduped by scoped batch/record identity |
| CSR-T05 | Settlement position missing after expected cut-off | Exception raised; not assumed zero |
| CSR-T06 | Scheme net position differs from processor report | Aggregate mismatch, treasury investigation |
| CSR-T07 | Payout report exists, bank credit missing | Merchant funding exception |
| CSR-T08 | Late chargeback for previously settled item | New linked financial adjustment, preserve original |
| CSR-T09 | Currency mismatch between capture and settlement | Explicit FX mapping or exception |
| CSR-T10 | File imported out of order | Deferred/partial matching, no fabricated matches |
| CSR-T11 | Ledger double-submit after worker restart | Unique business event key blocks duplicate posting |
| CSR-T12 | Correction after cutoff | Audited new correction/version, not destructive edit |

## 6. NFR review

- **Integrity:** durable source metadata, unique financial keys, balanced ledger, tamper-aware audit.
- **Availability:** separate online payment availability from nightly/batch clearing windows.
- **Recoverability:** precise checkpoints, files/row replay contracts and operator escalation.
- **Performance:** peak records per batch, import duration, matching SLA, file retention.
- **Security:** encryption at rest/in transit, least-privilege export/report access, masking.
- **Operations:** dashboards for unmatched counts, aged breaks, payout delays and cut-off progress.

## 7. Review gate

Before sign-off, obtain provider-specific presentment rules, settlement account arrangements, required scheme report definitions, value-date calendars, merchant fee schedules, dispute/refund lifecycle rules and accounting policy. Nothing in this example substitutes for actual network specifications.
