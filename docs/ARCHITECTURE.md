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