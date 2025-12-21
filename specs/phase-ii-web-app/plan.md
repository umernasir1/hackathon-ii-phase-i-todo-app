# Implementation Plan: Todo Full-Stack Web Application (Phase II)

**Feature Branch**: `002-phase-ii-web-app`
**Created**: 2025-12-18
**Status**: Draft
**Spec Reference**: `specs/phase-ii-web-app/spec.md`

---

## 1. Scope and Dependencies

### In Scope
- Full-stack web application with Next.js frontend and FastAPI backend
- User authentication and authorization with Better Auth + JWT
- Database persistence with Neon PostgreSQL
- All 5 Basic Level features from Phase I (Add, View, Update, Delete, Mark Complete)
- Responsive UI for desktop and mobile
- RESTful API architecture
- Deployment to Vercel (frontend) and cloud hosting (backend)

### Out of Scope
- Password reset/email verification
- OAuth/social login
- Advanced features (priorities, tags, search, filters, due dates)
- Real-time collaboration
- AI chatbot interface (Phase III)
- Kubernetes deployment (Phase IV-V)

### External Dependencies

| Dependency | Version | Purpose | Owner |
|------------|---------|---------|-------|
| Neon PostgreSQL | Latest | Database | Neon (managed service) |
| Vercel | Latest | Frontend hosting | Vercel (managed service) |
| Railway/Render | Latest | Backend hosting | Railway/Render (managed service) |
| Better Auth | Latest | Authentication | Frontend team |
| Next.js | 16+ | Frontend framework | Frontend team |
| FastAPI | Latest | Backend framework | Backend team |
| SQLModel | Latest | ORM | Backend team |

---

## 2. Key Decisions and Rationale

### Decision 1: Monorepo Structure

**Options Considered:**
1. **Monorepo** (frontend + backend in same repo) ✅ SELECTED
2. Separate repos (frontend and backend split)
3. Polyrepo with shared packages

**Trade-offs:**

| Approach | Pros | Cons |
|----------|------|------|
| Monorepo | Single source of truth, easier spec management, simpler CI/CD | Larger repo size |
| Separate repos | Independent deployment, clear boundaries | Harder to sync specs, duplicate tooling |
| Polyrepo | Shared code reuse | Over-engineering for hackathon |

**Rationale:**
- Spec-Kit Plus works best with single context
- Claude Code can see entire project
- Easier for hackathon timeline (Dec 14 deadline)
- Simpler to manage specs/history/docs in one place

**Principles:**
- Single source of truth for specs
- Smallest viable change from Phase I structure
- Reversible: can split repos later if needed

---

### Decision 2: Authentication Strategy (Better Auth + JWT)

**Options Considered:**
1. **Better Auth (frontend) + JWT verification (backend)** ✅ SELECTED
2. Auth0/Clerk (managed auth services)
3. Custom auth with sessions

**Trade-offs:**

| Approach | Pros | Cons |
|----------|------|------|
| Better Auth + JWT | Full control, no vendor lock-in, free | More setup complexity |
| Auth0/Clerk | Managed service, easy setup | Costs money, vendor lock-in |
| Custom auth | Full flexibility | Security risks, time-consuming |

**Rationale:**
- Better Auth is modern, TypeScript-native, and free
- JWT tokens enable stateless backend (scalable)
- No third-party API dependencies
- Meets hackathon requirements

**Principles:**
- Security first (bcrypt password hashing)
- Stateless backend (horizontal scalability)
- Industry standard (JWT)

---

### Decision 3: Database Choice (Neon PostgreSQL)

**Options Considered:**
1. **Neon Serverless PostgreSQL** ✅ SELECTED
2. Supabase (Postgres + Auth + Storage)
3. PlanetScale (MySQL serverless)

**Trade-offs:**

| Approach | Pros | Cons |
|----------|------|------|
| Neon | Free tier, serverless, pure Postgres | Fewer features than Supabase |
| Supabase | Built-in auth, storage, realtime | More complexity, vendor lock-in |
| PlanetScale | MySQL, great DX | Not Postgres, schema changes complex |

