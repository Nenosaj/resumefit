# Tech Stack

This document tracks the core technologies used in ResumeFit and the reasons they were chosen.

## Main Stack

- **Frontend**: Nuxt + Vue + TypeScript + Tailwind CSS
- **Backend API**: Laravel
- **AI/Data Service**: Python + FastAPI (with Pydantic for validation, python-dotenv for config, and Uvicorn)
- **LLM Provider**: Gemini API
- **Database**: PostgreSQL
- **Queue/Cache**: Redis
- **Deployment**: Docker Compose first
- **Storage**: Local storage first

The Laravel framework is configured as the central API backend, communicating with PostgreSQL, Redis, and the Python microservice.

Docker Compose is used to define and run the multi-container Docker application for the backend, ensuring consistent development environments.