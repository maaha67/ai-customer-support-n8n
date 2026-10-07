# AI Customer Support & Order Resolution System

**Author: Maha**  
AI automation and product focused roles

An n8n portfolio demo that validates support tickets, checks synthetic order data, drafts policy-guided replies, collects human approval, sends eligible responses, and maintains a support follow-up queue.

## Workflows

| Workflow | Purpose | Trigger |
|---|---|---|
| CSR-01 | Ticket validation, classification, order/policy checks, drafting and action logging | Manual |
| CSR-02 | Reviewer approval or rejection | Called by CSR-01 |
| CSR-03 | Response eligibility checks, Gmail sending and execution logging | Manual |
| CSR-04 | Active/inactive follow-up queue refresh | Manual |

Uses n8n, Google Sheets, Gmail, OpenAI chat models and a local Python order API. Sticky notes explain each workflow and its branches.

## What this demo demonstrates

- Structured AI output validation and routing of invalid outputs.
- Order ID and email consistency checks before using order data.
- One active matching policy, with missing or duplicate policy handling.
- Human approval for sensitive or uncertain responses.
- Sending the saved Action_Log draft rather than regenerating it.
- Gmail message ID recording and checks that reduce repeated sequential sends.
- Updating existing follow-up cases by ticket ID.

It sends responses and tracks proposed actions. It does not execute refunds, replacements, returns or delivery investigations.

## Setup

1. Import the four JSON files into n8n. Imports are inactive and contain no credential bindings.
2. Connect your Google Sheets, Gmail and OpenAI credentials. Select chat models available to your account for both LLM nodes in CSR-01.
3. Create the spreadsheet tabs with the exact headers in `docs/sheet-schema.md`.
4. In every Google Sheets node, replace `YOUR_GOOGLE_SHEET_ID` and select the corresponding tab. Verify mappings after selection. Keep ticket_id and action_id unique.
5. Import/configure CSR-02 first. In CSR-01's Request Support Response Approval node, select that imported workflow in place of `YOUR_CSR02_WORKFLOW_ID` and verify the seven input mappings. Keep waiting for subworkflow completion off.
6. Configure CSR-02's reviewer address in place of `reviewer@example.com`. Configure CSR-03's fixed test inbox in place of `test-inbox@example.com`. Keep synthetic tests going to your own inbox.
7. Configure a reachable public n8n URL for approval callbacks. Publish/enable CSR-02 as required by your n8n instance. Keep Gmail authorization valid.
8. Start your demo order API on port 8000. CSR-01 uses `http://host.docker.internal:8000/orders/` plus the encoded order ID, appropriate to the existing Windows Docker setup. Adjust the host for other environments. The supplied API source is included in `api/main.py`; see `docs/api-setup.md`.
9. Use synthetic data and run CSR-01 manually. Respond to reviewer emails when required, then run CSR-03. Run CSR-04 to refresh the queue. Avoid overlapping executions.
10. Filter Followup_Queue to queue_status Active for the operational view. Retain inactive entries.

The API must return `{ "found": true, "order": { ... } }` for a found order; its order fields are listed in the schema. Unknown orders in the existing demo return HTTP 404.

## Demo rules

Damaged items use a 7-day window from delivery; returns use a 30-day window. Both require further evidence. A late order must be in transit with its expected date passed. Eligibility uses the ticket creation date. These windows are hardcoded in Check Policy Eligibility and must be kept consistent with Store_Policies text.

## Validation and limits

See `docs/review.md` for the export review and isolated fixture checks. Earlier manual end-to-end tests were reported during development; the generalized imports need a fresh test after configuration. No live n8n, Gmail or Sheets execution was performed during this export review.

This is a portfolio demo. Google Sheets updates are not atomic; concurrent runs can race. Sheet failures and approval dispatch failures may stop execution without recording a ticket error. Actions stuck In Progress and ambiguous email failures need manual reconciliation against Gmail Sent. The follow-up queue does not send follow-ups, revise drafts or reconcile deleted tickets. Email matching is not customer authentication.
## Workflow Screenshots

### CSR-01 — Support Ticket Processing
Validates tickets, classifies requests, verifies orders, checks policies, and drafts responses.

![Support Ticket Processing](<Images/CSR-01  Support Ticket Processing.png>)
### CSR-02 — Support Response Approval
Requests human approval and records approved or rejected responses.

![Support Response Approval](<Images/CSR-02  Support Response Approval.png>)

### CSR-03 — Execute Support Responses
Checks approval and ticket readiness, sends responses, and records results.

![Execute Support Responses](<Images/CSR-03  Execute Support Responses.png>)

### CSR-04 — Support Follow-up Queue
Maintains active cases needing attention and marks existing entries inactive when attention is no longer required.

![Support Follow-up Queue](<Images/CSR-04  Support Follow-up Queue 1.png>)
![Manual Test Results](<Images/Test Results.PNG>)
