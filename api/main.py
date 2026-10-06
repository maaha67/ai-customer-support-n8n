from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Customer Support Order API",
    description="Synthetic order data for Maha's automation portfolio.",
    version="1.0.0",
)

# Demo records matching the Google Sheets Orders tab.
# Changes in Google Sheets do not automatically update these records.
ORDERS = {
    "ORD-1001": {
        "order_id": "ORD-1001",
        "customer_email": "customer@example.com",
        "product_name": "Everyday Backpack",
        "quantity": 1,
        "order_total": 59.00,
        "currency": "USD",
        "order_status": "Delivered",
        "order_date": "2026-09-23",
        "expected_delivery_date": "2026-09-28",
        "delivered_date": "2026-09-28",
        "tracking_number": "DEMO-TRACK-001",
    },
    "ORD-1002": {
        "order_id": "ORD-1002",
        "customer_email": "customer2@example.com",
        "product_name": "Travel Organizer",
        "quantity": 2,
        "order_total": 38.00,
        "currency": "USD",
        "order_status": "In Transit",
        "order_date": "2026-09-20",
        "expected_delivery_date": "2026-09-27",
        "delivered_date": None,
        "tracking_number": "DEMO-TRACK-002",
    },
    "ORD-1003": {
        "order_id": "ORD-1003",
        "customer_email": "customer3@example.com",
        "product_name": "Desk Lamp",
        "quantity": 1,
        "order_total": 45.00,
        "currency": "USD",
        "order_status": "Delivered",
        "order_date": "2026-09-18",
        "expected_delivery_date": "2026-09-23",
        "delivered_date": "2026-09-23",
        "tracking_number": "DEMO-TRACK-003",
    },
}


@app.get("/health")
def health():
    return {"status": "ok", "demo": True}


@app.get("/orders/{order_id}")
def get_order(order_id: str):
    normalized_id = order_id.strip().upper()
    order = ORDERS.get(normalized_id)

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )

    return {"found": True, "demo": True, "order": order}