# Features

This document keeps track of MVP features, explaining what each feature does and how to test it.

## Feature Template
Whenever a new feature is completed, document it here using the following format:

```text
## Feature Name

Status:
Purpose:
User Flow:
Technical Flow:
Related Endpoints:
Files/Modules:
How to Test:
Notes / Limitations:
```

## System Health Check (Laravel API)

Status: Complete
Purpose: Validates that the Laravel API is running and can serve frontend requests.
User Flow: N/A (System level)
Technical Flow: Nuxt (or Client) -> Nginx -> Laravel `GET /api/health` -> Returns JSON status.
Related Endpoints: `GET /api/health`
Files/Modules: `routes/api.php`
How to Test: Run `curl http://localhost:8080/api/health` and verify the `{"service": "ResumeFit Laravel API", "status": "running"}` response.

## System Health Check (FastAPI)

Status: Complete
Purpose: Validates that the FastAPI AI service is running and accessible to Laravel.
User Flow: N/A (System level)
Technical Flow: Laravel -> FastAPI `GET /` -> Returns JSON status.
Related Endpoints: `GET /`
Files/Modules: `ai-service/app/main.py`, `ai-service/app/schemas/health.py`
How to Test: Run `curl http://localhost:8000/` and verify the `{"service": "ResumeFit AI Service", "status": "running"}` response.

```