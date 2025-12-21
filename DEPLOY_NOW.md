# 🚀 Deploy Now - Step-by-Step Guide

Your code is pushed to GitHub! Now let's deploy it in 3 simple steps.

**Repository**: https://github.com/umernasir1/hackathon-ii-phase-i-todo-app

---

## Step 1: Deploy Backend to Railway (10 minutes)

### 1.1 Sign Up / Login to Railway
1. Go to: https://railway.app
2. Click "Login" and sign in with your GitHub account
3. Authorize Railway to access your GitHub repositories

### 1.2 Create New Project
1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Search for: `hackathon-ii-phase-i-todo-app`
4. Click on your repository to select it

### 1.3 Configure Backend Service
1. Railway will detect your repository
2. Click **"Add variables"** or go to the **Variables** tab
3. Add these environment variables (click "+ New Variable" for each):

```
DATABASE_URL=postgresql://neondb_owner:npg_crCTIlG91iJR@ep-floral-bird-ahxuxm4r-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require
JWT_SECRET=a1fd210da153ee29b3595e54fe87dde55c9a24d213f9bc5f22f63b2bba5c54b8
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_DAYS=7
FRONTEND_URL=https://your-app.vercel.app
```

**Note**: You'll update `FRONTEND_URL` after deploying the frontend in Step 2.

### 1.4 Configure Build Settings
1. Go to **Settings** tab
2. Set **Root Directory**: `backend`
3. Set **Build Command**: `pip install -r requirements.txt`
4. Set **Start Command**: `python -m alembic upgrade head && python -m uvicorn main:app --host 0.0.0.0 --port $PORT`

### 1.5 Deploy
1. Click **"Deploy"** or wait for automatic deployment
2. Deployment takes 2-3 minutes
3. Once deployed, you'll see a green checkmark ✅

### 1.6 Get Your Backend URL
1. Go to the **Settings** tab
2. Under **Domains**, click **"Generate Domain"**
3. Copy your domain (e.g., `your-app-production.up.railway.app`)
4. Your backend URL is: `https://your-app-production.up.railway.app`

### 1.7 Test Backend
Visit: `https://your-backend-url.up.railway.app/health`

You should see:
```json
{"status":"healthy"}
```

Also check: `https://your-backend-url.up.railway.app/docs` for API documentation.

---

## Step 2: Deploy Frontend to Vercel (8 minutes)

### 2.1 Sign Up / Login to Vercel
1. Go to: https://vercel.com
2. Click **"Sign Up"** or **"Login"**
3. Choose **"Continue with GitHub"**
4. Authorize Vercel to access your repositories

### 2.2 Import Project
1. Click **"Add New..."** → **"Project"**
2. Find your repository: `hackathon-ii-phase-i-todo-app`
3. Click **"Import"**

### 2.3 Configure Project
1. **Framework Preset**: Next.js (auto-detected)
2. **Root Directory**: Click **"Edit"** and type: `frontend`
3. **Build Command**: `npm run build` (default)
4. **Output Directory**: `.next` (default)

### 2.4 Add Environment Variable
1. Scroll down to **"Environment Variables"**
2. Add this variable:
   - **Name**: `NEXT_PUBLIC_API_URL`
   - **Value**: `https://your-backend-url.up.railway.app` (from Step 1.6)
   - Click **"Add"**

### 2.5 Deploy
1. Click **"Deploy"**
2. Deployment takes 2-3 minutes
3. You'll see a success screen with confetti! 🎉

### 2.6 Get Your Frontend URL
1. On the success screen, you'll see your deployment URL
2. It will look like: `https://hackathon-ii-phase-i-todo-app.vercel.app`
3. Click **"Visit"** to open your app

---

## Step 3: Update Backend CORS (2 minutes)

Now that you have your frontend URL, update the backend to allow requests from it:

### 3.1 Update Railway Environment Variable
1. Go back to Railway dashboard
2. Go to your backend service
3. Go to **Variables** tab
4. Find `FRONTEND_URL`
5. Update its value to your Vercel URL (e.g., `https://hackathon-ii-phase-i-todo-app.vercel.app`)
6. Click **"Save"**

