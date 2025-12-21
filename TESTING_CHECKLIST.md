# Phase II Testing Checklist

Complete this checklist before considering Phase II done.

## ✅ Local Development Testing

### Backend API Tests
- [ ] **Health Check**: GET `/health` returns `{"status": "healthy"}`
- [ ] **API Documentation**: GET `/docs` displays Swagger UI
- [ ] **Database Connection**: Backend can connect to Neon PostgreSQL
- [ ] **Migrations**: Alembic migrations applied successfully

### Authentication Tests
- [ ] **Register User**: POST `/auth/register` creates new user
- [ ] **Register Duplicate**: POST `/auth/register` with existing email returns 400
- [ ] **Login Success**: POST `/auth/login` with valid credentials returns JWT token
- [ ] **Login Failure**: POST `/auth/login` with wrong password returns 401
- [ ] **Token Validation**: Protected endpoints reject invalid/missing tokens

### Task CRUD Tests
- [ ] **Create Task**: POST `/api/{user_id}/tasks` creates task
- [ ] **List Tasks**: GET `/api/{user_id}/tasks` returns user's tasks only
- [ ] **Get Task**: GET `/api/{user_id}/tasks/{id}` returns specific task
- [ ] **Update Task**: PUT `/api/{user_id}/tasks/{id}` updates task
- [ ] **Delete Task**: DELETE `/api/{user_id}/tasks/{id}` removes task
- [ ] **Mark Complete**: Task completion toggle works

### Authorization Tests
- [ ] **User Isolation**: User A cannot access User B's tasks (returns 403)
- [ ] **Path Validation**: user_id in path must match JWT user_id
- [ ] **Public Endpoints**: `/auth/register` and `/auth/login` work without token

### Validation Tests
- [ ] **Title Required**: Creating task without title returns 400
- [ ] **Title Length**: Title > 200 chars returns 400
- [ ] **Description Length**: Description > 1000 chars returns 400
- [ ] **Email Format**: Invalid email format returns 400

### Frontend UI Tests
- [ ] **Landing Page**: `/` loads without errors
- [ ] **Login Page**: `/login` displays login form
- [ ] **Signup Page**: `/signup` displays registration form
- [ ] **Dashboard**: `/dashboard` requires authentication
- [ ] **Logout**: Logout button clears session and redirects

### Frontend Integration Tests
- [ ] **Register Flow**: User can register and is auto-logged in
- [ ] **Login Flow**: User can login and sees dashboard
- [ ] **Add Task**: User can create task via UI
- [ ] **View Tasks**: Dashboard displays all user's tasks
- [ ] **Edit Task**: User can update task title/description
- [ ] **Delete Task**: User can delete task with confirmation
- [ ] **Toggle Complete**: Checkbox marks task complete/pending
- [ ] **Session Persistence**: Refreshing page maintains login state

### Responsive Design Tests
- [ ] **Mobile (320px)**: All pages usable on iPhone SE size
- [ ] **Tablet (768px)**: Optimal layout on iPad size
- [ ] **Desktop (1920px)**: Full features visible on large screens
- [ ] **No Horizontal Scroll**: All viewports prevent horizontal scrolling

### Error Handling Tests
- [ ] **Network Error**: UI shows error message if backend unreachable
- [ ] **Form Validation**: Client-side validation shows errors before submission
- [ ] **API Errors**: Backend error messages displayed to user
- [ ] **Loading States**: Spinners/loading indicators during async operations

## 🚀 Deployment Testing

### Backend Deployment
- [ ] **Platform**: Deployed to Railway/Render/Fly.io
- [ ] **Public URL**: Backend accessible via HTTPS
- [ ] **Environment Variables**: All env vars configured correctly
- [ ] **Database Migrations**: Alembic migrations run on deployed database
- [ ] **Health Check**: Production `/health` endpoint returns 200
- [ ] **CORS**: Backend allows requests from frontend domain
- [ ] **Logs**: No errors in deployment logs