**Rationale:**
- Hackathon requirement specifies Neon
- Free tier sufficient for development
- SQLModel (Pydantic + SQLAlchemy) works best with Postgres
- Serverless = no maintenance overhead

**Principles:**
- Use managed services where possible
- Postgres reliability and features
- Cost-effective for development

---

### Decision 4: API Design (RESTful with User Scoping)

**API Pattern:** `/api/{user_id}/tasks`

**Options Considered:**
1. **User ID in URL path** ✅ SELECTED
2. User ID extracted from JWT only
3. Session-based with cookies

**Trade-offs:**

| Approach | Pros | Cons |
|----------|------|------|
| User ID in path | Explicit, easy to debug, clear ownership | Redundant (also in JWT) |
| JWT only | Cleaner URLs, implicit auth | Harder to debug, less explicit |
| Session-based | Traditional, simple | Not stateless, scalability issues |

**Rationale:**
- Explicit user scoping makes authorization clear
- Backend validates path user_id matches JWT user_id
- Easy to test and debug
- Follows REST conventions for resource hierarchy

**Principles:**
- Explicit over implicit
- Defense in depth (check user_id in both path and JWT)
- RESTful resource naming

---

## 3. Interfaces and API Contracts

### 3.1 REST API Endpoints

#### Base URL
- **Development**: `http://localhost:8000`
- **Production**: `https://api-todo.example.com`

#### Authentication
All endpoints (except public auth endpoints) require JWT token:
```
Authorization: Bearer <jwt_token>
```

---

#### Endpoint 1: GET /api/{user_id}/tasks

**Purpose**: List all tasks for authenticated user

**Request:**
```http
GET /api/{user_id}/tasks HTTP/1.1
Host: api-todo.example.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Response (200 OK):**
```json
{
  "tasks": [
    {
      "id": 1,
      "user_id": "user_123",
      "title": "Buy groceries",
      "description": "Milk, eggs, bread",
      "completed": false,
      "created_at": "2025-12-18T10:00:00Z",
      "updated_at": "2025-12-18T10:00:00Z"
    }
  ],
  "total": 1,
  "completed": 0,
  "pending": 1
}
```

**Errors:**
- `401 Unauthorized`: Missing or invalid JWT
- `403 Forbidden`: user_id in path doesn't match JWT user_id
- `500 Internal Server Error`: Database connection failed

**Idempotency**: Yes (GET is idempotent)

**Timeout**: 5 seconds

**Retry Strategy**: Frontend retries up to 3 times with exponential backoff

---

#### Endpoint 2: POST /api/{user_id}/tasks

**Purpose**: Create a new task

**Request:**
```http
POST /api/{user_id}/tasks HTTP/1.1
Host: api-todo.example.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread"
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "user_id": "user_123",
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": false,
  "created_at": "2025-12-18T10:00:00Z",
  "updated_at": "2025-12-18T10:00:00Z"
}
```

**Errors:**
- `400 Bad Request`: Invalid input (title missing, title > 200 chars, description > 1000 chars)
- `401 Unauthorized`: Missing or invalid JWT
- `403 Forbidden`: user_id mismatch
- `500 Internal Server Error`: Database error

**Idempotency**: No (creates new resource each time)

**Timeout**: 5 seconds

---

#### Endpoint 3: GET /api/{user_id}/tasks/{id}

**Purpose**: Get details of a specific task

**Request:**
```http
GET /api/{user_id}/tasks/1 HTTP/1.1
Host: api-todo.example.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Response (200 OK):**
```json
{
  "id": 1,
  "user_id": "user_123",
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": false,
  "created_at": "2025-12-18T10:00:00Z",
  "updated_at": "2025-12-18T10:00:00Z"
}
```

**Errors:**
- `401 Unauthorized`: Missing or invalid JWT
- `403 Forbidden`: Task belongs to different user
- `404 Not Found`: Task doesn't exist
- `500 Internal Server Error`: Database error

