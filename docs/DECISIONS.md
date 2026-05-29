# Decisions

This document records important product and technical decisions for ResumeFit.

## Decision Template
Whenever a core decision is made, document it here:

```text
## YYYY-MM-DD — Decision Title

Decision:
Context:
Options Considered:
Reason:
Tradeoffs:
```

## 2026-05-29 — Implement CI Validation without CD

Decision: Implement a GitHub Actions workflow for Continuous Integration (CI) only, postponing Continuous Deployment (CD) for later.
Context: We need to validate that backend code changes do not break the Docker composition and fundamental services, but we do not yet have a target deployment environment for ResumeFit.
Options Considered:
- Full CI/CD pipeline (rejected due to lack of deployment target).
- No automated validation (rejected because regressions would go unnoticed).
- CI only (chosen).
Reason: CI ensures health checks and migrations pass on new pull requests, improving code reliability before merging, while keeping the workflow focused and simple until a deployment strategy is defined.
Tradeoffs: Lacks automated deployment, requiring manual deployment or future expansion. Placeholder secrets are used instead of real secure environment configuration.