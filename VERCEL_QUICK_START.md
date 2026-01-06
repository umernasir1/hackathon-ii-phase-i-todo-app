# 🚀 Vercel Deployment - Quick Start

## Your Configuration

**Backend (Railway)**: ✅ Running
- URL: `https://hackathon-ii-phase-i-todo-app-production.up.railway.app`
- Health Check: ✅ Responding (200 OK)

**Frontend (Ready to Deploy)**:
- Repo: `umernasir1/hackathon-ii-phase-i-todo-app`
- Branch: `main`
- Framework: Next.js 16

## Deploy in 5 Minutes

### 1. Go to Vercel
👉 **https://vercel.com/new**

### 2. Import Repository
- Click "Import Git Repository"
- Select: `umernasir1/hackathon-ii-phase-i-todo-app`
- Click "Import"

### 3. Add Environment Variable (CRITICAL!)
In the configuration screen:

```
Name:  NEXT_PUBLIC_API_URL
Value: https://hackathon-ii-phase-i-todo-app-production.up.railway.app
```

✅ Check: Production, Preview, Development

### 4. Deploy
Click **"Deploy"** and wait 2-3 minutes

### 5. Test Your App
Visit the Vercel URL and verify:
- [ ] Landing page loads
- [ ] Sign up works
- [ ] Login works
- [ ] Dashboard shows tasks
- [ ] Can create/edit/delete tasks

## If You Get CORS Errors

Your Railway backend needs to allow Vercel's domain.

**Check your FastAPI `main.py` has**:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or add your specific Vercel domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Then redeploy your Railway backend.

## Auto-Deployment Active

Every `git push origin main` will trigger automatic Vercel deployment! 🎉

---

**Full Guide**: See `VERCEL_DEPLOY_GUIDE.md` for detailed instructions.
