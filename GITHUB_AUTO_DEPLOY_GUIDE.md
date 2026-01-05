# 🚀 One-Click GitHub Auto-Deploy Setup

**Setup Time**: 20 minutes
**After Setup**: Every push to GitHub automatically deploys!

Your Repository: https://github.com/umernasir1/hackathon-ii-phase-i-todo-app

---

## ✅ What's Already Ready

Your project is **100% configured** for deployment:
- ✅ `railway.toml` - Railway configuration
- ✅ `Dockerfile` - Container configuration
- ✅ `Procfile` - Process configuration
- ✅ `requirements.txt` - Python dependencies
- ✅ `runtime.txt` - Python version (3.11)
- ✅ `vercel.json` - Vercel configuration
- ✅ `package.json` - Frontend dependencies
- ✅ All code pushed to GitHub

**You just need to connect the platforms!**

---

## 🔵 Part 1: Railway Backend Setup (10 minutes)

### Step 1: Login to Railway
1. Visit: **https://railway.app/login**
2. Click **"Login with GitHub"**
3. Authorize Railway (if first time)

### Step 2: Create New Project from GitHub
1. Click **"New Project"** button (top right)
2. Select **"Deploy from GitHub repo"**
3. You'll see a list of your repositories
4. Find and click: **`hackathon-ii-phase-i-todo-app`**

### Step 3: Configure Service
Railway will automatically detect your repository. Now configure it:

1. **Service Name**: Keep default or rename to `todo-backend`
2. **Root Directory**:
   - Click **Settings** tab
   - Scroll to **Source** section
   - Set **Root Directory** to: `backend`
   - Click **Save**

### Step 4: Add Environment Variables
1. Click **Variables** tab
2. Click **"+ New Variable"** for each variable below:

```env
DATABASE_URL=postgresql://neondb_owner:npg_crCTIlG91iJR@ep-floral-bird-ahxuxm4r-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require
JWT_SECRET=a1fd210da153ee29b3595e54fe87dde55c9a24d213f9bc5f22f63b2bba5c54b8
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_DAYS=7
FRONTEND_URL=https://TEMP-will-update-after-vercel.com
```

**Note**: We'll update `FRONTEND_URL` after Step 2

3. Click outside or press Enter after each variable

### Step 5: Generate Public URL
1. Go to **Settings** tab
2. Scroll to **Networking** section
3. Click **"Generate Domain"**
4. Copy your domain (e.g., `todo-backend-production.up.railway.app`)

**🎯 SAVE THIS URL**: _______________________________________________

### Step 6: Deploy
1. Railway automatically deploys after you save settings
2. Go to **Deployments** tab to watch progress
3. Wait 2-3 minutes for first deployment
4. Status will show ✅ **"SUCCESS"** when done

### Step 7: Test Backend
Open in browser: `https://YOUR-RAILWAY-URL/health`

Expected response:
```json
{"status":"healthy"}
```

✅ **Backend deployed and connected to GitHub!**

---

## 🟢 Part 2: Vercel Frontend Setup (10 minutes)

### Step 1: Login to Vercel
1. Visit: **https://vercel.com/login**
2. Click **"Continue with GitHub"**
3. Authorize Vercel (if first time)

### Step 2: Import Project from GitHub
1. Click **"Add New..."** (top right)
2. Select **"Project"**
3. Find: **`hackathon-ii-phase-i-todo-app`**
4. Click **"Import"**

### Step 3: Configure Build Settings
Vercel will show configuration screen:

1. **Framework Preset**: Next.js ✅ (auto-detected)
2. **Root Directory**:
   - Click **"Edit"** next to Root Directory
   - Type: `frontend`
   - Click **Save**
3. **Build Command**: `npm run build` ✅ (auto-filled)
4. **Output Directory**: `.next` ✅ (auto-filled)
5. **Install Command**: `npm install` ✅ (auto-filled)

### Step 4: Add Environment Variable
Scroll down to **Environment Variables** section:

1. **Key**: `NEXT_PUBLIC_API_URL`
2. **Value**: `https://YOUR-RAILWAY-URL` (from Part 1, Step 5)
3. Click **"Add"**

