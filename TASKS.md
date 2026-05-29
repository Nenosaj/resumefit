# TASKS.md — ResumeFit Implementation Tasks

## How to Use This File

This is the living task board for the coding agent.

Rules:

- Work from top to bottom unless the user changes priority.
- Keep each task small and reviewable.
- Mark a task complete only after validation.
- Add newly discovered tasks under the correct phase.
- Do not skip MVP tasks to build later features.

Task status legend:

```text
[ ] Not started
[/] In progress
[x] Done
[!] Blocked
[?] Needs user decision
```

## Current Priority

Build the backend foundation first:

```text
WSL project structure → Docker inside laravel-backend → Laravel + PostgreSQL + Redis + FastAPI → Gemini Job Analyzer Agent
```

## Phase 0 — Spec and Agent Setup

- [x] Create `GEMINI.md` for agent behavior, workflow, and boundaries.
- [x] Create `SPEC.md` as the living project specification.
- [x] Create `TASKS.md` as the implementation checklist.
- [x] Place these files in the project root.
- [x] Initialize git repository.
- [x] Create `.gitignore` for Laravel, Nuxt, Python, Docker, and environment files.
- [x] Create root `README.md` with project overview and local setup commands.
- [x] Create `docs/` folder.
- [x] Create `docs/ARCHITECTURE.md` with initial service architecture.
- [x] Create `docs/TECH_STACK.md` with stack choices and reasons.
- [x] Create `docs/FEATURES.md` with MVP feature documentation template.
- [x] Create `docs/DECISIONS.md` with initial project decisions.

## Phase 1 — Project Structure

- [x] Create root folder `resumefit/`.
- [x] Create `nuxt-frontend/` folder.
- [x] Create `laravel-backend/` folder.
- [x] Confirm whether `nuxt-frontend/` spelling should stay as requested or be renamed later.
- [x] Keep all Docker files inside `laravel-backend/`.

Expected structure:

```text
resumefit/
├── GEMINI.md
├── SPEC.md
├── TASKS.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── TECH_STACK.md
│   ├── FEATURES.md
│   └── DECISIONS.md
├── nuxt-frontend/
└── laravel-backend/
```

## Phase 2 — Backend Docker Foundation

- [ ] Create `laravel-backend/docker-compose.yml`.
- [ ] Add PostgreSQL service.
- [ ] Add Redis service.
- [ ] Add Laravel PHP service.
- [ ] Add Nginx service or decide to use Laravel dev server for early MVP.
- [ ] Add FastAPI AI service.
- [ ] Add shared Docker network.
- [ ] Add PostgreSQL volume.
- [ ] Create `laravel-backend/.env.example`.
- [ ] Ensure `.env` is ignored by git.
- [ ] Validate `docker compose config`.
- [ ] Run `docker compose up -d --build`.
- [ ] Validate all containers start.
- [ ] Update `docs/ARCHITECTURE.md` and `docs/TECH_STACK.md` with backend Docker foundation details.

## Phase 3 — Laravel Backend Setup

- [ ] Create Laravel app inside `laravel-backend/src/`.
- [ ] Configure Laravel database connection for PostgreSQL container.
- [ ] Configure Redis connection.
- [ ] Generate Laravel app key.
- [ ] Run default Laravel migrations.
- [ ] Create `/api/health` endpoint.
- [ ] Confirm `/api/health` works from host machine.
- [ ] Add Laravel HTTP client config for FastAPI service URL.
- [ ] Update `docs/FEATURES.md` with Laravel health endpoint and backend API foundation notes.

## Phase 4 — FastAPI AI Service Setup

- [ ] Create `laravel-backend/ai-service/`.
- [ ] Add FastAPI `Dockerfile`.
- [ ] Add `requirements.txt`.
- [ ] Add `app/main.py`.
- [ ] Add `GET /` health endpoint.
- [ ] Add Pydantic request/response schemas.
- [ ] Read `GEMINI_API_KEY` from environment.
- [ ] Read `GEMINI_MODEL` from environment.
- [ ] Confirm FastAPI is reachable at `http://localhost:8000`.
- [ ] Update `docs/ARCHITECTURE.md` with FastAPI AI service responsibilities.

## Phase 5 — Gemini Job Analyzer Agent

- [ ] Create `JobAnalyzerAgent` class.
- [ ] Add prompt for extracting structured job data.
- [ ] Force JSON-only response from Gemini.
- [ ] Strip markdown code fences if Gemini returns them.
- [ ] Validate parsed JSON using Pydantic.
- [ ] Return predictable error JSON when parsing fails.
- [ ] Create `POST /analyze-job` endpoint.
- [ ] Test with sample IT Data Analyst job description.
- [ ] Test missing fields return `null` or `[]` instead of fabricated values.
- [ ] Update `docs/FEATURES.md` with Gemini Job Analyzer feature, request/response example, and limitations.

Expected request:

```json
{
  "job_description": "We are hiring an IT Data Analyst..."
}
```

Expected response shape:

```json
{
  "company": null,
  "role": "IT Data Analyst",
  "location": "Cagayan de Oro",
  "work_setup": "On-site",
  "employment_type": null,
  "required_skills": ["SQL", "Python"],
  "soft_skills": ["communication"],
  "responsibilities": [],
  "fresh_graduate_friendly": true,
  "role_type": "IT Data Analyst",
  "summary": "Short neutral summary."
}
```

