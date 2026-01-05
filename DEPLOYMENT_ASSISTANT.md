# 🚀 Deployment Assistant - Step-by-Step Guide

**Your Repository**: https://github.com/umernasir1/hackathon-ii-phase-i-todo-app

I'll help you deploy your application. Follow these steps carefully:

---

## 🔵 Step 1: Deploy Backend to Railway (10 minutes)

### 1.1 Login to Railway
1. Open: https://railway.app/login
2. Click **"Login with GitHub"**
3. Authorize Railway to access your repositories

### 1.2 Create New Project
1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Search for: `hackathon-ii-phase-i-todo-app`
4. Click on your repository

### 1.3 Configure Backend Service
1. Railway will detect your `railway.toml` configuration
2. Click **"Add variables"** or go to **Variables** tab
3. Add these environment variables:

```env
DATABASE_URL=postgresql://neondb_owner:npg_crCTIlG91iJR@ep-floral-bird-ahxuxm4r-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require
JWT_SECRET=a1fd210da153ee29b3595e54fe87dde55c9a24d213f9bc5f22f63b2bba5c54b8
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_DAYS=7
FRONTEND_URL=https://your-app.vercel.app
```

**Note**: You'll update `FRONTEND_URL` after deploying frontend (Step 2)

### 1.4 Configure Root Directory
1. Go to **Settings** tab
2. Under **Source**, set **Root Directory** to: `backend`
3. Railway will use the `railway.toml` for build/start commands

### 1.5 Deploy
1. Click **"Deploy"** or wait for automatic deployment
2. Deployment takes 2-3 minutes
3. Watch the logs for any errors

### 1.6 Get Your Backend URL
1. Go to **Settings** tab
2. Under **Networking**, click **"Generate Domain"**
3. Copy your domain (e.g., `your-app.up.railway.app`)
4. **SAVE THIS URL** - You'll need it for Step 2

### 1.7 Test Backend
Visit: `https://YOUR-BACKEND-URL/health`

You should see:
```json
{"status":"healthy"}
```

✅ **Backend deployed!** Copy your backend URL: ___________________________

---

## 🟢 Step 2: Deploy Frontend to Vercel (8 minutes)

### 2.1 Login to Vercel
1. Open: https://vercel.com/login
2. Click **"Continue with GitHub"**
3. Authorize Vercel

### 2.2 Import Project
1. Click **"Add New..."** → **"Project"**
2. Find: `hackathon-ii-phase-i-todo-app`
3. Click **"Import"**

### 2.3 Configure Project
1. **Framework Preset**: Next.js (auto-detected)
2. **Root Directory**: Click **"Edit"** → Enter: `frontend`
3. **Build Command**: `npm run build` (default)
4. **Output Directory**: `.next` (default)

### 2.4 Add Environment Variable
1. Scroll to **"Environment Variables"**
2. Add:
   - **Name**: `NEXT_PUBLIC_API_URL`
   - **Value**: `https://YOUR-BACKEND-URL` (from Step 1.6)
3. Click **"Add"**

### 2.5 Deploy
1. Click **"Deploy"**
2. Wait 2-3 minutes
3. Success screen with confetti! 🎉

### 2.6 Get Your Frontend URL
1. You'll see your deployment URL (e.g., `hackathon-ii-phase-i-todo-app.vercel.app`)
2. Click **"Visit"** to open your app
3. **SAVE THIS URL** - You'll need it for Step 3

✅ **Frontend deployed!** Your app URL: ___________________________

---

## 🔄 Step 3: Update Backend CORS (2 minutes)

### 3.1 Update Railway Environment Variable
1. Go back to Railway dashboard
2. Click on your backend service
3. Go to **Variables** tab
4. Find `FRONTEND_URL` variable
5. Update value to your Vercel URL: `https://your-app.vercel.app`
6. Click **"Save"** or press Enter

### 3.2 Redeploy Backend
1. Railway will automatically redeploy
2. Wait 1-2 minutes for completion
3. Check logs to ensure successful deployment

✅ **CORS updated!** Backend now accepts requests from your frontend.

---

## 🎯 Step 4: Test Your Live Application (5 minutes)

### 4.1 Open Your App
Visit: `https://your-app.vercel.app`

### 4.2 Test Registration
1. Click **"Sign Up"**
2. Enter email and password
3. Click **"Sign up"**
4. You should be redirected to dashboard

### 4.3 Test Task Management
1. ✅ **Add task**: Enter title/description, click "Add Task"
2. ✅ **View tasks**: Task appears in list
3. ✅ **Mark complete**: Click checkbox
4. ✅ **Edit task**: Click "Edit", modify, click "Save"
5. ✅ **Delete task**: Click "Delete", confirm

### 4.4 Test Multi-User
1. Logout
2. Create new account with different email
3. Verify tasks are separate

---

## 🎉 Success! Your App is LIVE!

### Your Deployment URLs:
- **Frontend**: https://___________________________
- **Backend API**: https://___________________________
- **API Docs**: https://___________________________/docs

---

## ❗ Troubleshooting

### Issue: "Failed to fetch" on frontend
**Solution**:
1. Verify `NEXT_PUBLIC_API_URL` in Vercel matches Railway backend URL
2. Verify `FRONTEND_URL` in Railway matches Vercel URL
3. Both must use `https://` (not `http://`)
4. Redeploy both services after changes

### Issue: Backend deployment fails
**Solution**:
1. Check Railway logs: **Deployments** → **View Logs**
2. Verify `DATABASE_URL` is correct (check Neon dashboard)
3. Ensure Root Directory is set to `backend`
4. Check that `railway.toml` exists in backend folder

### Issue: Frontend build fails
**Solution**:
1. Check Vercel logs: **Deployments** → **Function Logs**
2. Verify Root Directory is `frontend`
3. Verify `NEXT_PUBLIC_API_URL` is set correctly

### Issue: Database connection error
**Solution**:
1. Verify Neon database is active: https://console.neon.tech
2. Check `DATABASE_URL` ends with `?sslmode=require`
3. Test connection from Railway logs

---

## 📝 After Deployment Checklist

- [ ] Backend health check returns `{"status":"healthy"}`
- [ ] Frontend loads without errors
- [ ] Can register new user
- [ ] Can login with user
- [ ] Can add tasks
- [ ] Can mark tasks complete
- [ ] Can edit tasks
- [ ] Can delete tasks
- [ ] Different users see different tasks

---

**Once deployed, let me know and I'll help you test everything!**
