# 🐍 Deploy to PythonAnywhere - Complete Guide

**Last Updated**: December 28, 2025
**Platform**: PythonAnywhere (Backend) + Vercel (Frontend)
**Cost**: 100% FREE - No credit card required!
**Difficulty**: Beginner-friendly

---

## ✅ Why PythonAnywhere?

- ✅ **100% FREE** - No credit card, ever
- ✅ **Always on** - No spin-down/sleep mode
- ✅ **Python native** - Perfect for FastAPI
- ✅ **Simple setup** - Web-based interface
- ✅ **Git integration** - Clone directly from GitHub
- ✅ **Reliable** - Been around since 2012

---

## Part 1: Deploy Backend to PythonAnywhere 🐍

### Step 1: Create PythonAnywhere Account (FREE)

1. Go to **https://www.pythonanywhere.com/**
2. Click **"Start running Python online in less than a minute!"**
3. Click **"Create a Beginner account"** (FREE forever)
4. Fill in:
   - Username: Choose any username (e.g., `yourusername`)
   - Email: Your email
   - Password: Create a password
5. Click **"Register"**
6. ✅ Check your email and verify (if required)
7. ✅ No credit card needed!

### Step 2: Open Bash Console

1. Once logged in, click on **"Consoles"** tab
2. Click **"Bash"** under "Start a new console"
3. A black terminal window will open
4. ✅ You're now in a Linux command line!

### Step 3: Clone Your Repository

In the Bash console, type these commands:

```bash
# Clone your repository
git clone https://github.com/umernasir1/hackathon-ii-phase-i-todo-app.git

# Navigate to backend directory
cd hackathon-ii-phase-i-todo-app/backend

# Check if files are there
ls -la
```

You should see:
- `main.py`
- `requirements.txt`
- `app/` directory
- etc.

✅ **Your code is now on PythonAnywhere!**

### Step 4: Create Virtual Environment

Still in the Bash console:

```bash
# Go back to home directory
cd ~

# Create virtual environment (Python 3.11)
mkvirtualenv --python=/usr/bin/python3.11 todoenv

# Your prompt should now show (todoenv) at the beginning
```

### Step 5: Install Dependencies

```bash
# Navigate to backend directory
cd ~/hackathon-ii-phase-i-todo-app/backend

# Install all requirements
pip install -r requirements.txt

# This will take 2-3 minutes - wait for it to complete
```

Expected packages installed:
- fastapi
- uvicorn
- sqlmodel
- python-jose
- passlib
- python-dotenv
- alembic
- etc.

✅ **Dependencies installed!**

### Step 6: Create Web App

