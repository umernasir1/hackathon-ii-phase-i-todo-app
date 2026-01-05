# 🚀 Quick Deployment Reference

**⏱️ Total Time**: 20 minutes | **📖 Full Guide**: See `GITHUB_AUTO_DEPLOY_GUIDE.md`

---

## 🎯 Overview

```
GitHub Repository → Railway (Backend) + Vercel (Frontend) → Live App
      ↓                    ↓                    ↓
  Every push        Auto-deploys          Auto-deploys
```

---

## 📋 Quick Steps

### 1️⃣ Railway Backend (10 min)
```
https://railway.app/login
→ Login with GitHub
→ New Project → Deploy from GitHub repo
→ Select: hackathon-ii-phase-i-todo-app
→ Settings → Root Directory: backend
→ Variables → Add 5 environment variables
→ Settings → Networking → Generate Domain
→ Save domain: _______________________
```

### 2️⃣ Vercel Frontend (10 min)
```
https://vercel.com/login
→ Continue with GitHub
→ Add New Project
→ Import: hackathon-ii-phase-i-todo-app
→ Root Directory: frontend
→ Environment Variables:
   NEXT_PUBLIC_API_URL = [Your Railway URL]
→ Deploy
→ Save URL: _______________________
```

### 3️⃣ Update CORS (2 min)
```
Railway Dashboard
→ Variables
→ Update FRONTEND_URL = [Your Vercel URL]
→ Auto-redeploys
```

---

## 🔧 Environment Variables

### Railway (Backend):
```env
DATABASE_URL=postgresql://neondb_owner:npg_crCTIlG91iJR@ep-floral-bird-ahxuxm4r-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require
JWT_SECRET=a1fd210da153ee29b3595e54fe87dde55c9a24d213f9bc5f22f63b2bba5c54b8
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_DAYS=7
FRONTEND_URL=[Update after Vercel deploy]
```

### Vercel (Frontend):
```env
NEXT_PUBLIC_API_URL=[Your Railway URL]
```

---

## ✅ Test Checklist

- [ ] `https://[railway-url]/health` → `{"status":"healthy"}`
- [ ] `https://[railway-url]/docs` → API documentation
- [ ] `https://[vercel-url]` → Login page loads
- [ ] Register account → Works
- [ ] Create task → Works
- [ ] Edit/Delete task → Works
- [ ] Logout/Login → Works

---

## 🚨 Quick Troubleshooting

| Issue | Fix |
|-------|-----|
| Backend won't deploy | Check Railway logs, verify DATABASE_URL |
| Frontend won't deploy | Check Root Directory = `frontend` |
| "Failed to fetch" | Verify env vars match deployed URLs |
| CORS error | Update FRONTEND_URL in Railway |
| Database error | Check Neon database is active |

---

## 🎯 Your Deployment URLs

After setup, record your URLs here:

**Backend**: https://_____________________________.railway.app
**Frontend**: https://_____________________________.vercel.app
**API Docs**: https://_____________________________.railway.app/docs

---

## 🔄 Making Changes After Setup

```bash
# Make changes
git add .
git commit -m "Your changes"
git push

# Both Railway and Vercel auto-deploy! ✨
```

---

## 📚 Resources

- **Full Guide**: `GITHUB_AUTO_DEPLOY_GUIDE.md` (detailed step-by-step)
- **Step-by-Step**: `DEPLOY_NOW.md` (manual deployment)
- **Assistant Guide**: `DEPLOYMENT_ASSISTANT.md` (web dashboard help)
- **Repository**: https://github.com/umernasir1/hackathon-ii-phase-i-todo-app

---

**Ready? Start here**: https://railway.app/login 🚀
