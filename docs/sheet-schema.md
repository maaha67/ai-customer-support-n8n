# Spreadsheet schema

Use these exact tab names and column headers. These are schemas, not exported live spreadsheet data.

## Support_Tickets
```text
ticket_id,created_at,customer_email,order_id,customer_message,category,priority,processing_status,draft_response,policy_id,needs_approval,resolution_status,error_message
```
New tickets use processing_status NEW. Leave missing order IDs truly blank, not the text "Leave empty". Use ISO dates and valid email syntax.

## Action_Log
```text
action_id,ticket_id,order_id,created_at,category,policy_id,proposed_action,draft_response,requires_approval,approval_status,reviewer_notes,approved_at,execution_status,executed_at,error_message,gmail_message_id
```
Keep draft_response unchanged after approval. The sender uses the current saved Action_Log draft; no hash/version binding enforces immutability.

## Store_Policies
```text
policy_id,category,policy_title,policy_text,requires_approval,active
```
Allowed categories: DAMAGED_ITEM, LATE_DELIVERY, RETURN_REQUEST, PRODUCT_QUESTION, OTHER. Boolean cells must parse as true or false. Use one active policy per category.

## Orders / API order object
```text
order_id,customer_email,product_name,quantity,order_total,currency,order_status,order_date,expected_delivery_date,delivered_date,tracking_number
```
The current demo API uses its own order data; editing an Orders sheet does not synchronize the API.

## Followup_Queue
```text
ticket_id,order_id,category,priority,processing_status,resolution_status,customer_message,error_message,last_refreshed_at,queue_status
```
Queue status is Active or Inactive.

## Test_Results
```text
test_id,ticket_id,scenario,expected_result,actual_result,result
```
Keep development test evidence separate from newly configured import tests.
