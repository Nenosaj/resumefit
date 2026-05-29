# ResumeFit

ResumeFit is an AI-assisted job matching and resume tailoring system that helps streamline job applications by generating realistic fit insights and tailored application content.

## MVP Goal

The first usable version (MVP 1) includes a manual job analyzer:
`Paste job description → analyze → get fit score → get recommended projects → get tailored resume bullets → save to tracker`

## Structure

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

## Continuous Integration

ResumeFit uses GitHub Actions for Continuous Integration (CI). Pushes and pull requests to the `main` branch trigger a backend validation workflow that:
- Builds the Docker Compose stack
- Runs Laravel migrations
- Verifies system health endpoints

*(A CI status badge will be added here once the repository is pushed to a remote host).*