1. Click on **"Web"** tab (top of page)
2. Click **"Add a new web app"**
3. Click **"Next"** (ignore the domain name, we'll use the default)
4. Choose **"Manual configuration"** (not Flask/Django)
5. Select **"Python 3.11"**
6. Click **"Next"**
7. ✅ Web app created!

You'll see your web app URL: `https://yourusername.pythonanywhere.com`

### Step 7: Configure Virtual Environment

On the Web tab, scroll to **"Virtualenv"** section:

1. Click **"Enter path to a virtualenv"**
2. Enter: `/home/yourusername/.virtualenvs/todoenv`
   - Replace `yourusername` with YOUR actual PythonAnywhere username
3. Click the checkmark ✓

✅ **Virtual environment linked!**

### Step 8: Configure WSGI File

This is the most important step!

1. On the Web tab, scroll to **"Code"** section
2. Find **"WSGI configuration file:"** (will be something like `/var/www/yourusername_pythonanywhere_com_wsgi.py`)
3. Click on that file path (blue link)
4. A code editor will open

**DELETE ALL THE EXISTING CODE** in that file and replace with:

```python
# /var/www/yourusername_pythonanywhere_com_wsgi.py
import sys
import os

# Add your project directory to the sys.path
project_home = '/home/yourusername/hackathon-ii-phase-i-todo-app/backend'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variables
os.environ['DATABASE_URL'] = 'postgresql://neondb_owner:npg_crCTIlG91iJR@ep-floral-bird-ahxuxm4r-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require'
os.environ['JWT_SECRET'] = 'a1fd210da153ee29b3595e54fe87dde55c9a24d213f9bc5f22f63b2bba5c54b8'
os.environ['JWT_ALGORITHM'] = 'HS256'
os.environ['ACCESS_TOKEN_EXPIRE_DAYS'] = '7'
os.environ['FRONTEND_URL'] = 'http://localhost:3000'  # We'll update this later

# Import the FastAPI app
from main import app as application
```

⚠️ **IMPORTANT**:
- Replace `yourusername` with YOUR PythonAnywhere username (appears twice in the code)
- Keep all the environment variable values exactly as shown

5. Click **"Save"** (top right)

✅ **WSGI file configured!**

### Step 9: Run Database Migrations

Go back to your Bash console:

```bash
# Make sure you're in the backend directory
cd ~/hackathon-ii-phase-i-todo-app/backend

# Make sure virtual environment is active (you should see (todoenv))
workon todoenv

# Run migrations
alembic upgrade head
```

You should see:
```
INFO  [alembic.runtime.migration] Running upgrade ...
```

✅ **Database tables created!**

### Step 10: Reload Web App

1. Go back to **"Web"** tab
2. Scroll to the top
3. Click the big green **"Reload"** button
4. Wait for "Reloading..." to finish

✅ **Backend deployed!**

### Step 11: Test Your Backend

Open a new browser tab and visit:

**Health Check:**
```
https://yourusername.pythonanywhere.com/health
```

Should return:
```json
{"status": "healthy"}
```

**API Documentation:**
```
https://yourusename.pythonanywhere.com/docs
```

Should show Swagger UI with all your endpoints!

✅ **Backend is LIVE!** 🎉

### Step 12: Get Your Backend URL

Your backend URL is:
```
https://yourusername.pythonanywhere.com
```

**Copy this** - you'll need it for the frontend!

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
2. Find your repository: `hackathon-ii-phase-i-todo-app`
3. Click **"Import"**

### Step 3: Configure Project

#### Framework
- **Framework Preset**: **Next.js** (auto-detected)

#### Root Directory
- Click **"Edit"** next to Root Directory
- Set to: `frontend` ⚠️ **CRITICAL**

#### Build Settings (leave defaults)
- **Build Command**: `npm run build`
- **Output Directory**: `.next`
- **Install Command**: `npm install`

### Step 4: Environment Variable

Click **"Environment Variables"** section:

- **Name**: `NEXT_PUBLIC_API_URL`
- **Value**: `https://yourusername.pythonanywhere.com`
  - ⚠️ Replace `yourusername` with YOUR PythonAnywhere username
  - Must start with `https://`
  - No trailing slash
  - No `/api` path

Example:
```
NEXT_PUBLIC_API_URL=https://johndoe.pythonanywhere.com
```

- **Environment**: Check all three (Production, Preview, Development)

### Step 5: Deploy Frontend

1. Click **"Deploy"**
2. Wait 2-4 minutes
3. Watch build progress
4. Wait for **"Congratulations!"** message

### Step 6: Get Your Frontend URL

- URL will be shown (e.g., `https://hackathon-ii-phase-i-todo-app.vercel.app`)
- Click **"Visit"** to open your app
- **Copy this URL**

### Step 7: Update Backend CORS

Now we need to update the backend to allow your Vercel URL.

1. Go back to **PythonAnywhere**
2. Click **"Web"** tab
3. Click on your **WSGI configuration file** again
4. Find this line:
   ```python
   os.environ['FRONTEND_URL'] = 'http://localhost:3000'
   ```
5. Change it to your Vercel URL:
   ```python
   os.environ['FRONTEND_URL'] = 'https://your-app.vercel.app'
   ```
   ⚠️ Use YOUR actual Vercel URL

6. Click **"Save"**
7. Go back to Web tab
8. Click **"Reload"** button

✅ **CORS configured!**

---

## Part 3: Test End-to-End Deployment 🧪

### Test Checklist

Visit your Vercel URL: `https://your-app.vercel.app`

#### 1. ✅ Landing Page Loads
- Page should load without errors
- Should see login/signup options

#### 2. ✅ User Registration
1. Click **"Sign Up"**
2. Enter test credentials:
   - Email: `test@example.com`
   - Password: `testpassword123`
3. Click **"Sign Up"**
4. Should redirect to dashboard

#### 3. ✅ Add Task
1. Enter task details:
   - Title: "Test PythonAnywhere deployment"
   - Description: "Testing Phase II deployment"
2. Click **"Add Task"**
3. Task should appear in the list

#### 4. ✅ Mark Complete
1. Click checkbox next to your task
2. Task should show as completed (strikethrough or visual change)

#### 5. ✅ Edit Task
1. Click **"Edit"** button
2. Change title to "Deployment successful!"
3. Click **"Save"**
4. Task should update

#### 6. ✅ Delete Task
1. Click **"Delete"** button
2. Confirm deletion
3. Task should disappear

#### 7. ✅ Logout and Login
1. Click **"Logout"**
2. Should redirect to login page
3. Log back in with same credentials
4. Should see dashboard

#### 8. ✅ API Documentation
Visit: `https://yourusername.pythonanywhere.com/docs`
- Should see Swagger UI
- All endpoints should be listed

---

## 🎉 Success!

If all tests passed, your Phase II application is **FULLY DEPLOYED!**

### Your Live URLs:

**Frontend (Vercel):**
```
https://your-app.vercel.app
```

**Backend (PythonAnywhere):**
```
https://yourusername.pythonanywhere.com
```

**API Docs:**
```
https://yourusername.pythonanywhere.com/docs
```

---

## 📊 PythonAnywhere Free Tier Limits

✅ **What You Get:**
- 1 web app (always on)
- 512 MB disk space
- Python 3.11 support
- Daily CPU quota (100 seconds)
- No credit card required
- No automatic sleep/spin-down

⚠️ **Limitations:**
- CPU quota resets daily
- Limited to 1 web app
- Outbound internet limited to whitelist (but Neon PostgreSQL works!)
- No SSH access on free tier

**Perfect for:** Demos, testing, small projects, hackathons!

---

## 🐛 Troubleshooting

### Backend shows "Something went wrong"

**Check the Error Log:**
1. Go to **"Web"** tab in PythonAnywhere
2. Scroll to **"Log files"** section
3. Click on **"Error log"** (red link)
4. Look at the latest errors

**Common issues:**
- **Import error**: Check WSGI file has correct username paths
- **Database error**: Verify DATABASE_URL is correct
- **Module not found**: Run `pip install -r requirements.txt` again

### Frontend can't connect to backend

**Check CORS:**
1. Verify FRONTEND_URL in WSGI file matches your Vercel URL exactly
2. Make sure you clicked "Reload" after changing WSGI file
3. Check browser console for specific error

**Check API URL:**
1. Verify `NEXT_PUBLIC_API_URL` in Vercel environment variables
2. Should be `https://yourusername.pythonanywhere.com` (no trailing slash)

### Database connection failed

**Check DATABASE_URL:**
- Must include `?sslmode=require`
- Check Neon dashboard that database is active
- Verify connection string is correct in WSGI file

### 502 Bad Gateway

**Reload the web app:**
1. Go to Web tab
2. Click "Reload" button
3. Wait 30 seconds
4. Try again

**Check WSGI file:**
- Verify import statement: `from main import app as application`
- Make sure project path is correct
- Check for syntax errors

---

## 🔧 Useful Commands

### In PythonAnywhere Bash Console:

```bash
# Activate virtual environment
workon todoenv

# Update code from GitHub
cd ~/hackathon-ii-phase-i-todo-app
git pull origin main

# Reinstall dependencies
cd backend
pip install -r requirements.txt

# Run migrations
alembic upgrade head

# Check what's installed
pip list

# View logs (last 50 lines)
tail -50 /var/log/yourusername.pythonanywhere.com.error.log
```

### After Making Changes:

1. Save changes
2. Go to Web tab
3. Click **"Reload"** button
4. Wait for reload to complete
5. Test your changes

---

## 🔄 Updating Your Deployment

### When you make code changes:

**Backend updates:**
1. Commit and push to GitHub
2. In PythonAnywhere Bash console:
   ```bash
   cd ~/hackathon-ii-phase-i-todo-app
   git pull origin main
   ```
3. Go to Web tab
4. Click **"Reload"**

**Frontend updates:**
1. Commit and push to GitHub
2. Vercel automatically deploys (no action needed!)
3. Check Vercel dashboard for deployment status

---

## 💡 Tips and Best Practices

### Keep Your Console Open
- The Bash console times out after 24 hours
- It's okay - just open a new one when needed
- Your web app keeps running 24/7

### Check Logs Regularly
- Error log shows Python errors
- Server log shows access requests
- Both accessible from Web tab

### Environment Variables
- Stored in WSGI file
- Never commit secrets to Git
- Update WSGI file if you change them
- Always reload after changes

### Database Migrations
- Run in Bash console, not WSGI file
- Only need to run once per migration
- If you add new models, create migration locally first

---

## 🚀 Advanced: Custom Domain (Optional)

PythonAnywhere allows custom domains on paid plans, but your `.pythonanywhere.com` URL works perfectly for hackathons and demos!

---

## 📝 Final Checklist

Before considering deployment complete:

- [ ] Backend deployed to PythonAnywhere
- [ ] Health check returns `{"status": "healthy"}`
- [ ] API docs accessible at `/docs`
- [ ] Frontend deployed to Vercel
- [ ] Can register new user
- [ ] Can login
- [ ] Can add tasks
- [ ] Can mark tasks complete
- [ ] Can edit tasks
- [ ] Can delete tasks
- [ ] Can logout and login again
- [ ] FRONTEND_URL updated in WSGI file
- [ ] Both URLs documented

---

## 🎓 What You've Learned

✅ Git clone in Linux environment
✅ Python virtual environments
✅ WSGI configuration for FastAPI
✅ Environment variable management
✅ Database migrations in production
✅ CORS configuration
✅ Full-stack deployment
✅ Production troubleshooting

---

## 🆘 Need Help?

If you encounter issues:

1. **Check error logs** (Web tab → Error log)
2. **Verify WSGI file** paths and environment variables
3. **Check Bash console** for command errors
4. **Reload web app** after any changes
5. **Verify Git pull** succeeded if updating code

**Common gotchas:**
- Forgetting to replace `yourusername` in WSGI file
- Not clicking "Reload" after changes
- Trailing slashes in URLs
- Virtual environment not activated

---

## 🎉 Congratulations!

You've successfully deployed a full-stack application with:
- ✅ Python FastAPI backend (PythonAnywhere)
- ✅ Next.js frontend (Vercel)
- ✅ PostgreSQL database (Neon)
- ✅ JWT authentication
- ✅ Complete CRUD operations
- ✅ 100% FREE hosting
- ✅ NO credit card required
- ✅ Production-ready deployment

**Phase II is COMPLETE!** 🚀

---

**Ready?** Let's start with Step 1: Create your PythonAnywhere account! 🐍

**Questions?** Let me know at each step if you need help!
