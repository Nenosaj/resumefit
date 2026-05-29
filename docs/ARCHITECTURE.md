# Architecture

This document outlines the initial service architecture for ResumeFit.

## Core Flow

```text
Nuxt Frontend
    ↓
Laravel API
    ↓
PostgreSQL Database
    ↓
FastAPI AI Service
    ↓
Gemini API
```

**Supporting Services**: Redis for caching/queues, and local storage for MVP files.

The backend services (Laravel API, PostgreSQL, FastAPI AI Service, Redis) are orchestrated using Docker Compose within the `laravel-backend/` directory.

## Service Responsibilities

- **Laravel API**: Acts as the core backend orchestrator. It manages the PostgreSQL database via Eloquent, handles API requests from the Nuxt frontend, persists data, queues jobs via Redis, and acts as the client communicating with the FastAPI AI Service for LLM operations.
- **FastAPI AI Service**: An isolated Python microservice built with FastAPI. It provides endpoints for AI parsing, data extraction, and handles direct communication with the Gemini API using strict Pydantic schema validation.
- **PostgreSQL**: Stores the structured master resume data, job posts, fit scores, applications, and resume versions.
- **Redis**: Handles Laravel's cache and queue workers.

## CI Validation Flow

GitHub Actions runs a lightweight Continuous Integration (CI) pipeline on pushes and pull requests to `main`.

1. **Checkout**: Retrieves the repository.
2. **Setup**: Prepares `.env` files with placeholder secrets.
3. **Build & Start**: Uses Docker Compose to build and start the backend stack.
4. **Validate**: Runs Laravel migrations, generates app keys, lists routes, and tests health endpoints (`http://localhost:8000/` for FastAPI and `http://localhost:8080/api/health` for Laravel) via `curl`.
5. **Teardown**: Stops and removes Docker containers.

This pipeline ensures that changes do not break the basic dockerized backend setup. Continuous Deployment (CD) will be integrated once a target deployment environment is selected.