### 3.2 Redeploy Backend
1. Railway will automatically redeploy after saving variables
2. Wait for deployment to complete (1-2 minutes)

---

## Step 4: Test Your Live App! (5 minutes)

### 4.1 Visit Your App
Go to your Vercel URL: `https://your-app.vercel.app`

### 4.2 Create Account
1. Click **"Sign Up"**
2. Enter your email and password
3. Click **"Sign up"**
4. You should be redirected to the dashboard

### 4.3 Test Features
1. ✅ **Add a task**: Enter title and description, click "Add Task"
2. ✅ **View tasks**: Your task should appear in the list
3. ✅ **Mark complete**: Click the checkbox to toggle completion
4. ✅ **Edit task**: Click "Edit", change the title, click "Save"
5. ✅ **Delete task**: Click "Delete", confirm deletion

### 4.4 Test Multi-User
1. Logout from your account
2. Create a new account with different email
3. Verify you don't see tasks from the first account
4. Create tasks in the new account
5. Verify they're separate from the first account

---

## Step 5: Update Your Repository (Optional)

Update your README with live URLs:

### 5.1 Edit README.md
Add this section at the top:

```markdown
## 🌐 Live Demo

**Frontend**: https://your-app.vercel.app
**Backend API**: https://your-backend.up.railway.app
**API Documentation**: https://your-backend.up.railway.app/docs

Try it now! Sign up and start managing your tasks.
```

### 5.2 Commit and Push
```bash
git add README.md
git commit -m "docs: Add live demo URLs"
git push origin main
```

---

## 🎉 Congratulations!

Your Phase II application is now LIVE on the internet! 🚀

### Your Deployment URLs
- **Frontend**: `https://______________________.vercel.app`
- **Backend**: `https://______________________.up.railway.app`

### What You've Accomplished
✅ Transformed a console app into a full-stack web application
✅ Implemented all 5 basic requirements
✅ Added user authentication and multi-user support
✅ Deployed to production (live on the internet!)
✅ Used modern tech stack (Next.js 16, FastAPI, PostgreSQL)

---

## Troubleshooting

### Issue: "Failed to fetch" on frontend
**Fix**:
1. Check that `NEXT_PUBLIC_API_URL` in Vercel matches your Railway backend URL
2. Make sure `FRONTEND_URL` in Railway matches your Vercel frontend URL
3. Verify both use `https://` (not `http://`)

### Issue: Backend shows "Database connection failed"
**Fix**:
1. Verify `DATABASE_URL` in Railway is correct
2. Make sure it ends with `?sslmode=require`
3. Check that your Neon database is active

### Issue: API returns 401 Unauthorized
**Fix**:
1. Clear browser localStorage (F12 → Application → Local Storage → Clear)
2. Try logging in again
3. Verify `JWT_SECRET` is set in Railway

### Issue: Build failed on Railway
**Fix**:
1. Check Railway logs for specific error
2. Verify `requirements.txt` has all dependencies
3. Make sure Python version in `runtime.txt` is 3.11.8

### Issue: Build failed on Vercel
**Fix**:
1. Check Vercel build logs
2. Verify `Root Directory` is set to `frontend`
3. Make sure `NEXT_PUBLIC_API_URL` is set

---

## Next Steps

Once deployed, you can:
1. Share your app URL with friends/colleagues
2. Add it to your portfolio/resume
3. Submit for hackathon evaluation
4. Continue adding features (see `PHASE_II_COMPLETE.md` for ideas)

---

## Support

If you encounter issues:
1. Check Railway logs: Dashboard → Deployments → View Logs
2. Check Vercel logs: Dashboard → Deployments → Function Logs
3. Check browser console: F12 → Console tab
4. Review `DEPLOYMENT.md` for detailed troubleshooting

---

**Deployment Guide Created**: 2025-12-21
**Estimated Time**: 25-30 minutes
**Status**: Ready to Deploy! 🚀