**Idempotency**: Yes

---

#### Endpoint 4: PUT /api/{user_id}/tasks/{id}

**Purpose**: Update task title and/or description

**Request:**
```http
PUT /api/{user_id}/tasks/1 HTTP/1.1
Host: api-todo.example.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
  "title": "Buy groceries and supplies",
  "description": "Milk, eggs, bread, cheese"
}
```

**Response (200 OK):**
```json
{
  "id": 1,
  "user_id": "user_123",
  "title": "Buy groceries and supplies",
  "description": "Milk, eggs, bread, cheese",
  "completed": false,
  "created_at": "2025-12-18T10:00:00Z",
  "updated_at": "2025-12-18T10:30:00Z"
}
```

**Errors:**
- `400 Bad Request`: Invalid input
- `401 Unauthorized`: Missing or invalid JWT
- `403 Forbidden`: Task belongs to different user
- `404 Not Found`: Task doesn't exist
- `500 Internal Server Error`: Database error

**Idempotency**: Yes (multiple identical PUTs result in same state)

---

#### Endpoint 5: DELETE /api/{user_id}/tasks/{id}

**Purpose**: Delete a task

**Request:**
```http
DELETE /api/{user_id}/tasks/1 HTTP/1.1
Host: api-todo.example.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Response (204 No Content):**
```http
HTTP/1.1 204 No Content
```

**Errors:**
- `401 Unauthorized`: Missing or invalid JWT
- `403 Forbidden`: Task belongs to different user
- `404 Not Found`: Task doesn't exist
- `500 Internal Server Error`: Database error

**Idempotency**: Yes (deleting same task multiple times is safe)

---

#### Endpoint 6: PATCH /api/{user_id}/tasks/{id}/complete

**Purpose**: Toggle task completion status

**Request:**
```http
PATCH /api/{user_id}/tasks/1/complete HTTP/1.1
Host: api-todo.example.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
  "completed": true
}
```

**Response (200 OK):**
```json
{
  "id": 1,
  "user_id": "user_123",
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": true,
  "created_at": "2025-12-18T10:00:00Z",
  "updated_at": "2025-12-18T10:45:00Z"
}
```

**Errors:**
- `400 Bad Request`: Invalid completed value (must be boolean)
- `401 Unauthorized`: Missing or invalid JWT
- `403 Forbidden`: Task belongs to different user
- `404 Not Found`: Task doesn't exist
- `500 Internal Server Error`: Database error

**Idempotency**: Yes (setting to same value is safe)

---

### 3.2 Error Taxonomy

**Status Codes:**

| Code | Meaning | When to Use |
|------|---------|-------------|
| 200 | OK | Successful GET, PUT, PATCH |
| 201 | Created | Successful POST |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Invalid input (validation failed) |
| 401 | Unauthorized | Missing, invalid, or expired JWT |
| 403 | Forbidden | Valid JWT but insufficient permissions |
| 404 | Not Found | Resource doesn't exist |
| 500 | Internal Server Error | Database error, unexpected exception |

**Error Response Format:**
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Title must be between 1 and 200 characters",
    "field": "title"
  }
}
```

---

## 4. Non-Functional Requirements (NFRs) and Budgets

### 4.1 Performance

**Requirements:**
- **p95 Latency**: < 500ms for all API endpoints
- **p99 Latency**: < 1000ms
- **Throughput**: Support 100 concurrent users
- **Frontend Load Time**: < 2s (First Contentful Paint)

**Resource Caps:**
- Database connections: Max 10 concurrent (Neon free tier limit)
- Backend memory: 512MB
- Frontend bundle size: < 500KB (gzipped)

**Measurement:**
- Use Vercel Analytics for frontend
- Use FastAPI middleware to log response times
- Monitor Neon dashboard for database performance

---

### 4.2 Reliability

**SLOs:**
- Availability: 99% (hackathon context, not production)
- Error Rate: < 1% of requests

**Error Budget:**
- Allow 7 hours of downtime per month
- Allow 1 failed request per 100 requests