## Phase 6 — Laravel to FastAPI Integration

- [ ] Create Laravel route `POST /api/jobs/analyze`.
- [ ] Validate request has `job_description`.
- [ ] Laravel calls FastAPI `POST /analyze-job`.
- [ ] Laravel normalizes FastAPI response.
- [ ] Laravel returns frontend-ready JSON.
- [ ] Handle FastAPI timeout.
- [ ] Handle FastAPI validation errors.
- [ ] Add Laravel feature test for `/api/jobs/analyze`.
- [ ] Update `docs/FEATURES.md` with Laravel-to-FastAPI analysis flow.

## Phase 7 — Database Schema MVP

- [ ] Create `profiles` migration.
- [ ] Create `skills` migration.
- [ ] Create `projects` migration.
- [ ] Create `project_bullets` migration.
- [ ] Create `work_experiences` migration.
- [ ] Create `experience_bullets` migration.
- [ ] Create `job_posts` migration.
- [ ] Create `fit_scores` migration.
- [ ] Create `applications` migration.
- [ ] Create `resume_versions` migration.
- [ ] Add Eloquent models and relationships.
- [ ] Run migrations successfully.
- [ ] Update `docs/ARCHITECTURE.md` with database schema overview.

## Phase 8 — Master Resume Data CRUD

- [ ] Create Profile CRUD endpoints.
- [ ] Create Skills CRUD endpoints.
- [ ] Create Projects CRUD endpoints.
- [ ] Create Project Bullets CRUD endpoints.
- [ ] Create Work Experience CRUD endpoints.
- [ ] Create Experience Bullets CRUD endpoints.
- [ ] Add basic request validation.
- [ ] Add seed data for Jason's master resume.
- [ ] Update `docs/FEATURES.md` with master resume data management notes.

## Phase 9 — Fit Score MVP

- [ ] Implement deterministic scoring service first.
- [ ] Score skills match out of 35.
- [ ] Score project evidence out of 25.
- [ ] Score experience relevance out of 20.
- [ ] Score location/work setup out of 10.
- [ ] Score junior/fresh-grad friendliness out of 10.
- [ ] Return match level and apply decision.
- [ ] Do not call score a guaranteed interview chance.
- [ ] Update `docs/FEATURES.md` with Fit Score formula and interpretation.

## Phase 10 — Project Recommendation MVP

- [ ] Implement role-based project recommendation rules.
- [ ] Prioritize Automated Email Parser, MediFort, and LUPAD for IT Data Analyst roles.
- [ ] Prioritize TapIT, LUPAD, and MediFort for Full Stack roles.
- [ ] Prioritize Automated Email Parser, LUPAD, and ResumeFit for AI Automation roles.
- [ ] Prioritize Globe internship, MediFort, and TapIT/Automated Email Parser for Support roles.
- [ ] Return explanation for why each project was recommended.
- [ ] Update `docs/FEATURES.md` with project recommendation logic.

## Phase 11 — Resume Tailoring MVP

- [ ] Generate tailored professional summary.
- [ ] Generate tailored skills section.
- [ ] Generate tailored project bullets.
- [ ] Ensure generated bullets do not invent experience.
- [ ] Save tailored result as `resume_versions` row.
- [ ] Return editable preview data to frontend.
- [ ] Update `docs/FEATURES.md` with resume tailoring behavior and honesty rules.

## Phase 12 — Application Tracker MVP

- [ ] Create job post save endpoint.
- [ ] Create application save endpoint.
- [ ] Add statuses:
  - Saved
  - Tailoring
  - Ready to Apply
  - Applied
  - Followed Up
  - Interview Scheduled
  - Interview Done
  - Rejected
  - No Reply
  - Offer
  - Archived
- [ ] Add follow-up date field.
- [ ] Add notes field.
- [ ] Add next action field.
- [ ] Update `docs/FEATURES.md` with application tracker statuses and workflow.

## Phase 13 — Nuxt Frontend MVP

- [ ] Initialize Nuxt app in `nuxt-frotend/`.
- [ ] Install Tailwind CSS.
- [ ] Create dashboard layout.
- [ ] Create Job Analyzer page.
- [ ] Add paste job description textarea.
- [ ] Call Laravel `POST /api/jobs/analyze`.
- [ ] Show parsed job requirements.
- [ ] Show fit score card once scoring is implemented.
- [ ] Show matched skills.
- [ ] Show missing skills.
- [ ] Show recommended projects.
- [ ] Show tailored resume preview.
- [ ] Update `docs/FEATURES.md` with Nuxt Job Analyzer UI flow.

## Phase 14 — Validation and Demo

- [ ] Create sample job descriptions for testing.
- [ ] Record expected outputs for at least three role types.
- [ ] Confirm Docker startup from fresh clone.
- [ ] Confirm no secrets are committed.
- [ ] Update README with demo flow.
- [ ] Prepare portfolio explanation of ResumeFit.
- [ ] Confirm documentation explains features, architecture, tech stack, and key decisions.

## Parking Lot — Later Features

Do not build these until MVP 1 works:

- [ ] DOCX resume export.
- [ ] Cover letter generator.
- [ ] Gmail draft generation.
- [ ] n8n workflow automation.
- [ ] Google Sheets sync.
- [ ] Notion sync.
- [ ] pgvector embeddings.
- [ ] Semantic job matching.
- [ ] PDF export.
- [ ] Job board scraping.
- [ ] Production deployment.