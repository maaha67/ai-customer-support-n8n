# Export review — 6 October 2026

## Review scope

Reviewed all four supplied JSON exports, their node parameters, connections, sticky notes and embedded JavaScript. This is an export inspection and isolated fixture validation, not a new live integration run.

## Checks completed

- CSR-01 | Support Ticket Processing: unique names, connection targets and expression references verified.
- CSR-02 | Support Response Approval: unique names, connection targets and expression references verified.
- CSR-03 | Execute Support Responses: unique names, connection targets and expression references verified.
- CSR-04 | Support Follow-up Queue 1: unique names, connection targets and expression references verified.
- 19 fixture assertions passed; all exported Code node bodies compiled.

CSR-01's HTTP and LLM request error outputs are connected to error logging and return to the ticket loop. Invalid classification, draft, missing order and policy branches are present. CSR-02 rejection cancels the action. CSR-03 checks approval, draft, execution status and Gmail message ID; sends the Action_Log draft; records Gmail success; and has a separate send-error branch. CSR-04 appends or updates by ticket_id and copies current statuses when deactivating a case.

## Changes in the generalized copies

- Removed personal Gmail recipients, spreadsheet identifiers and cached URLs, credential bindings, instance/workflow metadata and node webhook IDs.
- Replaced the CSR-02 subworkflow identifier with a configuration placeholder.
- Kept all imports inactive and pinData empty.
- Added the missing CSR-01 overview and Maha author attribution to each workflow overview.
- Removed stray trailing Markdown heading markers from CSR-01 notes.
- Removed the extra "1" from the CSR-04 workflow name.
- Retained operational connections, validation code, mappings and existing note positions/sizes. Readability at your canvas zoom still needs visual confirmation.

## Remaining limitations

- Sheets and approval-request transport failures lack comprehensive error recovery.
- No atomic ticket claim or send claim; overlapping runs can create duplicate actions or sends.
- The action ID changes by execution, so repeated processing of the same NEW ticket is not intrinsically idempotent.
- The sender skips unready/missing tickets without logging a reason.
- Approval results are checked as a boolean, with no separate malformed-result or expiration branch.
- The saved draft is editable after approval; approval does not bind a version/hash.
- Draft validation checks structure and matching IDs/actions, not factual accuracy of every sentence.
- Eligibility windows are hardcoded and can diverge from edited policy text.
- Queue lookup has Always Output Data off in the supplied export. A missing entry produces no downstream item; it remains absent, which matches this branch's intended no-op behavior.
- Deleted support tickets do not automatically deactivate queue entries.
- Human follow-up work and revision/resubmission remain manual.
- No live import or external-service test of these generalized copies has been performed.

## Next verification

After selecting credentials, spreadsheet tabs, available models, recipients and the imported CSR-02 workflow, test one approved response, one rejection, one no-approval response and one queue deactivate/reactivate cycle in the configured copy. Check Gmail Sent and Action_Log before any retry.

## Supplied Python API

Added the original main.py without changing its handler logic. It contains synthetic example.com addresses and Maha attribution. Python syntax and six isolated handler checks passed (health, three orders, normalization, 404). FastAPI was stubbed for this review; no live HTTP integration test was run. Added dependency declaration, Windows startup instructions and a .gitignore.
