# SPEC.md — ResumeFit Specification

## Status

Living specification. Keep this file updated whenever the product scope, architecture, data model, API contract, or implementation plan changes.

## Product Vision

ResumeFit is an AI-assisted job matching and resume tailoring system that helps Jason T. Daohog apply to jobs more strategically.

The system stores a structured master resume database, compares job descriptions against Jason's skills, projects, work experience, education, and portfolio, then generates realistic fit insights and tailored application content.

The goal is not to guarantee interviews. The goal is to improve application quality, reduce wasted applications, and create a repeatable job-search workflow.

## Primary User

Jason T. Daohog

Profile:

- Computer Engineering student / fresh graduate candidate
- Based in Cagayan de Oro City, Philippines
- Background in full-stack development, IT systems, data annotation, networking, Linux, automation, and AI-assisted workflows

Primary job lanes:

1. Junior Full Stack Developer
2. Junior Backend Developer
3. IT Data Analyst
4. Application Support / Technical Support Engineer
5. AI Automation Developer
6. Business Systems / ERP Junior Developer
7. Junior Python Developer

## First Build Goal

The first usable version must be simple:

```text
Paste job description → analyze → get fit score → get recommended projects → get tailored resume bullets → save to tracker
```

Do not start with scraping, PDF generation, or complex multi-agent orchestration.

## MVP Scope

### MVP 1 — Manual Job Analyzer

The first MVP includes:

1. Master resume data stored in PostgreSQL
2. Manual job description paste
3. Job parser
4. Fit score generator
5. Recommended projects
6. Tailored summary generator
7. Tailored skills section generator
8. Tailored project bullet generator
9. Application tracker

### Later MVPs

MVP 2:

- DOCX resume generation
- Cover letter generation
- Resume version history
- Download generated files

MVP 3:

- n8n job intake
- Follow-up reminders
- Gmail draft generation
- Google Sheets or Notion sync

MVP 4:

- Embeddings for projects, skills, and experience
- Job description embeddings
- pgvector similarity search
- Improved project ranking
- Improved missing-skill detection

## Non-Goals for First Build

Do not build these first:

- automatic job scraping
- PDF generation
- multi-agent orchestration framework
- paid cloud storage
- AWS services
- complex authentication and teams
- production deployment
- semantic vector matching

## Repository Structure

The desired root structure is:

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

`nuxt-frotend/` is intentionally spelled according to the user's requested structure. Do not rename it without approval.

Docker must live in:

```text
laravel-backend/
```

Suggested backend structure:

```text
laravel-backend/
├── docker-compose.yml
├── .env.example
├── src/                       # Laravel app
├── docker/
│   ├── php/
│   │   └── Dockerfile
│   └── nginx/
│       └── default.conf
└── ai-service/
    ├── Dockerfile
    ├── requirements.txt
    └── app/
        ├── main.py
        ├── agents/
        │   └── job_analyzer_agent.py
        ├── schemas/
        └── services/
```

## Architecture

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

Supporting services:

```text
Redis: queue/cache
n8n: automation later
Local storage: generated documents and uploads
pgvector: semantic matching later
```

## Tech Stack

```text
Frontend: Nuxt + Vue + TypeScript + Tailwind CSS
Backend API: Laravel
AI/Data Service: Python + FastAPI
LLM Provider: Gemini API
Database: PostgreSQL
Vector Search: pgvector later
Queue/Cache: Redis
Automation: n8n later
Storage: local storage first
Deployment: Docker Compose first
```

## Documentation Strategy

Documentation is required for important work. The goal is to make ResumeFit easy to continue, explain, and present as a portfolio project.

Documentation files:

```text
README.md                # project overview, setup, and demo flow
SPEC.md                  # living product and technical specification
TASKS.md                 # task board and implementation progress
docs/ARCHITECTURE.md     # service architecture, data flow, and responsibilities
docs/TECH_STACK.md       # technologies used, why they were chosen, and later alternatives
docs/FEATURES.md         # explanation of each major feature and how to test it
docs/DECISIONS.md        # important product and technical decisions
```

Documentation update rules:

- Every completed feature must be documented in `docs/FEATURES.md`.
- Architecture changes must be reflected in both `docs/ARCHITECTURE.md` and `SPEC.md`.
- Tech stack changes must be reflected in both `docs/TECH_STACK.md` and `SPEC.md`.
- Important tradeoffs or decisions must be recorded in `docs/DECISIONS.md`.
- README should stay focused on setup, quickstart, and demo flow.
- Documentation must not claim a feature is complete until the implementation is validated.

Minimum feature documentation format:

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

Minimum decision documentation format:

```text
## YYYY-MM-DD — Decision Title

Decision:
Context:
Options Considered:
Reason:
Tradeoffs:
```

