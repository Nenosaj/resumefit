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