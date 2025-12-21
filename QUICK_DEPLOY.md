# Quick Deploy Guide - Phase II

Get your Todo app deployed in under 30 minutes!

## Prerequisites Checklist

Before starting, make sure you have:
- [ ] GitHub account with this repository pushed
- [ ] Neon PostgreSQL database created (connection string ready)
- [ ] Accounts created on deployment platforms (Railway/Render + Vercel)

## ⚡ 5-Step Deployment

### Step 1: Deploy Backend (10 minutes)

#### Option A: Railway (Recommended)
1. Go to [railway.app](https://railway.app) and sign in with GitHub
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Add these environment variables:
   ```
   DATABASE_URL=<paste-your-neon-connection-string>
   JWT_SECRET=<generate-random-32-char-key>
   JWT_ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_DAYS=7
   FRONTEND_URL=https://your-app.vercel.app
   ```
5. Set Root Directory: `backend`
6. Railway will auto-deploy
7. Copy your backend URL (e.g., `https://your-app.up.railway.app`)

#### Option B: Render
1. Go to [render.com](https://render.com) and sign in
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - Name: `todo-backend`
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python -m alembic upgrade head && python -m uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add the same environment variables as above
6. Click "Create Web Service"
7. Copy your backend URL

### Step 2: Verify Backend (2 minutes)

Test your deployed backend:
```bash
curl https://your-backend-url.up.railway.app/health
```

Should return: `{"status":"healthy"}`

Also visit: `https://your-backend-url.up.railway.app/docs` to see API documentation.

### Step 3: Deploy Frontend (8 minutes)

1. Go to [vercel.com](https://vercel.com) and sign in with GitHub
2. Click "Add New..." → "Project"
3. Import your GitHub repository
4. Configure:
   - Framework Preset: Next.js
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `.next`
5. Add environment variable:
   ```
   NEXT_PUBLIC_API_URL=https://your-backend-url.up.railway.app
   ```
   (Use the backend URL from Step 1)
6. Click "Deploy"
7. Wait for deployment to complete (2-3 minutes)
8. Copy your frontend URL (e.g., `https://your-app.vercel.app`)

### Step 4: Update Backend CORS (2 minutes)

Go back to your backend deployment (Railway/Render):
1. Update the `FRONTEND_URL` environment variable
2. Change from `https://your-app.vercel.app` to your actual Vercel URL
3. Trigger a redeploy

### Step 5: Test Production App (5 minutes)

1. Visit your Vercel URL: `https://your-app.vercel.app`
2. Click "Sign Up" and create an account
3. You should be redirected to dashboard
4. Try adding a task
5. Try editing and deleting tasks
6. Logout and login again

If everything works: **🎉 Congratulations! Your app is live!**

## Common Issues & Fixes

### Issue: Backend shows "Database connection failed"
**Fix:** Check your `DATABASE_URL` in backend environment variables. Make sure it includes `?sslmode=require` at the end.

### Issue: Frontend can't connect to backend
**Fix:**
1. Check `NEXT_PUBLIC_API_URL` in Vercel
2. Make sure CORS is configured correctly in backend (`FRONTEND_URL` env var)
3. Verify both URLs use HTTPS

### Issue: "Token expired" errors
**Fix:** Make sure `JWT_SECRET` is the same value in both frontend and backend (if using Better Auth).

### Issue: Alembic migration fails on backend
**Fix:**
1. Check that `DATABASE_URL` is correct
2. Make sure Neon database is active
3. Try running migrations manually: `python -m alembic upgrade head`

## Environment Variable Reference

### Backend Required Variables
```bash
DATABASE_URL=postgresql://user:password@host/database?sslmode=require
JWT_SECRET=your-secret-key-min-32-chars
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_DAYS=7
FRONTEND_URL=https://your-frontend.vercel.app
```

### Frontend Required Variables
```bash
NEXT_PUBLIC_API_URL=https://your-backend.up.railway.app
```

## Generate JWT Secret

**On Linux/Mac:**
```bash
openssl rand -hex 32
```

**On Windows PowerShell:**
```powershell
-join ((48..57) + (65..70) | Get-Random -Count 64 | % {[char]$_})
```

**Online:**
Visit [random.org/strings](https://www.random.org/strings/?num=1&len=64&digits=on&upperalpha=on&loweralpha=on&unique=on&format=html&rnd=new)

## Post-Deployment Checklist

After deployment, verify:
- [ ] Backend health check works: `/health`
- [ ] Backend API docs accessible: `/docs`
- [ ] Frontend loads without errors
- [ ] User registration works
- [ ] User login works
- [ ] Tasks can be created
- [ ] Tasks can be viewed
- [ ] Tasks can be updated
- [ ] Tasks can be deleted
- [ ] Logout works

## Update Your Repository

After successful deployment, update your README.md with live URLs:

```markdown
## Live Demo

- **Frontend**: https://your-app.vercel.app
- **Backend API**: https://your-backend.up.railway.app
- **API Docs**: https://your-backend.up.railway.app/docs
```

## Need Help?

1. Check [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed instructions
2. Review [TESTING_CHECKLIST.md](./TESTING_CHECKLIST.md)
3. Check deployment platform logs for errors
4. Verify all environment variables are set correctly

---

**Estimated Total Time**: 25-30 minutes
**Difficulty**: Beginner-friendly
**Cost**: $0 (all platforms have free tiers)
