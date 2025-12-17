<!--
SYNC IMPACT REPORT
==================
Version Change: UNVERSIONED → 1.1.0
Modified Principles:
  - UPDATED: I. Full-Stack Architecture with Clear Separation (was Component-Based Architecture)
    * Now explicitly specifies Next.js 16+, FastAPI, SQLModel, Neon PostgreSQL, Better Auth
    * Aligns with Hackathon II technology stack requirements
  - NEW: II. Type Safety First
  - NEW: III. Test-Driven Development (TDD) with Pragmatic Hackathon Exception
  - NEW: IV. Integration Testing
  - NEW: V. Observability
  - NEW: VI. Versioning & Breaking Changes
  - NEW: VII. Simplicity & Pragmatism
Added Sections:
  - Development Workflow (with branch strategy, testing gates, deployment)
  - Quality Standards (code quality, performance, security, accessibility)
  - Governance (amendment process, compliance, exceptions, enforcement)
Removed Sections: None
Templates Requiring Updates:
  ✅ plan-template.md - Constitution Check section aligned
  ✅ spec-template.md - User stories and requirements structure aligned
  ✅ tasks-template.md - Task categorization aligned with principles
Technology Stack Alignment:
  ✅ Next.js 16+ (App Router) - Frontend framework
  ✅ FastAPI - Backend framework
  ✅ SQLModel - ORM for Python
  ✅ Neon Serverless PostgreSQL - Database
  ✅ Better Auth - Authentication system
  ✅ TypeScript - Type safety for frontend
Follow-up TODOs: None
-->

# HackatonII Constitution

## Core Principles

### I. Full-Stack Architecture with Clear Separation

**Rule**: The application follows a clear client-server separation:
- **Frontend**: Next.js 16+ with App Router, TypeScript, and React components
- **Backend**: Python FastAPI with SQLModel ORM
- **Database**: Neon Serverless PostgreSQL
- **Authentication**: Better Auth with JWT tokens

All components must be independently deployable and testable. Frontend communicates with backend via RESTful APIs.

**Rationale**: This architecture enables independent scaling, clear separation of concerns, language-specific optimization (TypeScript for frontend, Python for backend), and aligns with the hackathon's technology requirements.

### II. Type Safety First

**Rule**: All code MUST use TypeScript with strict mode enabled. No `any` types except where absolutely necessary and explicitly justified. All component props, API responses, and data models must have explicit type definitions.

**Rationale**: Type safety catches errors at compile time, provides excellent IDE support, serves as living documentation, and reduces runtime errors significantly in production.

### III. Test-Driven Development (TDD)

**Rule**: For all critical business logic and user-facing features, tests MUST be written FIRST and MUST FAIL before implementation begins. Follow the Red-Green-Refactor cycle strictly:
- Red: Write failing test
- Green: Implement minimum code to pass
- Refactor: Clean up while keeping tests green

**Exceptions**: For hackathon rapid prototyping, TDD is strongly recommended but not strictly blocking. However, all completed features MUST have tests before being considered "done."

**Rationale**: TDD ensures requirements are understood, provides confidence in changes, creates a safety net for refactoring, and results in better-designed, more testable code.

### IV. Integration Testing

**Rule**: Integration tests are REQUIRED for:
- API endpoint contracts (request/response validation)
- Database interactions and data persistence
- Third-party service integrations
- Cross-component user workflows
- State management flows

**Rationale**: Unit tests alone cannot catch integration issues. Real-world failures often occur at system boundaries and component interactions.

### V. Observability

**Rule**: All components and services MUST include:
- Structured logging with consistent format (use standard logging library)
- Error boundaries in React components
- Performance monitoring for critical paths
- Clear error messages for debugging

**Rationale**: Observability is essential for debugging production issues, understanding user behavior, and maintaining system health.

### VI. Versioning & Breaking Changes

**Rule**: Follow Semantic Versioning (MAJOR.MINOR.PATCH):
- MAJOR: Breaking changes (incompatible API changes)
- MINOR: New features (backward compatible)
- PATCH: Bug fixes (backward compatible)

All API endpoints and component interfaces must maintain backward compatibility within major versions. Breaking changes require explicit migration guides.

**Rationale**: Clear versioning communicates impact to users and enables confident upgrades without unexpected breakage.

### VII. Simplicity & Pragmatism

**Rule**: Always choose the simplest solution that meets requirements. Follow YAGNI (You Aren't Gonna Need It):
- Don't add features or abstractions for hypothetical future needs
- Prefer standard patterns over clever solutions
- Start with direct implementation; refactor when patterns emerge
- Three uses before creating abstraction

**Rationale**: Over-engineering wastes time, increases complexity, and makes maintenance harder. Simple code is easier to understand, modify, and debug.

## Development Workflow

**Code Review Requirements**:
- All PRs require review before merge
- Reviewer must verify constitution compliance
- Tests must pass in CI/CD pipeline

**Branch Strategy**:
- Feature branches: `###-feature-name` format
- Main branch protected, requires PR
- Branch from latest main, keep branches short-lived

**Testing Gates**:
- Unit tests: Run on every commit
- Integration tests: Run on PR creation
- E2E tests: Run before merge to main
- Coverage threshold: Minimum 80% for new code (hackathon: 60% acceptable)

**Deployment Approval**:
- Staging: Automatic on merge to main
- Production: Manual approval required
- Rollback plan documented for each deployment

## Quality Standards

**Code Quality**:
- ESLint and Prettier configured and enforced
- No TypeScript errors allowed
- All warnings must be addressed or explicitly justified

**Performance Standards**:
- Initial page load: < 3s on 3G
- Time to Interactive (TTI): < 5s
- Lighthouse score: Minimum 80 (hackathon: 70 acceptable)

**Security Requirements**:
- No hardcoded secrets (use environment variables)
- Input validation on all user inputs
- Authentication/Authorization required for protected routes
- OWASP top 10 awareness required

**Accessibility**:
- Minimum WCAG 2.1 Level AA compliance
- Semantic HTML required
- Keyboard navigation support
- Screen reader compatibility

## Governance

**Amendment Process**:
1. Propose change with justification and impact analysis
2. Team review and discussion
3. Approval from project lead required
4. Update constitution with version bump
5. Create migration plan if needed
6. Document in ADR for significant decisions

**Compliance Verification**:
- All PRs must reference constitution principles addressed
- Monthly constitution review sessions
- Complexity violations require explicit justification in plan.md

**Exception Handling**:
- Exceptions to principles allowed only with:
  - Documented justification
  - Time-bound scope (if temporary)
  - Approval from project lead
  - Tracked in complexity tracking table

**Enforcement**:
- Constitution supersedes all other development practices
- Non-compliance blocks PR merge
- Repeated violations require team discussion and process improvement

**Version**: 1.1.0 | **Ratified**: 2025-12-17 | **Last Amended**: 2025-12-17
