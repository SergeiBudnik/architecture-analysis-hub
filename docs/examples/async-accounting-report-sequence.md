---
title: Sequence Example — Asynchronous Report Generation
sidebar_position: 11
---

# Sequence Diagram: Long-Running Accounting Report

**Source:** `SEQUENCE_EXAMPLES.docx`, Example №1, from Sergei Budnik's STORAGE library. This adaptation keeps the source's **report queue ID, 30-second polling and 10-minute limit**.

## 1. Scenario

An accountant initiates generation of a large report from a UI. The backend may need up to **10 minutes** to generate it. The UI begins generation using an endpoint equivalent to `/getReport`; it then sends `/checkReport` every **30 seconds**, correlated by `queueId`. If the report is not ready after ten minutes, the user sees an error.

The original exercise explicitly omits employee authorization and most exceptional conditions. The public edition follows that scope instead of pretending they were modeled in the source.

## 2. Participants

| Participant | Responsibility |
|---|---|
| Accountant | Requests report and receives output or timeout |
| `accounting-ui` | Starts asynchronous job and checks readiness |
| `accounting-report-service` | Queues/generates report, returns queueId and status |
| Report store (added in public illustration) | Holds generated artifact for retrieval |

## 3. Main sequence

1. Accountant clicks Generate Report.
2. `accounting-ui` → `accounting-report-service`: `/getReport`.
3. Report service returns a unique `queueId`.
4. UI requests `/checkReport?queueId=...` every **30 seconds**.
5. If ready within ten minutes, UI retrieves and opens/downloads the generated report.
6. If not ready within ten minutes, UI displays an error.

## 4. Editable source and diagram

[Download asynchronous report generation sequence (PlantUML)](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/storage-async-report-sequence.puml).

```mermaid
sequenceDiagram
    actor Accountant
    participant UI as accounting-ui
    participant Report as accounting-report-service
    Accountant->>UI: Generate report
    UI->>Report: /getReport
    Report-->>UI: queueId
    loop Every 30 sec; maximum 10 min
      UI->>Report: /checkReport(queueId)
      alt Ready
        Report-->>UI: READY + report reference
        UI-->>Accountant: Download report
      else Still processing
        Report-->>UI: PENDING
      end
    end
    opt Not ready by 10-minute deadline
      UI-->>Accountant: Report generation timed out
    end
```

**Architecture note (new):** This is a useful teaching example of asynchronous work and polling, not a benchmark. Real systems additionally require job retention, authorization, cancellation, retry, secure artifact access and timeouts for partial report generation.

**Licence:** [CC BY 4.0](../license.md).
