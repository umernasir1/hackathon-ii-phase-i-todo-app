# 🚀 Deploy to Koyeb - Complete Step-by-Step Guide

**Last Updated**: December 28, 2025
**Platform**: Koyeb (Backend) + Vercel (Frontend)
**Cost**: 100% FREE - No credit card required!
**Time**: 15-20 minutes

---

## ✅ Why Koyeb Works Best

- ✅ **100% FREE** - No credit card required
- ✅ **No database restrictions** - Works with Neon PostgreSQL
- ✅ **FastAPI native support** - No code changes needed
- ✅ **Always on** - No spin-down delays
- ✅ **Easy GitHub deployment**
- ✅ **Automatic HTTPS**

---

## 🎯 IMPORTANT: Service Naming Rules

**Before you start**, understand Koyeb's naming rules to avoid errors:

### ✅ **Valid Names:**
- All lowercase letters: `todoapi` ✅
- With numbers: `todo2024` ✅
- With hyphens (NOT at start/end): `todo-api` ✅
- Simple words: `backend`, `phaseii`, `hackathon` ✅

### ❌ **Invalid Names:**
- Capital letters: `TodoAPI` ❌
- Underscores: `todo_api` ❌
- Spaces: `todo api` ❌
- Starting with hyphen: `-todoapi` ❌
- Ending with hyphen: `todoapi-` ❌
- Special characters: `todo.api`, `todo@api` ❌

### 💡 **Recommended Names to Use:**

Pick one of these (guaranteed to work):
```
todoapi
phaseii-backend
hackathon-todo
backend-phaseii
my-todo-api
fastapi-backend
```

---

## Part 1: Deploy Backend to Koyeb 🚀

### Step 1: Create Koyeb Account (2 minutes)

1. Go to **https://www.koyeb.com/**
2. Click **"Sign up"** (top right)
3. Click **"Continue with GitHub"**
4. Click **"Authorize Koyeb"** when prompted
5. ✅ You're logged in! No credit card asked!

### Step 2: Create New App

1. You'll see the Koyeb dashboard
2. Click **"Create App"** button (or "Create Web Service")
3. You'll see deployment options

### Step 3: Select Deployment Method

1. Click **"GitHub"** (under "Deploy from")
2. If first time, click **"Connect GitHub account"**
3. Authorize Koyeb to access your repositories
4. You'll see a list of your repositories

### Step 4: Select Your Repository

1. Find: `hackathon-ii-phase-i-todo-app`
2. Click on it to select
3. Click **"Next"** or **"Configure"**

### Step 5: Configure Build Settings ⚠️ CRITICAL

This is the most important step!

#### **Service Name:**
Enter: `todoapi` (or pick from recommended names above)
- ⚠️ All lowercase
- ⚠️ No underscores or spaces
- ⚠️ No capital letters

#### **Region:**
Choose closest to you:
- `Washington, D.C. (US East)`
- `Frankfurt (Europe)`
- `Singapore (Asia)`

#### **Branch:**
Select: `main`

#### **Builder:**
Select: **"Buildpack"** (or "Dockerfile" if you prefer)

#### **Root Path / Working Directory:**
⚠️ **CRITICAL** - Enter exactly: `backend`
- This tells Koyeb where your backend code is
- Must be exactly `backend` (lowercase, no slashes)

### Step 6: Configure Build Commands

Koyeb should auto-detect Python, but verify:

#### **Build Command:**
```bash
pip install -r requirements.txt
```

#### **Run Command:**
```bash
alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port $PORT
```