## Core User Flow

1. Jason opens ResumeFit.
2. Jason pastes a job description.
3. ResumeFit extracts structured job data:
   - company
   - role
   - location
   - work setup
   - employment type
   - required skills
   - soft skills
   - responsibilities
   - fresh graduate friendliness
   - role type
4. ResumeFit compares the job against Jason's master resume.
5. ResumeFit returns:
   - Fit Score
   - match level
   - apply decision
   - matched skills
   - missing skills
   - recommended projects
   - resume angle
6. ResumeFit generates tailored resume sections.
7. Jason reviews and edits.
8. Jason saves the job/application to the tracker.

## Fit Score System

Score must be realistic and explainable.

Suggested scoring:

```text
Skills Match: 35 points
Project Evidence: 25 points
Experience Relevance: 20 points
Location / Work Setup Match: 10 points
Fresh Grad / Junior Friendliness: 10 points
Total: 100 points
```

Score meaning:

```text
90–100: Very strong match. Tailor immediately and apply.
80–89: Strong match. Apply after tailoring.
70–79: Possible match. Apply if interested, but improve positioning.
60–69: Weak-to-moderate match. Apply only if strategic.
Below 60: Low match. Skip unless there is a strong reason.
```

Never call this a guaranteed interview probability.

## Primary Data Models

### Profile

```text
id
user_id
full_name
email
phone
location
linkedin_url
github_url
portfolio_url
summary
created_at
updated_at
```

### Skill

```text
id
user_id
name
category
proficiency
created_at
updated_at
```

### Project

```text
id
user_id
name
type
description
tech_stack
repo_url
live_url
start_date
end_date
created_at
updated_at
```

### ProjectBullet

```text
id
project_id
bullet
role_angle
keywords
created_at
updated_at
```

### WorkExperience

```text
id
user_id
company
role
location
start_date
end_date
description
created_at
updated_at
```

### ExperienceBullet

```text
id
work_experience_id
bullet
role_angle
keywords
created_at
updated_at
```

### JobPost

```text
id
user_id
company
role
location
work_setup
employment_type
job_url
raw_description
parsed_description
created_at
updated_at
```

### FitScore

```text
id
job_post_id
score
match_level
apply_decision
skills_score
project_score
experience_score
location_score
junior_score
matched_skills
missing_skills
recommended_projects
resume_angle
explanation
created_at
updated_at
```

### Application

```text
id
user_id
job_post_id
status
date_applied
follow_up_date
resume_version_id
cover_letter_id
contact_person
contact_url
notes
created_at
updated_at
```

### ResumeVersion

```text
id
user_id
job_post_id
title
summary
skills_section
experience_section
projects_section
file_path
created_at
updated_at
```

## API Contracts

### Laravel API

Laravel owns persistence, validation, application workflow, and frontend-facing API routes.

Initial routes:

```text
GET  /api/health
POST /api/jobs/analyze
POST /api/job-posts
GET  /api/job-posts
GET  /api/job-posts/{id}
POST /api/applications
GET  /api/applications
PATCH /api/applications/{id}
```

### `POST /api/jobs/analyze`

Purpose:

- Accept a pasted job description from Nuxt.
- Forward text to FastAPI.
- Receive parsed job data and later fit scoring.
- Return a frontend-ready response.

Request:

```json
{
  "job_description": "string",
  "job_url": "optional string"
}
```

Initial response:

```json
{
  "company": "string or null",
  "role": "string or null",
  "location": "string or null",
  "work_setup": "string or null",
  "employment_type": "string or null",
  "required_skills": [],
  "soft_skills": [],
  "responsibilities": [],
  "fresh_graduate_friendly": true,
  "role_type": "IT Data Analyst",
  "summary": "string"
}
```

Expanded response later:

```json
{
  "fit_score": 88,
  "match_level": "Strong Match",
  "apply_decision": "Apply after tailoring",
  "matched_skills": [],
  "missing_skills": [],
  "recommended_projects": [],
  "resume_angle": "string",
  "tailored_summary": "string",
  "tailored_project_bullets": []
}
```

## FastAPI AI Service

FastAPI owns AI/data-processing operations.

Initial endpoint:

```text
GET  /
POST /analyze-job
```

Later endpoints:

```text
POST /score-fit
POST /recommend-projects
POST /tailor-resume
POST /generate-cover-letter
POST /generate-follow-up
POST /generate-interview-prep
POST /embed-profile
POST /embed-job
```

### Gemini Job Analyzer Agent

The first agent is `JobAnalyzerAgent`.

Responsibilities:

- Parse a pasted job description.
- Extract structured job fields.
- Classify the role type.
- Return valid JSON only.
- Avoid fabricating missing information.
- Use `null` or empty arrays when unknown.

