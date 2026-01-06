# CORS Configuration for Vercel Frontend

## Issue
Your Railway backend CORS is currently configured to only allow:
- `http://localhost:3000` (local development)
- The value of `FRONTEND_URL` environment variable

Once you deploy to Vercel, you'll get a URL like:
- `https://your-project.vercel.app`

The backend needs to allow requests from this Vercel domain.

## Solution: Update Railway Environment Variable

### Option 1: Allow All Vercel Domains (Recommended for Quick Deploy)

1. Go to your Railway project dashboard
2. Navigate to: **Variables** tab
3. Find or add `FRONTEND_URL` variable
4. Set the value to allow wildcard Vercel domains:

```
FRONTEND_URL=https://*.vercel.app
```

**Note**: This allows all `*.vercel.app` domains, including preview deployments.

### Option 2: Allow Specific Vercel Domain (More Secure)

After deploying to Vercel and getting your production URL:

1. Go to Railway project > **Variables**
2. Update `FRONTEND_URL` to your exact Vercel URL:

```
FRONTEND_URL=https://your-project-name.vercel.app
```

Replace `your-project-name` with your actual Vercel project name.

### Option 3: Multiple Origins (Best Practice)

If you want to allow both localhost (development) and Vercel (production):

**Update `backend/main.py`** to accept multiple origins:

```python
# CORS configuration for Next.js frontend
origins = [
    "http://localhost:3000",  # Next.js dev server
    "https://localhost:3000",
    settings.frontend_url,     # From FRONTEND_URL env var
    "https://*.vercel.app",    # All Vercel deployments
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Then in Railway, set:
```
FRONTEND_URL=https://your-project-name.vercel.app
```

**After making changes**:
- Redeploy your Railway backend
- Wait 1-2 minutes for deployment
- Then deploy your Vercel frontend

## Current CORS Configuration

Your backend (`backend/main.py:31-43`) currently has:

```python
origins = [
    "http://localhost:3000",
    "https://localhost:3000",
    settings.frontend_url
]
```

Where `settings.frontend_url` comes from the `FRONTEND_URL` environment variable.

## Testing CORS After Deploy

1. Deploy frontend to Vercel
2. Open browser DevTools (F12)
3. Go to **Network** tab
4. Try to sign up or login
5. Check the API request to Railway:
   - ✅ **Success**: Status 200, no CORS errors
   - ❌ **CORS Error**: Red error in console about "Access-Control-Allow-Origin"

If you see CORS errors:
- Verify `FRONTEND_URL` is set correctly in Railway
- Check Railway backend has redeployed with new env var
- Clear browser cache and try again

## Quick Fix for Testing

If you want to test immediately without CORS restrictions:

**Temporarily allow all origins** (NOT for production!):

In `backend/main.py`, change:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (TEMPORARY ONLY)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Then redeploy Railway backend.

**Important**: Change this back to specific origins before going to production!

---

**Action Required**: Update `FRONTEND_URL` in Railway before deploying to Vercel.
