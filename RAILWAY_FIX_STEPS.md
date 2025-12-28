# Railway Deployment Fix - Step by Step

## Issue: "Error creating build plan with Railpack"

This happens when Railway can't auto-detect the build configuration. Let's fix it.

---

## 🔧 Fix Steps

### Step 1: Check Service Configuration

In Railway dashboard:

1. Click on your **backend service** (the one that failed)
2. Click on **"Settings"** tab (on the left or top)
3. Scroll down to find these sections:

---

### Step 2: Configure Root Directory

**Look for: "Source"** or **"Deploy"** section

**Set:**
- **Root Directory**: `backend`
- **Branch**: `main`

**Save** if there's a save button.

---

### Step 3: Configure Build Settings

**Look for: "Build"** or **"Deploy"** section

Railway needs to know it's a Python project. Set these:

**Builder**:
- If you see a dropdown, select **"Nixpacks"** or **"Dockerfile"**
- If it says "Automatic", that's fine

**Build Command** (might be labeled "Install Command"):
```
pip install -r requirements.txt
```

**Start Command** (might be labeled "Run Command"):
```
python -m alembic upgrade head && python -m uvicorn main:app --host 0.0.0.0 --port $PORT
```

**OR if the above doesn't work, try this simpler version:**
```
uvicorn main:app --host 0.0.0.0 --port $PORT
```

**Save** the settings.

---

### Step 4: Add Python Version (Important!)

Railway might not detect Python version. Let's be explicit:

**Look for: "Environment Variables"** section

Add a new variable:
- **Name**: `PYTHON_VERSION`
- **Value**: `3.11.8`

This tells Railway which Python to use.

---

### Step 5: Verify All Environment Variables

Make sure you have ALL these in the **Variables** tab:

```
✅ DATABASE_URL
✅ JWT_SECRET
✅ JWT_ALGORITHM
✅ ACCESS_TOKEN_EXPIRE_DAYS
✅ FRONTEND_URL
✅ PYTHON_VERSION (just added)
```

---

### Step 6: Force Redeploy

1. Go to **"Deployments"** tab
2. Click on the failed deployment
3. Click **"Redeploy"** button (top right)

**OR**

1. Go to **"Settings"** tab
2. Scroll to bottom
3. Find **"Trigger Deploy"** or similar button
4. Click it

---

### Step 7: Watch the Build

1. Stay on the **Deployments** page
2. Watch the build logs in real-time
3. Look for these stages:
   - ✅ Cloning repository
   - ✅ Installing dependencies
   - ✅ Running alembic migrations
   - ✅ Starting uvicorn server

**Common Success Messages:**
- "Build succeeded"
- "Deployment live"
- "Application started"

---

## 🆘 If Build Still Fails

### Check the Error Message

Look at the build logs. Common errors and fixes:

**Error: "No Python installation found"**
- **Fix**: Add `PYTHON_VERSION=3.11.8` environment variable

**Error: "requirements.txt not found"**
- **Fix**: Verify Root Directory is set to `backend`

**Error: "No module named 'fastapi'"**
- **Fix**: Verify Build Command is `pip install -r requirements.txt`

**Error: "Port already in use" or "Address in use"**
- **Fix**: Make sure Start Command uses `$PORT` variable

**Error: "Database connection failed"**
- **Fix**: Check `DATABASE_URL` is correct and includes `?sslmode=require`

---

## Alternative Configuration Method

If the above doesn't work, try this:

### Create railway.json file

Railway might prefer a config file. Let me know if you want to try this approach.

---

## 📸 What to Look For

When you're in Railway Settings, you should see sections like:

```
Source
├── Repository: umernasir1/hackathon-ii-phase-i-todo-app
├── Branch: main
└── Root Directory: backend

Build
├── Builder: Nixpacks
├── Build Command: pip install -r requirements.txt
└── Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT

Environment Variables
├── DATABASE_URL: postgresql://...
├── JWT_SECRET: a1fd...
├── PYTHON_VERSION: 3.11.8
└── ... (other vars)
```

---

## ✅ Success Indicators

When deployment succeeds, you'll see:

1. **Green checkmark** ✅ on deployment
2. **"Live"** status
3. A **public URL** generated (like `xxx.up.railway.app`)
4. Logs showing: "Application startup complete"

---

## 🎯 Next Steps After Success

1. Copy your Railway URL
2. Test it: Visit `https://your-url.up.railway.app/health`
3. Should return: `{"status":"healthy"}`
4. Then we'll deploy the frontend to Vercel

---

**Try the fixes above and let me know:**
- ✅ "It's deploying!" - when build starts
- ✅ "Deployed!" + your URL - when it's live
- ❌ "Still failing" + error message - if it fails again
