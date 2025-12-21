# Local Testing Guide

Follow these steps to test the application locally before deployment.

## Prerequisites Checklist

- [ ] Python 3.11+ installed (`python --version`)
- [ ] Node.js 18+ installed (`node --version`)
- [ ] Neon PostgreSQL database created
- [ ] Database connection string copied

## Step 1: Configure Backend

1. **Edit backend/.env file**:
   ```bash
   # Open backend/.env in your text editor
   # Replace the DATABASE_URL with your Neon connection string
   ```

   Your `.env` should look like:
   ```env
   DATABASE_URL=postgresql://user:password@ep-xxx.neon.tech/neondb?sslmode=require
   JWT_SECRET=dev-secret-key-change-in-production-use-openssl-rand-hex-32
   JWT_ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_DAYS=7
   FRONTEND_URL=http://localhost:3000
   ```

2. **Generate a secure JWT secret** (optional but recommended):
   ```bash
   # Option 1: Using OpenSSL
   openssl rand -hex 32

   # Option 2: Using Python
   python -c "import secrets; print(secrets.token_hex(32))"

   # Copy the output and replace JWT_SECRET in .env
   ```

## Step 2: Set Up Backend

```bash
# Navigate to backend directory
cd backend

# Install dependencies (if not already installed)
pip install -r requirements.txt

# Run database migrations
python -m alembic upgrade head
```

**Expected output**:
```
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> xxxxx, Initial migration
```

## Step 3: Start Backend Server

```bash
# Still in backend directory
python -m uvicorn main:app --reload --port 8000
```

**Expected output**:
```
INFO:     Will watch for changes in these directories: ['...']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [xxxxx] using WatchFiles
INFO:     Started server process [xxxxx]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**Test backend health** (in a new terminal):
```bash
curl http://localhost:8000/health
# Should return: {"status":"healthy"}
```

**View API documentation**:
Open browser to: http://localhost:8000/docs

## Step 4: Configure Frontend

```bash
# Open a NEW terminal window
cd frontend

# Verify .env.local exists and contains:
# NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Step 5: Start Frontend Server

```bash
# Still in frontend directory
npm run dev
```

**Expected output**:
```
  ▲ Next.js 16.0.10
  - Local:        http://localhost:3000
  - Environments: .env.local

 ✓ Starting...
 ✓ Ready in 2.3s
```

## Step 6: Test the Application

1. **Open browser** to http://localhost:3000

2. **Sign up for an account**:
   - Click "Sign Up"
   - Email: test@example.com
   - Password: test123
   - Click "Sign up"
   - You should be redirected to dashboard

3. **Add a task**:
   - Title: "Test task"
   - Description: "This is a test"
   - Click "Add Task"
   - Task should appear in list

4. **Test task operations**:
   - [ ] Click checkbox to mark complete
   - [ ] Click "Edit" and modify the task
   - [ ] Click "Delete" to remove the task

5. **Test authentication**:
   - Click "Logout"
   - Click "Login"
   - Use same credentials
   - Should see your tasks again

## Verification Checklist

### Backend
- [ ] Server starts without errors
- [ ] Health endpoint returns {"status":"healthy"}
- [ ] API docs accessible at /docs
- [ ] Database connection successful
- [ ] Migrations applied successfully

### Frontend
- [ ] Server starts without errors
- [ ] Landing page loads
- [ ] Sign up works
- [ ] Login works
- [ ] Dashboard loads
- [ ] Can add tasks
- [ ] Can view tasks
- [ ] Can mark tasks complete
- [ ] Can edit tasks
- [ ] Can delete tasks
- [ ] Logout works

### Database
- [ ] Users table created
- [ ] Tasks table created
- [ ] Can register new users
- [ ] Can create tasks
- [ ] Data persists across page refreshes

## Common Issues & Solutions

### Backend Issues

**"ModuleNotFoundError: No module named 'fastapi'"**
```bash
cd backend
pip install -r requirements.txt
```

**"could not connect to server: Connection refused"**
- Check DATABASE_URL in .env is correct
- Verify Neon database is active
- Ensure connection string has ?sslmode=require

**"relation 'users' does not exist"**
```bash
cd backend
python -m alembic upgrade head
```

### Frontend Issues

**"Cannot connect to backend"**
- Verify backend is running on port 8000
- Check .env.local has correct NEXT_PUBLIC_API_URL
- Check browser console for CORS errors

**"Module not found" errors**
```bash
cd frontend
npm install
```

**Build errors**
```bash
cd frontend
rm -rf .next node_modules
npm install
npm run dev
```

## Success Criteria

If all checks pass, your application is working correctly locally!

You should be able to:
1. ✅ Register a new account
2. ✅ Login with credentials
3. ✅ Create tasks
4. ✅ View tasks
5. ✅ Mark tasks complete/incomplete
6. ✅ Edit tasks
7. ✅ Delete tasks
8. ✅ Logout and login again
9. ✅ See tasks persist across sessions

## Next Steps

Once local testing is complete, we'll proceed with deployment to:
- Frontend: Vercel
- Backend: Railway or Render
- Database: Already on Neon

See DEPLOYMENT.md for production deployment steps.
