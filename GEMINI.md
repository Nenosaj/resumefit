# GEMINI.md — ResumeFit Agent Instructions

## Role

You are the coding agent for **ResumeFit**, an AI-assisted job matching and resume tailoring system.

Your job is to help build the project one small, reviewable task at a time. You must follow `SPEC.md` as the source of truth and `TASKS.md` as the execution checklist.

## Read Order

Before making changes, read these files in order:

1. `GEMINI.md` — agent behavior, workflow, and boundaries
2. `SPEC.md` — product, architecture, and technical specification
3. `TASKS.md` — current implementation tasks and progress

If these files conflict, follow this priority:

1. User's latest explicit instruction
2. `GEMINI.md` boundaries
3. `SPEC.md`
4. `TASKS.md`
5. Existing code patterns

## Project Summary

ResumeFit helps Jason T. Daohog apply to jobs more strategically by:

- storing a structured master resume database
- accepting pasted job descriptions
- extracting job requirements
- calculating a realistic Fit Score
- recommending relevant projects
- generating tailored resume content
- tracking applications and follow-ups

Do not describe the score as a guaranteed interview chance. Use terms like **Fit Score**, **Interview Potential Score**, **Strong Match**, **Moderate Match**, **Low Match**, **Apply Now**, **Tailor First**, or **Skip / Save for Later**.

## Current Folder Structure

The intended root structure is:

```text
resumefit/
├── GEMINI.md
├── SPEC.md
├── TASKS.md
├── nuxt-frontend/
└── laravel-backend/
```

Important: the folder name `nuxt-frotend/` is intentionally written this way because the user requested it. Do not rename it unless the user explicitly asks.

Docker-related files must live inside:

```text
laravel-backend/
```

The backend folder may contain Laravel, Docker Compose, PostgreSQL, Redis, and the FastAPI AI service.

## Main Stack

Use this stack unless the user changes it:

```text
Frontend: Nuxt + Vue + TypeScript + Tailwind CSS
Backend API: Laravel
AI/Data Service: Python + FastAPI
LLM Provider: Gemini API
Database: PostgreSQL
Vector Search: pgvector later, not required in MVP
Queue/Cache: Redis
Automation: n8n later
Deployment: Docker Compose first
Storage: local storage first
```

## Development Workflow

Use a spec-driven workflow:

1. **Specify** — clarify or update `SPEC.md`.
2. **Plan** — identify the smallest useful task from `TASKS.md`.
3. **Implement** — make focused code changes only for that task.
4. **Validate** — run relevant tests or commands.
5. **Update** — mark progress in `TASKS.md` and update `SPEC.md` if the design changed.

Do not jump into large implementation work without checking the current task.

## Shell Command Policy

The agent must not run shell commands directly.

When validation is needed, the agent should:
1. Finish the file changes.
2. Provide exact commands for the user to run manually.
3. Explain the expected output.
4. Ask the user to paste any errors or logs if validation fails.

This applies to Docker, Git, Composer, npm, Laravel Artisan, database migrations, tests, curl, and all other terminal commands.

## Dynamic Documentation Rules

Keep the docs alive. Documentation is part of the definition of done, not an optional cleanup step.

Core documentation files:

```text
SPEC.md                  # source of truth for product scope, architecture, API contracts, data models
TASKS.md                 # implementation checklist and progress tracking
docs/ARCHITECTURE.md     # explains the system architecture and service responsibilities
docs/TECH_STACK.md       # explains technologies used and why they were chosen
docs/FEATURES.md         # explains completed and planned features in user-friendly language
docs/DECISIONS.md        # records important technical/product decisions and tradeoffs
```

When adding or changing a feature:

- Update `docs/FEATURES.md` with what the feature does, how it works, and how to test it.
- Update `SPEC.md` if the feature changes product scope, API contracts, data models, or architecture.
- Update `TASKS.md` after completing or discovering tasks.
- Update `README.md` when setup, commands, demo flow, or developer onboarding changes.

When changing architecture:

- Update `docs/ARCHITECTURE.md`.
- Update the Architecture section in `SPEC.md`.
- Explain the reason for the change and any tradeoffs.

When changing the tech stack:

- Update `docs/TECH_STACK.md`.
- Update the Tech Stack section in `SPEC.md`.
- Ask the user first if the change replaces Laravel, Nuxt, FastAPI, PostgreSQL, Gemini, Docker, or Redis.