**Degradation Strategy:**
- If database connection fails: Show cached data with warning banner
- If backend is down: Show maintenance page with retry button
- If authentication fails: Redirect to login page

---

### 4.3 Security

**Authentication & Authorization:**
- Passwords hashed with bcrypt (cost factor 12)
- JWT tokens signed with HS256 algorithm
- JWT secret stored in environment variables (never committed)
- Token expiry: 7 days
- Backend validates user_id in path matches JWT claim

**Data Handling:**
- All API requests over HTTPS in production
- Database connection string in environment variables
- No sensitive data in error messages
- SQL injection prevented via SQLModel parameterized queries

**Secrets Management:**
- `.env.local` for local development (gitignored)
- Vercel environment variables for frontend
- Railway/Render environment variables for backend

**Auditing:**
- Log all authentication events (login, logout)
- Log all task mutations (create, update, delete) with user_id and timestamp

---

### 4.4 Cost

**Unit Economics:**
- Neon PostgreSQL: Free tier (0.5GB storage, 100 hours compute/month)
- Vercel: Free tier (100GB bandwidth/month)
- Railway/Render: Free tier ($5 credit, 500MB RAM)

**Total Cost:** $0/month for development and hackathon demo

**Upgrade Path (if needed):**
- Neon Pro: $19/month (10GB storage)
- Vercel Pro: $20/month (1TB bandwidth)
- Railway: $5/month for 8GB RAM

---

## 5. Data Management and Migration

### 5.1 Source of Truth

**Database:** Neon PostgreSQL is the single source of truth

**Schema Version Control:**
- Use Alembic for database migrations
- Migration files stored in `backend/alembic/versions/`
- Each migration has up and down scripts

---

### 5.2 Database Schema

#### Table: users

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PRIMARY KEY, DEFAULT gen_random_uuid() | User unique identifier |
| email | VARCHAR(255) | UNIQUE, NOT NULL | User email (login) |
| password_hash | VARCHAR(255) | NOT NULL | Bcrypt hashed password |
| name | VARCHAR(100) | NULL | User display name |
| created_at | TIMESTAMP | NOT NULL, DEFAULT NOW() | Account creation time |
| updated_at | TIMESTAMP | NOT NULL, DEFAULT NOW() | Last update time |

**Indexes:**
- `idx_users_email` on `email` (for fast login lookups)

---

#### Table: tasks

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY, SERIAL | Task unique identifier |
| user_id | UUID | FOREIGN KEY REFERENCES users(id) ON DELETE CASCADE, NOT NULL | Task owner |
| title | VARCHAR(200) | NOT NULL | Task title |
| description | TEXT | NULL | Task description (max 1000 chars, enforced in app) |
| completed | BOOLEAN | NOT NULL, DEFAULT FALSE | Completion status |
| created_at | TIMESTAMP | NOT NULL, DEFAULT NOW() | Task creation time |
| updated_at | TIMESTAMP | NOT NULL, DEFAULT NOW() | Last update time |

**Indexes:**
- `idx_tasks_user_id` on `user_id` (for fast user task lookups)
- `idx_tasks_completed` on `completed` (for filtering by status)

**Foreign Keys:**
- `tasks.user_id` → `users.id` (ON DELETE CASCADE: if user deleted, their tasks are deleted)

---

### 5.3 Schema Evolution

**Migration Strategy:**
- Use Alembic to generate migrations
- Test migrations locally before applying to production
- Backward compatible changes only (no breaking changes)