Role types:

```text
Junior Full Stack Developer
Junior Backend Developer
IT Data Analyst
Application Support / Technical Support Engineer
AI Automation Developer
Business Systems / ERP Junior Developer
Junior Python Developer
Other
```

## AI Output Validation

Gemini output must be validated before use.

Rules:

- Response must be parseable JSON.
- Unknown scalar fields should be `null`.
- Unknown list fields should be `[]`.
- Fit Score must be between 0 and 100.
- The model must not invent resume details.
- Tailored resume output must be based only on stored master resume data.

## Resume Tailoring Rules

When tailoring a resume:

1. Do not invent experience.
2. Do not claim a skill unless it exists in the master resume or the user confirms it.
3. Reframe projects honestly based on the target role.
4. Prioritize the most relevant projects, not always the most technically impressive projects.
5. Keep bullets concise and results-focused.
6. Use keywords from the job post naturally.
7. Keep the resume suitable for fresh graduate / junior roles.
8. Do not overload the resume with every technology.
9. Match the employer's language where possible.
10. Keep confidence high but realistic.

## Project Recommendation Logic

### Junior Full Stack Developer

Prioritize:

1. TapIT
2. LUPAD
3. MediFort

Emphasize:

- Laravel
- Nuxt/Vue
- TypeScript
- APIs
- Git/GitHub
- Docker
- full-stack development

### IT Data Analyst

Prioritize:

1. Automated Email Parser
2. MediFort
3. LUPAD

Emphasize:

- Python
- SQL
- data handling
- Excel/report automation
- databases
- IT systems
- reporting

### AI Automation Developer

Prioritize:

1. Automated Email Parser
2. LUPAD
3. ResumeFit

Emphasize:

- Python
- FastAPI
- AI workflows
- automation
- n8n
- APIs
- data extraction
- LLM-assisted workflows

### Technical Support / Application Support

Prioritize:

1. Globe Telecom internship
2. MediFort
3. TapIT or Automated Email Parser

Emphasize:

- troubleshooting
- Linux
- networking
- system monitoring
- documentation
- communication
- API/system understanding

### ERP / Business Systems Developer

Prioritize:

1. MediFort
2. Automated Email Parser
3. TapIT

Emphasize:

- database-backed systems
- internal tools
- SQL
- business workflows
- automation
- willingness to learn ERP systems

## Security Requirements

- Store secrets only in `.env`.
- Commit `.env.example`, not `.env`.
- Do not log API keys.
- Validate user input.
- Sanitize generated HTML or markdown before rendering.
- Keep Gemini calls server-side only.
- Do not expose direct Gemini API calls from Nuxt.

## Testing Strategy

Minimum validation for MVP:

- Docker stack starts successfully.
- Laravel health endpoint returns success.
- FastAPI health endpoint returns success.
- `POST /analyze-job` returns valid JSON for a sample job description.
- `POST /api/jobs/analyze` calls FastAPI and returns normalized JSON.
- Database migrations run successfully.

Later tests:

- Laravel feature tests for job analysis and tracker APIs.
- FastAPI unit tests for response parsing and schema validation.
- Nuxt component tests for Job Analyzer UI.

## Commands

Backend root:

```bash
cd laravel-backend
```

Docker:

```bash
docker compose up -d --build
docker compose ps
docker compose logs -f
```

Laravel, service name may be adjusted when compose is implemented:

```bash
docker compose exec app php artisan migrate
docker compose exec app php artisan test
```

FastAPI, service name may be adjusted when compose is implemented:

```bash
docker compose exec ai-service pytest
```

Frontend:

```bash
cd ../nuxt-frotend
npm install
npm run dev
npm run build
```

## Acceptance Criteria for First Milestone

The first milestone is complete when:

1. The root folders exist:
   - `nuxt-frotend/`
   - `laravel-backend/`
2. Docker Compose lives inside `laravel-backend/`.
3. PostgreSQL starts in Docker.
4. Redis starts in Docker.
5. Laravel runs behind Nginx or via Laravel dev server in Docker.
6. FastAPI AI service runs in Docker.
7. FastAPI exposes `POST /analyze-job`.
8. Gemini API key is read from `.env`.
9. A sample job description returns structured JSON.
10. No secrets are committed.
11. Initial documentation files exist under `docs/`.
12. The completed milestone is explained in `docs/FEATURES.md`, `docs/ARCHITECTURE.md`, and `docs/TECH_STACK.md` where relevant.

## References

- Addy Osmani, "How to write a good spec for AI agents": https://addyosmani.com/blog/good-spec/
- Gemini CLI `GEMINI.md` context documentation: https://google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html