**Alternative Run Command** (if migrations fail):
```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

(You can run migrations manually later if needed)

### Step 7: Set Environment Variables ⚠️ CRITICAL

Scroll to **"Environment Variables"** section.

Click **"Add Variable"** for each:

**Variable 1:**
- **Name**: `DATABASE_URL`
- **Value**:
  ```
  postgresql://neondb_owner:npg_crCTIlG91iJR@ep-floral-bird-ahxuxm4r-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require
  ```

**Variable 2:**
- **Name**: `JWT_SECRET`
- **Value**:
  ```
  a1fd210da153ee29b3595e54fe87dde55c9a24d213f9bc5f22f63b2bba5c54b8
  ```

**Variable 3:**
- **Name**: `JWT_ALGORITHM`
- **Value**: `HS256`

**Variable 4:**
- **Name**: `ACCESS_TOKEN_EXPIRE_DAYS`
- **Value**: `7`

**Variable 5:**
- **Name**: `FRONTEND_URL`
- **Value**: `http://localhost:3000`
  (We'll update this after deploying frontend)

**Variable 6:**
- **Name**: `PORT`
- **Value**: `8000`

### Step 8: Select Instance Type

Scroll to **"Instance"** or **"Resources"** section:

- **Instance Type**: Select **"Free"** or **"Eco"**
- **Scaling**: Set to `1` instance (minimum)
- **Auto-scaling**: Leave off (not needed for free tier)

### Step 9: Review and Deploy

1. Review all settings:
   - ✅ Service name (lowercase, no underscores)
   - ✅ Root path: `backend`
   - ✅ All 6 environment variables set
   - ✅ Build and run commands correct
   - ✅ Free instance selected

2. Click **"Deploy"** or **"Create Service"** button

### Step 10: Watch Deployment (3-5 minutes)

1. You'll see the deployment logs in real-time
2. Watch for these stages:
   - 🔵 "Fetching code from GitHub..."
   - 🔵 "Installing dependencies..."
   - 🔵 "Running migrations..." (if included in run command)
   - 🔵 "Starting server..."
   - ✅ "Healthy" or "Running"

3. Look for success messages:
   ```
   ✓ Application started successfully
   ✓ Listening on port 8000
   ✓ Deployment is healthy
   ```

### Step 11: Get Your Backend URL

Once deployment shows **"Healthy"** or **"Running"**:

1. Your URL will be displayed at the top
2. Format: `https://todoapi-YOUR-ID.koyeb.app`
3. **Copy this URL** - you'll need it for frontend!

Example: `https://todoapi-abc123def.koyeb.app`

### Step 12: Test Backend Deployment

Open these URLs in your browser:

#### **Health Check:**
```
https://your-service-name.koyeb.app/health
```

Should return:
```json
{"status": "healthy"}
```

#### **API Documentation:**
```
https://your-service-name.koyeb.app/docs
```

Should show Swagger UI with all your API endpoints!

#### **Root Endpoint:**
```
https://your-service-name.koyeb.app/
```

Should return API info.

✅ **If all three work, your backend is LIVE!** 🎉

---

## Part 2: Deploy Frontend to Vercel 🎨

### Step 1: Create Vercel Account (FREE)

1. Go to **https://vercel.com**
2. Click **"Sign Up"**
3. Choose **"Continue with GitHub"**
4. Authorize Vercel
5. ✅ No credit card required!

### Step 2: Import Project

1. Click **"Add New..."** → **"Project"**
2. Find: `hackathon-ii-phase-i-todo-app`
3. Click **"Import"**

### Step 3: Configure Project

#### **Framework Preset:**
- Should auto-detect: **"Next.js"** ✅

#### **Root Directory:**
⚠️ **CRITICAL**
1. Click **"Edit"** button next to "Root Directory"
2. Enter: `frontend`
3. Click checkmark to save

#### **Build Settings:**
Leave defaults (should be pre-filled):
- **Framework**: Next.js
- **Build Command**: `npm run build`
- **Output Directory**: `.next`
- **Install Command**: `npm install`

### Step 4: Add Environment Variable

Click **"Environment Variables"** section (expand if collapsed):

**Add this variable:**
- **Name**: `NEXT_PUBLIC_API_URL`
- **Value**: `https://your-koyeb-url.koyeb.app`
  - ⚠️ Use YOUR actual Koyeb URL from Step 11 above
  - Must start with `https://`
  - NO trailing slash
  - NO `/api` path

**Example:**
```
Name: NEXT_PUBLIC_API_URL
Value: https://todoapi-abc123def.koyeb.app
```

- **Environment**: Check all three:
  - ✅ Production
  - ✅ Preview
  - ✅ Development

### Step 5: Deploy Frontend

1. Click **"Deploy"** button
2. Vercel will start building (2-4 minutes)
3. Watch the build logs
4. Wait for **"Building"** → **"Completed"**

### Step 6: Get Your Frontend URL

Once deployed:
1. You'll see: **"Congratulations!"** 🎉
2. Your URL will be shown (e.g., `https://hackathon-ii-phase-i-todo-app.vercel.app`)
3. Click **"Visit"** to see your live app
4. **Copy this URL** - you need it for next step

### Step 7: Update Backend CORS

Now update your backend to allow your Vercel frontend:

1. Go back to **Koyeb dashboard**
2. Click on your backend service
3. Click **"Settings"** tab
4. Click **"Environment variables"**
5. Find `FRONTEND_URL`
6. Click **"Edit"** (pencil icon)
7. Change value to your Vercel URL:
   ```
   https://your-app.vercel.app
   ```
   (Use YOUR actual Vercel URL)
8. Click **"Save"**
9. Koyeb will automatically redeploy (1-2 minutes)
10. Wait for **"Healthy"** status again

✅ **Both frontend and backend are now LIVE!** 🎉

---

## Part 3: Test End-to-End Deployment 🧪

### Test Checklist - Do All 8 Tests:

Visit your Vercel URL: `https://your-app.vercel.app`

#### ✅ Test 1: Landing Page
- Page loads without errors
- See login/signup buttons

#### ✅ Test 2: User Registration
1. Click **"Sign Up"**
2. Enter test credentials:
   - Email: `test@example.com`
   - Password: `testpassword123`
3. Click **"Sign Up"**
4. Should redirect to dashboard

#### ✅ Test 3: Add Task
1. In dashboard, enter task:
   - Title: "Deploy Phase II"
   - Description: "Testing Koyeb deployment"
2. Click **"Add Task"**
3. Task appears in list

#### ✅ Test 4: Mark Complete
1. Click checkbox next to your task
2. Task shows as completed (strikethrough)

#### ✅ Test 5: Edit Task
1. Click **"Edit"** button
2. Change title to "Deployment successful!"
3. Click **"Save"**
4. Task updates

#### ✅ Test 6: Delete Task
1. Click **"Delete"** button
2. Confirm deletion
3. Task disappears

#### ✅ Test 7: Logout and Login
1. Click **"Logout"**
2. Redirects to login page
3. Log back in with same credentials
4. See dashboard again

#### ✅ Test 8: API Documentation
Visit: `https://your-koyeb-url.koyeb.app/docs`
- Swagger UI loads
- All endpoints listed

---

## 🎉 Success! Phase II Complete!

If all 8 tests passed, your application is **FULLY DEPLOYED!**

### Your Live URLs:

**Frontend (Vercel):**
```
https://your-app.vercel.app
```

**Backend (Koyeb):**
```
https://todoapi-xyz.koyeb.app
```

**API Docs:**
```
https://todoapi-xyz.koyeb.app/docs
```

---

## 📊 Platform Features (Free Tier)

### Koyeb Free Tier:
- ✅ 1 web service
- ✅ Always on (no sleep)
- ✅ 512MB RAM
- ✅ Shared CPU
- ✅ Auto HTTPS/SSL
- ✅ Git auto-deploy

### Vercel Free Tier:
- ✅ Unlimited projects
- ✅ 100GB bandwidth/month
- ✅ Fast global CDN
- ✅ Always on
- ✅ Auto deployments

---

## 🐛 Troubleshooting

### Backend Build Fails

**Error: "Service name invalid"**
- **Fix**: Use only lowercase letters, numbers, hyphens
- Try: `todoapi` (simple, works every time)

**Error: "requirements.txt not found"**
- **Fix**: Check Root Path is set to `backend`
- Verify in Settings → General → Root Path

**Error: "Port binding failed"**
- **Fix**: Ensure Run Command uses `$PORT` variable
- Command should include: `--port $PORT`

**Error: "Database connection failed"**
- **Fix**: Verify `DATABASE_URL` has `?sslmode=require`
- Check all environment variables are set correctly

### Frontend Build Fails

**Error: "Build failed"**
- **Fix**: Verify Root Directory is `frontend`
- Check in Project Settings

**Error: "NEXT_PUBLIC_API_URL not found"**
- **Fix**: Add environment variable in Vercel
- Must start with `https://`
- No trailing slash

### Runtime Errors

**CORS Error in Browser**
- **Fix**: Update `FRONTEND_URL` in Koyeb backend
- Must match your Vercel URL exactly
- Redeploy backend after changing

**502 Bad Gateway**
- **Fix**: Check Koyeb logs for errors
- Verify service is "Healthy"
- May need to restart service

**Can't Register/Login**
- **Fix**: Check browser console for errors
- Verify API URL in frontend env vars
- Test backend `/docs` endpoint works

---

## 🔄 Updating Your Deployment

### When You Make Code Changes:

**Backend Updates:**
1. Commit and push to GitHub
2. Koyeb automatically detects and redeploys
3. Watch deployment logs in Koyeb dashboard
4. Wait for "Healthy" status

**Frontend Updates:**
1. Commit and push to GitHub
2. Vercel automatically detects and redeploys
3. Check Vercel dashboard for status
4. Usually completes in 1-2 minutes

**Database Migrations:**
If you add new models:
1. Create migration locally
2. Commit and push
3. Koyeb will run `alembic upgrade head` on deploy
4. Check logs to verify migration succeeded

---

## 💡 Pro Tips

### Viewing Logs:
- **Koyeb**: Dashboard → Your Service → Logs tab
- **Vercel**: Project → Deployments → Click deployment → View logs

### Redeploying:
- **Koyeb**: Settings → Redeploy button
- **Vercel**: Deployments → Three dots → Redeploy

### Environment Variable Changes:
- Always redeploy after changing env vars
- Changes don't take effect until redeployment

### Database Changes:
- Test migrations locally first
- Always backup data before major schema changes
- Use Neon dashboard to check database state

---

## 🎓 What You've Accomplished

✅ Full-stack application deployed to production
✅ FastAPI backend on Koyeb (free, always on)
✅ Next.js frontend on Vercel (free, global CDN)
✅ PostgreSQL database on Neon (free, serverless)
✅ JWT authentication working
✅ Complete CRUD operations
✅ Responsive design (mobile + desktop)
✅ Automatic HTTPS on both platforms
✅ Git-based auto deployments
✅ **Zero cost - completely free!**

---

## 📝 Final Checklist

Before marking Phase II complete:

- [ ] Backend deployed to Koyeb
- [ ] Backend health check returns `{"status":"healthy"}`
- [ ] Backend `/docs` shows API documentation
- [ ] Frontend deployed to Vercel
- [ ] Frontend loads without errors
- [ ] Can register new user
- [ ] Can login
- [ ] Can add tasks
- [ ] Can mark tasks complete
- [ ] Can edit tasks
- [ ] Can delete tasks
- [ ] Can logout and login again
- [ ] CORS working (no browser errors)
- [ ] All 8 tests passed
- [ ] URLs documented

---

## 🆘 Still Having Issues?

### Check These First:
1. ✅ Service name is all lowercase (no capitals!)
2. ✅ Root path set to `backend` in Koyeb
3. ✅ Root directory set to `frontend` in Vercel
4. ✅ All 6 environment variables in Koyeb
5. ✅ `NEXT_PUBLIC_API_URL` in Vercel
6. ✅ `FRONTEND_URL` updated in Koyeb after Vercel deployment

### Common Mistakes:
- ❌ Capital letters in service name
- ❌ Forgetting to set root path/directory
- ❌ Trailing slash in API URL
- ❌ Not updating FRONTEND_URL after Vercel deployment
- ❌ Missing environment variables

### Where to Get Help:
- **Koyeb Docs**: https://www.koyeb.com/docs
- **Koyeb Community**: https://community.koyeb.com
- **Vercel Docs**: https://vercel.com/docs

---

## 🎉 Congratulations!

You've successfully deployed a production-ready full-stack application!

**What's Next?**
- Share your live URLs with others
- Test with multiple users
- Add to your portfolio
- Continue to Phase III (if applicable)

---

**Ready to start?** Begin with Part 1, Step 1: Create Koyeb Account! 🚀

**Questions?** Follow each step carefully and let me know if you get stuck at any point!