**Example Migration:**
```bash
# Generate migration
alembic revision --autogenerate -m "create users and tasks tables"

# Apply migration
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

---

### 5.4 Data Retention

**Policy:**
- User accounts retained indefinitely (no auto-deletion)
- Tasks retained indefinitely
- Completed tasks NOT auto-archived (user controls deletion)

**Deletion:**
- User can delete tasks manually
- If user account deleted (future feature), CASCADE deletes all tasks

---

## 6. Operational Readiness

### 6.1 Observability

**Logs:**
- Backend: Structured JSON logs with timestamp, level, message, user_id
- Frontend: Console errors sent to error tracking (future: Sentry)

**Metrics:**
- API response times (per endpoint)
- Error rates (4xx, 5xx)
- Database query times

**Traces:**
- Not implemented for hackathon (future: OpenTelemetry)

**Tools:**
- FastAPI built-in logging
- Vercel Analytics for frontend
- Neon dashboard for database metrics

---

### 6.2 Alerting

**Thresholds:**
- Alert if API p95 latency > 1000ms for 5 minutes
- Alert if error rate > 5% for 5 minutes
- Alert if database connection pool exhausted

**On-Call Owners:**
- Not applicable for hackathon (single developer)

---

### 6.3 Runbooks

#### Runbook 1: Backend Won't Start

**Symptoms:** `uvicorn main:app` fails with error

**Common Causes:**
1. Missing environment variables
2. Database connection string invalid
3. Port 8000 already in use

**Resolution:**
1. Check `.env` file exists in `backend/` directory
2. Verify `DATABASE_URL` is correct
3. Run `lsof -i :8000` and kill process if needed
4. Check logs for specific error

---

#### Runbook 2: Frontend Can't Connect to Backend

**Symptoms:** API calls return CORS errors or network errors

**Common Causes:**
1. Backend not running
2. CORS not configured
3. Wrong API URL in frontend

**Resolution:**
1. Verify backend is running: `curl http://localhost:8000/health`
2. Check CORS middleware in FastAPI includes frontend origin
3. Verify `NEXT_PUBLIC_API_URL` in frontend `.env.local`

---

#### Runbook 3: Authentication Fails

**Symptoms:** Login returns 401 or token invalid

**Common Causes:**
1. JWT secret mismatch between frontend and backend
2. Token expired
3. User credentials incorrect

**Resolution:**
1. Verify `BETTER_AUTH_SECRET` matches in both services
2. Check token expiry time
3. Test with known good credentials

---

### 6.4 Deployment Strategy

#### Development Environment

**Frontend:**
```bash
cd frontend
npm install
npm run dev  # Runs on http://localhost:3000
```

**Backend:**
```bash
cd backend
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
uvicorn app.main:app --reload  # Runs on http://localhost:8000
```

---

#### Production Deployment

**Frontend (Vercel):**
1. Connect GitHub repo to Vercel
2. Set environment variables:
   - `NEXT_PUBLIC_API_URL`: Backend production URL
   - `BETTER_AUTH_SECRET`: Shared secret
3. Deploy: `git push origin main` (auto-deploys)

**Backend (Railway/Render):**
1. Connect GitHub repo to Railway/Render
2. Set environment variables:
   - `DATABASE_URL`: Neon connection string
   - `JWT_SECRET`: Same as `BETTER_AUTH_SECRET`
   - `CORS_ORIGINS`: Frontend production URL
3. Deploy: `git push origin main` (auto-deploys)

**Database (Neon):**
1. Create database via Neon dashboard
2. Copy connection string
3. Run migrations: `alembic upgrade head`

---

### 6.5 Rollback Strategy

**Frontend:**
- Vercel keeps deployment history
- Rollback via Vercel dashboard: Deployments → Previous → Promote

**Backend:**
- Railway/Render keeps deployment history
- Rollback via dashboard or redeploy previous commit

**Database:**
- Alembic downgrade: `alembic downgrade -1`
- Backup/restore (manual for hackathon, automated in production)

---

### 6.6 Feature Flags

**Not Implemented for Phase II** (hackathon scope)

**Future:** Use environment variables as simple flags:
```python
ENABLE_NEW_FEATURE = os.getenv("ENABLE_NEW_FEATURE", "false") == "true"
```

---

## 7. Risk Analysis and Mitigation

### Risk 1: Better Auth + FastAPI Integration Complexity

**Impact:** HIGH (could block entire auth flow)

**Probability:** MEDIUM

