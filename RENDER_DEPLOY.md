# Deploy Backend to Render.com (Alternative to Railway)

If Railway is giving you issues, Render is more reliable and just as easy.

## Step-by-Step: Deploy to Render

### 1. Sign Up / Login
1. Go to: https://render.com
2. Click **"Get Started for Free"**
3. Choose **"Sign up with GitHub"**
4. Authorize Render to access your repositories

### 2. Create Web Service
1. Click **"New +"** (top right)
2. Select **"Web Service"**
3. Click **"Connect account"** if needed
4. Find your repository: `hackathon-ii-phase-i-todo-app`
5. Click **"Connect"**

### 3. Configure Service
Fill in these settings:

**Name**: `todo-backend` (or any name you prefer)

**Region**: Choose closest to you (e.g., Oregon, Frankfurt, Singapore)

**Branch**: `main`

**Root Directory**: `backend`

**Runtime**: **Python 3**

**Build Command**:
```
pip install -r requirements.txt
```

**Start Command**:
```
python -m alembic upgrade head && python -m uvicorn main:app --host 0.0.0.0 --port $PORT
```

**Instance Type**: **Free** (select from dropdown)

### 4. Add Environment Variables
Scroll down to **"Environment Variables"** section.

Click **"Add Environment Variable"** for each:

```
DATABASE_URL
postgresql://neondb_owner:npg_crCTIlG91iJR@ep-floral-bird-ahxuxm4r-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require

JWT_SECRET
a1fd210da153ee29b3595e54fe87dde55c9a24d213f9bc5f22f63b2bba5c54b8

JWT_ALGORITHM
HS256

ACCESS_TOKEN_EXPIRE_DAYS
7

FRONTEND_URL
https://your-app.vercel.app
```

**Note**: You'll update FRONTEND_URL after deploying the frontend.

### 5. Deploy
1. Scroll down and click **"Create Web Service"**
2. Render will start building (takes 3-5 minutes)
3. Watch the build logs on screen
4. Wait for **"Live"** status with green checkmark ✅

### 6. Get Your Backend URL
Once deployed:
1. Your URL will be shown at the top (e.g., `https://todo-backend.onrender.com`)
2. Copy this URL - you'll need it for the frontend

### 7. Test Backend
Visit: `https://your-backend-url.onrender.com/health`

Should return:
```json
{"status":"healthy"}
```

Also test: `https://your-backend-url.onrender.com/docs` for API documentation.

---

## Why Render Over Railway?

- ✅ More reliable build detection
- ✅ Clearer error messages
- ✅ Free tier includes 750 hours/month
- ✅ Auto-sleep on free tier (wakes on request)
- ✅ Better logging and monitoring

## Important Notes

**Free Tier Limitations**:
- Service spins down after 15 minutes of inactivity
- First request after spin-down takes ~30 seconds
- 750 hours/month (more than enough for testing)

**Spin-down Notice**: This is normal for free tier. Your app will wake up when someone visits it.

---

## Next: Deploy Frontend to Vercel

Once you have your Render backend URL, continue with frontend deployment to Vercel.

You'll use your Render URL as the `NEXT_PUBLIC_API_URL` in Vercel.

---

**Need Help?**
- Check Render logs for specific errors
- Verify all environment variables are set
- Make sure Root Directory is `backend`