When making an important decision:

- Add an entry to `docs/DECISIONS.md` with the decision, context, alternatives considered, and reason.
- Keep decision entries short and practical.

Documentation quality rules:

- Write for future Jason and portfolio reviewers.
- Explain why a feature exists, not just what files changed.
- Include commands or endpoint examples when useful.
- Keep docs factual; do not claim features are complete until they are validated.
- Do not rewrite the entire spec unless the user asks.

## Three-Tier Boundaries

### ✅ Always Do

- Keep the project MVP-first.
- Prefer small, focused commits or code changes.
- Keep Docker configuration inside `laravel-backend/`.
- Use PostgreSQL as the main database.
- Use local storage first.
- Use `.env.example` for environment variables.
- Never put real API keys in committed files.
- Validate AI output before trusting it.
- Return structured JSON from AI service endpoints.
- Keep generated resume claims honest and based on master resume data.
- Keep the first build focused on manual job description analysis.
- Update `TASKS.md` when work is completed.
- Update feature, architecture, tech stack, or decision docs when the task changes them.

### ⚠️ Ask First

Ask the user before doing any of these:

- Renaming `nuxt-frotend/` to `nuxt-frontend/`.
- Changing the main stack.
- Adding new major dependencies.
- Adding paid services.
- Adding AWS services.
- Introducing job board scraping.
- Building PDF export before the analyzer MVP works.
- Changing database schema after migrations already exist.
- Deleting files, migrations, or generated code.
- Replacing Laravel, Nuxt, FastAPI, PostgreSQL, or Gemini.
- Adding authentication if the current task does not require it.
- Making large refactors unrelated to the current task.

### 🛑 Never Do

- Never commit or expose `GEMINI_API_KEY`, database passwords, or secrets.
- Never invent Jason's experience, projects, skills, education, or employment history.
- Never claim guaranteed interviews, guaranteed callbacks, or recruiter responses.
- Never build automatic job scraping as the first version.
- Never start with PDF generation as the first version.
- Never depend on AWS unless the user explicitly asks.
- Never edit `vendor/`, `node_modules/`, generated lockfiles, or Docker volumes unless required by the task.
- Never remove tests to make a build pass.
- Never ignore failed tests or failed Docker commands.
- Never run shell commands automatically.
- Never ask the user for shell access or permission to run shell commands.
- Never execute Docker, Git, Composer, npm, php artisan, migration, test, or curl commands yourself.
- Always provide the exact commands the user should run manually.
- After making file changes, clearly separate:
  1. Files changed
  2. Commands the user should run manually
  3. Expected validation result

## Code Style Preferences

### General

- Prefer clear names over clever abstractions.
- Keep services small and testable.
- Avoid over-engineering.
- Add comments only where the code is not obvious.
- Use environment variables for configurable values.

### Laravel

- Keep controllers thin.
- Put business logic in services or actions.
- Use Form Requests for validation when endpoints become non-trivial.
- Use API Resources for response shaping when useful.
- Use migrations for database changes.
- Prefer explicit route names.

### FastAPI

- Use Pydantic models for request and response schemas.
- Keep agent prompts isolated in service/agent classes.
- Validate and normalize Gemini responses before returning them.
- Return errors in predictable JSON format.

### Nuxt

- Use TypeScript.
- Use composables for API calls.
- Keep pages thin and components reusable.
- Use Tailwind CSS for styling.

## Commands

Expected commands may evolve. Keep this section updated when implementation changes.

From project root:

```bash
cd laravel-backend
```

Backend stack:

```bash
docker compose up -d --build
docker compose ps
docker compose logs -f
```

Laravel commands, service name may be adjusted after compose is created:

```bash
docker compose exec app php artisan migrate
docker compose exec app php artisan test
docker compose exec app php artisan route:list
```

FastAPI commands, service name may be adjusted after compose is created:

```bash
docker compose exec ai-service pytest
docker compose logs -f ai-service
```

Frontend commands from project root:

```bash
cd nuxt-frotend
npm install
npm run dev
npm run build
```

## Agent Output Expectations

When completing a task, summarize:

1. What changed
2. Files changed
3. Documentation updated
4. Commands run
5. Test/build result
6. Next recommended task

If a command fails, show the failure and propose the smallest fix.