### Step 5: Deploy
1. Click **"Deploy"** button (bottom)
2. Watch the build logs (optional - just for fun!)
3. Wait 2-3 minutes
4. You'll see: **"Congratulations! 🎉"**

### Step 6: Get Your Frontend URL
1. You'll see your deployment URL on success screen
2. Format: `hackathon-ii-phase-i-todo-app-XXXXX.vercel.app`
3. Click **"Visit"** to open your app

**🎯 SAVE THIS URL**: _______________________________________________

### Step 7: Enable Auto-Deploy
✅ **Already enabled!** Vercel automatically deploys on every push to `main` branch.

---

## 🔄 Part 3: Update Backend CORS (2 minutes)

Now update the backend to accept requests from your frontend:

### Step 1: Update Railway Variable
1. Go back to **Railway dashboard**
2. Click on your backend service
3. Click **Variables** tab
4. Find `FRONTEND_URL`
5. Update its value to: `https://YOUR-VERCEL-URL` (from Part 2, Step 6)
6. Press Enter or click outside to save

### Step 2: Verify Auto-Redeploy
1. Railway will automatically redeploy (watch **Deployments** tab)
2. Wait 1-2 minutes
3. Status shows ✅ **"SUCCESS"**

✅ **CORS configured! Frontend can now talk to backend.**

---

## 🎯 Part 4: Test Everything (5 minutes)

### Test 1: Health Check
Visit: `https://YOUR-RAILWAY-URL/health`
- ✅ Should return: `{"status":"healthy"}`

### Test 2: API Documentation
Visit: `https://YOUR-RAILWAY-URL/docs`
- ✅ Should show interactive API documentation

### Test 3: Frontend Loads
Visit: `https://YOUR-VERCEL-URL`
- ✅ Should show login/signup page

### Test 4: User Registration
1. Click **"Sign Up"**
2. Enter email: `test@example.com`
3. Enter password: `test123`
4. Click **"Sign up"**
- ✅ Should redirect to dashboard

### Test 5: Create Task
1. Enter title: "Test Task"
2. Enter description: "Testing deployment"
3. Click **"Add Task"**
- ✅ Task should appear in list

### Test 6: Task Operations
- ✅ Check task as complete
- ✅ Edit task title
- ✅ Delete task

### Test 7: Multi-User Isolation
1. Logout
2. Create new account with different email
3. Create a task
4. Verify you don't see tasks from first account

---

## 🎉 Success! Auto-Deploy is Live!

### Your Live URLs:
- **Frontend**: `https://_____________________________.vercel.app`
- **Backend**: `https://_____________________________.railway.app`
- **API Docs**: `https://_____________________________.railway.app/docs`

### What Happens Now:
1. **Every push to GitHub** → Automatic deployment
2. **Railway monitors**: `backend/` folder
3. **Vercel monitors**: `frontend/` folder
4. **Zero downtime**: New versions replace old smoothly
5. **Rollback**: Easy rollback from dashboards if needed

---

## 🔧 How to Make Changes

### Update Backend:
```bash
cd backend
# Make your changes
git add .
git commit -m "Update backend feature"
git push
# Railway automatically deploys!
```

### Update Frontend:
```bash
cd frontend
# Make your changes
git add .
git commit -m "Update frontend UI"
git push
# Vercel automatically deploys!
```

### Update Both:
```bash
# Make changes to both
git add .
git commit -m "Update full-stack feature"
git push
# Both deploy automatically!
```

---

## 📊 Monitoring Your Deployments

### Railway Dashboard:
- **Deployments**: See deployment history and logs
- **Metrics**: CPU, memory, network usage
- **Logs**: Real-time application logs
- **Variables**: Update environment variables anytime

### Vercel Dashboard:
- **Deployments**: See all deployments with preview URLs
- **Analytics**: Page views, performance metrics
- **Logs**: Function logs and errors
- **Domains**: Add custom domains

---

## ⚙️ Environment Variables Reference

