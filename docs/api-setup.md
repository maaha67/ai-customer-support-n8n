# Local order API setup

Author: Maha

The supplied FastAPI app provides three synthetic orders. Its response format matches CSR-01's Verify Order Match node. It has no authentication and is intended for local synthetic demonstrations.

## Windows Command Prompt

Open Command Prompt inside this project's api folder, then run:

```bat
py -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Keep that terminal running while testing n8n. Binding to 0.0.0.0 allows access from the existing Docker setup; network access also depends on the host firewall. Keep the API limited to the demo environment.

If you are continuing with your existing customer-support-api installation, keep using its working environment and startup command. You do not need to create another environment just to use these project files.

## Check endpoints in your browser

- http://localhost:8000/health should return status ok and demo true.
- http://localhost:8000/orders/ORD-1001 should return found true, demo true and an order object.
- http://localhost:8000/orders/ORD-9999 should return HTTP 404 with detail Order not found.

CSR-01 running in Docker uses host.docker.internal rather than localhost to reach the Windows host. Order IDs are trimmed and uppercased by the API.

## Data and dependencies

Orders live in main.py and do not synchronize with Google Sheets. All customer emails use example.com. requirements.txt declares fastapi[standard] without pinning an unverified version. Record the versions from your working virtual environment for reproducible deployment.

## Review validation

Python syntax parsed successfully. Six isolated checks covered health, all three orders, ID normalization and unknown-order 404 behavior. FastAPI was substituted with a minimal route-registration/exception stub for these checks because it was not installed in the review environment. These checks verify handler logic, not HTTP transport or dependency compatibility. Live endpoints were previously tested by the project author; retest the configured copy locally.