### Frontend Deployment
- [ ] **Platform**: Deployed to Vercel
- [ ] **Public URL**: Frontend accessible via HTTPS
- [ ] **Environment Variables**: `NEXT_PUBLIC_API_URL` points to backend
- [ ] **Build Success**: Next.js production build completes without errors
- [ ] **Pages Load**: All routes (/, /login, /signup, /dashboard) accessible
- [ ] **API Connection**: Frontend can communicate with backend

### End-to-End Production Tests
- [ ] **Full Registration Flow**: Register new user in production
- [ ] **Full Login Flow**: Login with production credentials
- [ ] **Create Task in Production**: Add task via production UI
- [ ] **View Tasks in Production**: Tasks display correctly
- [ ] **Update Task in Production**: Edit task successfully
- [ ] **Delete Task in Production**: Remove task successfully
- [ ] **Multi-User Test**: Two users cannot see each other's tasks

## 📊 Performance Tests
- [ ] **API Response Time**: All endpoints respond < 500ms
- [ ] **Page Load Time**: Dashboard loads < 2s
- [ ] **Build Size**: Frontend bundle size reasonable
- [ ] **Lighthouse Score**: Performance > 80 (run in incognito)

## 🔒 Security Tests
- [ ] **Password Hashing**: Passwords stored as bcrypt hashes (not plaintext)
- [ ] **JWT Expiration**: Tokens expire after configured time (7 days)
- [ ] **HTTPS**: Both frontend and backend use HTTPS in production
- [ ] **Environment Secrets**: No secrets committed to git
- [ ] **SQL Injection**: SQLModel prevents SQL injection (parameterized queries)
- [ ] **XSS Protection**: User inputs sanitized

## 📝 Documentation Tests
- [ ] **README**: Updated with Phase II information
- [ ] **README URLs**: Contains production frontend and backend URLs
- [ ] **Setup Instructions**: Backend README has clear setup steps
- [ ] **API Documentation**: Swagger docs accessible at `/docs`
- [ ] **Deployment Guide**: DEPLOYMENT.md complete and accurate
- [ ] **Environment Templates**: `.env.example` files exist and are complete

## 🎯 Requirements Compliance

### Functional Requirements (All 5)
- [ ] **FR-1: Add Tasks** - Users can add tasks via web interface
- [ ] **FR-2: View Tasks** - Users can see all their tasks in dashboard
- [ ] **FR-3: Mark Complete** - Users can toggle task completion
- [ ] **FR-4: Update Tasks** - Users can edit task title/description
- [ ] **FR-5: Delete Tasks** - Users can remove tasks

### Additional Phase II Requirements
- [ ] **User Authentication**: Registration and login working
- [ ] **Multi-User Support**: Data isolation between users
- [ ] **Persistent Storage**: PostgreSQL database stores all data
- [ ] **RESTful API**: Backend provides proper REST endpoints
- [ ] **Responsive Design**: Works on mobile and desktop

### Technical Constraints
- [ ] **Next.js 16+**: Frontend uses Next.js 16 with App Router
- [ ] **FastAPI**: Backend uses FastAPI framework
- [ ] **SQLModel**: ORM is SQLModel
- [ ] **Neon PostgreSQL**: Database is Neon serverless PostgreSQL
- [ ] **TypeScript**: Frontend uses TypeScript
- [ ] **JWT**: Authentication uses JWT tokens

## 🏁 Final Verification

### Before Marking Phase II Complete
- [ ] All functional requirements met
- [ ] All technical constraints satisfied
- [ ] Both frontend and backend deployed
- [ ] Production URLs documented
- [ ] End-to-end flow works in production
- [ ] No critical bugs
- [ ] Code committed to git
- [ ] README updated with deployment info

## 📊 Completion Status

- **Total Tests**: 90+
- **Passed**: ___
- **Failed**: ___
- **Skipped**: ___

## Notes

Record any issues, bugs, or observations during testing:

---

**Last Updated**: 2025-12-21
**Tested By**: ___________
**Environment**: Local / Production
**Status**: 🟡 In Progress / ✅ Complete