### Backend (Railway):
| Variable | Value | Purpose |
|----------|-------|---------|
| `DATABASE_URL` | Your Neon PostgreSQL connection string | Database connection |
| `JWT_SECRET` | `a1fd210da...` | JWT token signing |
| `JWT_ALGORITHM` | `HS256` | JWT algorithm |
| `ACCESS_TOKEN_EXPIRE_DAYS` | `7` | Token expiry duration |
| `FRONTEND_URL` | Your Vercel URL | CORS configuration |

### Frontend (Vercel):
| Variable | Value | Purpose |
|----------|-------|---------|
| `NEXT_PUBLIC_API_URL` | Your Railway URL | Backend API endpoint |

---

## 🚨 Troubleshooting

### Backend deployment fails:
1. Check Railway logs: **Deployments** → Click deployment → **View Logs**
2. Common issues:
   - Database connection: Verify `DATABASE_URL` is correct
   - Python version: Should be 3.11 (check `runtime.txt`)
   - Missing dependencies: Check `requirements.txt`

### Frontend deployment fails:
1. Check Vercel logs: **Deployments** → Click deployment → **View Logs**
2. Common issues:
   - Missing env var: Ensure `NEXT_PUBLIC_API_URL` is set
   - Root directory: Should be `frontend`
   - Node version: Vercel auto-detects from `package.json`

### "Failed to fetch" error on frontend:
1. Verify `NEXT_PUBLIC_API_URL` in Vercel matches Railway URL
2. Verify `FRONTEND_URL` in Railway matches Vercel URL
3. Both should use `https://` (not `http://`)
4. Check Railway logs for CORS errors

### Database connection errors:
1. Go to Neon dashboard: https://console.neon.tech
2. Verify database is active
3. Check connection string ends with `?sslmode=require`
4. Copy fresh connection string if needed

---

## 🔐 Security Notes

- ✅ `JWT_SECRET` is set and secure
- ✅ Database credentials are in environment variables (not code)
- ✅ CORS is configured to only allow your frontend
- ✅ Passwords are hashed with bcrypt
- ✅ All connections use HTTPS/SSL

---

## 📈 Next Steps After Deployment

1. **Add Custom Domain** (Optional):
   - Railway: Settings → Networking → Add custom domain
   - Vercel: Settings → Domains → Add domain
   - Update environment variables with new domains

2. **Set Up Monitoring**:
   - Railway: Built-in metrics available
   - Vercel: Analytics available in dashboard
   - Consider: Sentry for error tracking

3. **Enable Notifications**:
   - Railway: Settings → Notifications → Slack/Email
   - Vercel: Settings → Notifications → GitHub/Slack

4. **Backup Database**:
   - Neon: Automated backups included
   - Consider: Manual export for extra safety

---

## 📞 Support Resources

- **Railway Docs**: https://docs.railway.app
- **Vercel Docs**: https://vercel.com/docs
- **Neon Docs**: https://neon.tech/docs
- **Project Issues**: https://github.com/umernasir1/hackathon-ii-phase-i-todo-app/issues

---

## ✅ Deployment Checklist

Use this checklist as you go through the setup:

### Railway Backend:
- [ ] Logged in to Railway with GitHub
- [ ] Created new project from GitHub repo
- [ ] Set root directory to `backend`
- [ ] Added all environment variables
- [ ] Generated public domain
- [ ] First deployment successful
- [ ] Health check returns `{"status":"healthy"}`
- [ ] API docs accessible at `/docs`

### Vercel Frontend:
- [ ] Logged in to Vercel with GitHub
- [ ] Imported project from GitHub
- [ ] Set root directory to `frontend`
- [ ] Added `NEXT_PUBLIC_API_URL` environment variable
- [ ] First deployment successful
- [ ] Frontend loads in browser
- [ ] Can see login/signup page

### Final Configuration:
- [ ] Updated `FRONTEND_URL` in Railway with Vercel URL
- [ ] Railway auto-redeployed successfully
- [ ] Can register new user
- [ ] Can login with user
- [ ] Can create, edit, delete tasks
- [ ] Multi-user isolation works

---

**🎉 You're all set! Your app now auto-deploys on every push to GitHub! 🚀**
