---
title: Worked Example — Payment Reconciliation
sidebar_position: 11
---

# Worked Example: Reconcile Capture, Clearing and Merchant Payout

**Author:** Sergei Budnik  
**Scenario:** One synthetic GBP card payment with a simple fictitious merchant fee. No real merchant, bank, account or scheme data is included.

## 1. Source data and arithmetic

| Record source | Reference | Amount | Meaning |
|---|---|---:|---|
| Gateway authorization | AUTH-201 | GBP 100.00 | Authorization approved |
| Merchant capture | CAP-301 | GBP 100.00 | Capture submitted once |
| Acquirer clearing | CLR-501 | GBP 100.00 | Captured purchase presented |
| Merchant fee report | FEE-501 | GBP 2.20 | Fictional contractual fees |
| Acquirer funding report | PAY-701 | GBP 97.80 | Merchant net payout |
| Merchant bank statement | BANK-701 | GBP 97.80 | Funds received |

### Compute merchant payout

```text
Gross captured amount   = 10,000 pence
Illustrative total fees  =    220 pence
Other adjustments        =      0 pence
Reserve / withholding    =      0 pence
Expected merchant payout =  9,780 pence = GBP 97.80
```

Formula:

```text
Expected payout =
  sum(eligible gross captures)
  - sum(contractual fees)
  + sum(positive adjustments)
  - sum(refunds/chargebacks/reserves/other deductions as applicable)
```

**This is a merchant-funding calculation only.** It is **not** a computation of the card scheme's interbank net settlement, interchange obligations or the issuer's ledger entries. The fee amount and assumptions are invented solely for illustration.

## 2. Match workflow

1. **Validate** import file metadata, currency, merchant, report period, checksum and row uniqueness.
2. **Match AUTH-201 → CAP-301** under capture/authorization amount and eligibility rules.
3. **Match CAP-301 → CLR-501** by acquirer reference and amount, accounting for accepted report granularity.
4. **Build merchant funding group** for a payout period and merchant; sum captures and adjustments.
5. **Calculate expected net** from item totals and fees.
6. **Match PAY-701** in the acquirer report to expected GBP 97.80.
7. **Match BANK-701** to the actual bank statement, value date and account.
8. **Mark reconciled** only after required evidence is present; otherwise create an exception with owner and investigation trail.

## 3. Exception example: payout short by GBP 0.50

Assume the processor report says merchant payout = **GBP 97.80**, while the bank statement shows **GBP 97.30** under the same reference:

```text
Processor payout:  +GBP 97.80
Bank receipt:      +GBP 97.30
Unexplained break:  GBP  0.50
```

Do **not** automatically invent a missing fee or overwrite the original capture. Open an exception such as:

```json
{
  "exceptionId": "REC-DEMO-801",
  "type": "PAYOUT_AMOUNT_MISMATCH",
  "merchantId": "merchant-demo",
  "payoutId": "PAY-701",
  "currency": "GBP",
  "expectedMinor": 9780,
  "receivedMinor": 9730,
  "differenceMinor": 50,
  "status": "OPEN",
  "possibleCauses": ["bank charge", "timing", "report adjustment"],
  "ownerTeam": "Finance Operations"
}
```

The listed possible causes are **investigation hypotheses**, not asserted causes.

## 4. Double-entry ledger illustration

For teaching purposes only, a platform may use journals to maintain consistency between expected receivables and liabilities. Example entries below **assume gross acquiring funding into the platform** and intentionally omit real interchange/network netting, revenue-recognition rules and taxes.

| Event | Debit | Credit | Amount |
|---|---|---|---:|
| Recognize eligible clearing receivable | Clearing receivable | Merchant payable | GBP 100.00 |
| Allocate contractual merchant fees | Merchant payable | Fees payable/revenue* | GBP 2.20 |
| Receive gross acquiring funds | Settlement cash | Clearing receivable | GBP 100.00 |
| Pay merchant | Merchant payable | Settlement cash | GBP 97.80 |

*Actual fees might be revenue, pass-through liabilities or expenses under the specific contract and accounting policy. The table is a **simplified balanced-journal teaching model**, not a universal settlement ledger.*

Controls: no orphan ledger posting, immutable audit, unique business-event posting key, explicit currency and rounding, financial review for repairs.

## 5. Common breaks and operational owner

| Exception | Detection | Recommended owner |
|---|---|---|
| Capture has no presentment by expected cut-off | Capture present in gateway, missing acquirer row | Processing operations |
| Clearing item has no captured source | Unmatched clearing reference | Acquirer integration / fraud review |
| Duplicate financial row | Same scoped financial key reported twice | Reconciliation / processor operations |
| Settlement position totals disagree | File/batch totals vs scheme report | Treasury / finance operations |
| Merchant report net mismatch | Gross – fees – adjustments != net | Merchant finance |
| Payout missing on bank statement | Net payout report exists, no bank credit | Treasury / bank operations |
| Chargeback or refund not linked | Adjustment without original transaction link | Dispute/financial operations |

## 6. Verification tests

- Repeat the same clearing file: no second ledger effect (file and row-level idempotency).
- Import a file with a missing row: detect and isolate the difference.
- Process the same payout report twice: do not initiate a second payout.
- Shift settlement value date without changing transaction date: match per documented date tolerance.
- Receive a correction after the period closes: create audited adjustment, do not silently rewrite history.
- Break the external-report upload: flag **missing evidence**, not successful settlement.

**Related:** [Lifecycle reference](clearing-settlement-reconciliation.md) · [ADR and controls](clearing-design-decisions.md).