**Blast Radius:** Entire application (no auth = no app)

**Mitigation:**
- Study Better Auth JWT documentation thoroughly
- Create proof-of-concept before full integration
- Test JWT verification in isolation
- Have fallback: custom JWT implementation if Better Auth fails

**Kill Switch:** Revert to simple password-only auth (no JWT) if integration takes > 2 days

---

### Risk 2: CORS Issues Between Frontend and Backend

**Impact:** MEDIUM (API calls fail)

**Probability:** HIGH (common issue)

**Blast Radius:** All API functionality

**Mitigation:**
- Configure CORS early in FastAPI setup
- Test with real frontend requests immediately
- Use `allow_origins=["http://localhost:3000"]` in development
- Use specific origin (not `*`) in production

**Kill Switch:** Proxy backend through Next.js API routes if CORS can't be resolved

---

### Risk 3: Neon PostgreSQL Free Tier Limitations

**Impact:** LOW (can upgrade)

**Probability:** LOW (unlikely to hit limits in hackathon)

**Blast Radius:** Database performance only

**Mitigation:**
- Monitor database size and connection usage
- Use connection pooling (SQLModel default)
- Limit max connections to 5 concurrent
- Upgrade to paid tier if needed ($19/month acceptable for demo)

**Kill Switch:** Migrate to Supabase free tier (similar Postgres offering)

---

## 8. Evaluation and Validation

### 8.1 Definition of Done

A task is considered complete when:

**Code:**
- [ ] Code generated via Claude Code (no manual coding)
- [ ] TypeScript/Python type hints present
- [ ] No linting errors
- [ ] Code follows patterns in CLAUDE.md

**Functionality:**
- [ ] Feature works as specified in `spec.md`
- [ ] All acceptance criteria pass
- [ ] Error cases handled gracefully

**Testing:**
- [ ] Manual testing performed
- [ ] API endpoints tested with Postman/curl
- [ ] Frontend tested in Chrome and Firefox
- [ ] Mobile responsive (tested with DevTools)

**Documentation:**
- [ ] Environment variables documented in README
- [ ] API endpoints documented
- [ ] Setup instructions updated

**Deployment:**
- [ ] Works in development environment
- [ ] Works in production (Vercel + Railway/Render)

---

### 8.2 Output Validation

**Format Validation:**
- API responses match JSON schema
- HTTP status codes correct
- Error messages clear and actionable

**Requirements Validation:**
- All 6 user stories implemented
- All API endpoints functional
- Authentication working
- User data isolated

**Safety Validation:**
- No SQL injection (tested with malicious inputs)
- No XSS (tested with `<script>` tags)
- Passwords not logged
- JWT tokens not exposed in client console

---

## 9. Component Breakdown

### 9.1 Frontend Components (`frontend/`)

#### Core Layout
- `app/layout.tsx` - Root layout with auth provider
- `app/page.tsx` - Landing/login page
- `app/dashboard/page.tsx` - Main dashboard (task list)

#### Components
- `components/TaskList.tsx` - Display list of tasks
- `components/TaskItem.tsx` - Single task row with actions
- `components/AddTaskForm.tsx` - Form to create new task
- `components/EditTaskModal.tsx` - Modal to edit existing task
- `components/DeleteConfirmModal.tsx` - Confirmation dialog
- `components/Navbar.tsx` - Top navigation with logout

#### Utilities
- `lib/api.ts` - API client (fetch wrapper with auth)
- `lib/auth.ts` - Better Auth configuration
- `lib/types.ts` - TypeScript types (Task, User)

---

### 9.2 Backend Components (`backend/`)

#### Application Structure
- `app/main.py` - FastAPI app entry point, CORS config
- `app/db.py` - Database connection and session management
- `app/models.py` - SQLModel models (User, Task)
- `app/auth.py` - JWT verification, password hashing
- `app/dependencies.py` - FastAPI dependencies (get_current_user)

#### Routes
- `app/routes/auth.py` - Auth endpoints (login, register)
- `app/routes/tasks.py` - Task CRUD endpoints

#### Database
- `alembic/versions/` - Database migrations
- `alembic.ini` - Alembic configuration

---

## 10. Development Workflow

### Step-by-Step Implementation Order

**Phase 1: Setup (Tasks 1-3)**
1. Create monorepo structure
2. Initialize Next.js frontend
3. Initialize FastAPI backend

**Phase 2: Database (Tasks 4-6)**
4. Set up Neon PostgreSQL
5. Create SQLModel models
6. Create and run migrations

**Phase 3: Authentication (Tasks 7-10)**
7. Set up Better Auth in frontend
8. Implement JWT verification in backend
9. Create login/register UI
10. Test auth flow end-to-end

**Phase 4: API Implementation (Tasks 11-16)**
11. Implement GET /api/{user_id}/tasks
12. Implement POST /api/{user_id}/tasks
13. Implement PUT /api/{user_id}/tasks/{id}
14. Implement DELETE /api/{user_id}/tasks/{id}
15. Implement PATCH /api/{user_id}/tasks/{id}/complete
16. Test all endpoints with Postman

**Phase 5: Frontend Implementation (Tasks 17-22)**
17. Create dashboard page
18. Implement TaskList component
19. Implement AddTaskForm component
20. Implement task update functionality
21. Implement task delete functionality
22. Implement task completion toggle

**Phase 6: Polish & Deploy (Tasks 23-25)**
23. Add responsive styling (Tailwind CSS)
24. Deploy frontend to Vercel
25. Deploy backend to Railway/Render

---

### Testing Strategy

**Manual Testing Checklist:**
- [ ] User can register with email/password
- [ ] User can log in
- [ ] User can view their tasks
- [ ] User can add a task
- [ ] User can edit a task
- [ ] User can delete a task
- [ ] User can mark task complete/incomplete
- [ ] User A cannot see User B's tasks
- [ ] Session persists on page refresh
- [ ] Logout clears session
- [ ] Responsive on mobile (320px width)
- [ ] Responsive on desktop (1920px width)

**API Testing (Postman Collection):**
```json
{
  "info": {
    "name": "Todo API Phase II",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Auth",
      "item": [
        {"name": "Register", "request": {"method": "POST", "url": "{{baseUrl}}/api/auth/register"}},
        {"name": "Login", "request": {"method": "POST", "url": "{{baseUrl}}/api/auth/login"}}
      ]
    },
    {
      "name": "Tasks",
      "item": [
        {"name": "List Tasks", "request": {"method": "GET", "url": "{{baseUrl}}/api/{{userId}}/tasks"}},
        {"name": "Create Task", "request": {"method": "POST", "url": "{{baseUrl}}/api/{{userId}}/tasks"}},
        {"name": "Update Task", "request": {"method": "PUT", "url": "{{baseUrl}}/api/{{userId}}/tasks/1"}},
        {"name": "Delete Task", "request": {"method": "DELETE", "url": "{{baseUrl}}/api/{{userId}}/tasks/1"}},
        {"name": "Toggle Complete", "request": {"method": "PATCH", "url": "{{baseUrl}}/api/{{userId}}/tasks/1/complete"}}
      ]
    }
  ]
}
```

---

## 11. References

- Spec: `specs/phase-ii-web-app/spec.md`
- Hackathon PDF: Pages 7-16 (Phase II Requirements)
- Next.js Docs: https://nextjs.org/docs
- FastAPI Docs: https://fastapi.tiangolo.com
- SQLModel Docs: https://sqlmodel.tiangolo.com
- Better Auth Docs: https://www.better-auth.com/docs
- Neon Docs: https://neon.tech/docs

---

## Approval

This plan is ready for task breakdown when:
- [x] All architectural decisions documented
- [x] API contracts defined
- [x] Database schema designed
- [x] Component breakdown complete
- [x] Deployment strategy clear
- [x] Risks identified and mitigated

**Next Step:** Generate `tasks.md` using `/sp.tasks` command
