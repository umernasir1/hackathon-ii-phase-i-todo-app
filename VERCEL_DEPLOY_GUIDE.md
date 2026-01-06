# Vercel Frontend Deployment Guide

Complete guide to deploy your Next.js frontend to Vercel with Railway backend integration.

## Prerequisites

- ✅ Backend deployed on Railway: https://hackathon-ii-phase-i-todo-app-production.up.railway.app
- ✅ GitHub repository: https://github.com/umernasir1/hackathon-ii-phase-i-todo-app
- ✅ Frontend code at project root (completed)
- ✅ Vercel account (create one at https://vercel.com if needed)

## Step-by-Step Deployment

### Step 1: Import Project to Vercel

1. **Go to Vercel Dashboard**: https://vercel.com/new
2. **Import Git Repository**:
   - Click "Import Git Repository"
   - Select "GitHub" and authorize Vercel to access your repositories
   - Find and select: `umernasir1/hackathon-ii-phase-i-todo-app`
   - Click "Import"

### Step 2: Configure Project Settings

Vercel will auto-detect your Next.js project. Verify these settings:

**Framework Preset**: Next.js ✅ (Auto-detected)

**Root Directory**: `.` (Leave empty or set to root) ✅

**Build & Development Settings**:
```
Build Command:       npm run build          (Auto-detected)
Output Directory:    .next                  (Auto-detected)
Install Command:     npm install            (Auto-detected)
Development Command: npm run dev            (Auto-detected)
```

### Step 3: Set Environment Variables (CRITICAL)

Before deploying, add your backend URL:

1. **In the Vercel project configuration page**, scroll to "Environment Variables"
2. **Add the following variable**:

   ```
   Name:  NEXT_PUBLIC_API_URL
   Value: https://hackathon-ii-phase-i-todo-app-production.up.railway.app
   ```

3. **Select environments**: Check all three boxes:
   - ✅ Production
   - ✅ Preview
   - ✅ Development

4. **Click "Add"**

**Important**:
- The URL should NOT have a trailing slash
- This variable MUST start with `NEXT_PUBLIC_` to be accessible in the browser
- Vercel will expose this to your React components

### Step 4: Deploy

1. Click **"Deploy"** button
2. Wait for the build to complete (usually 2-3 minutes)
3. Watch the build logs for any errors

**Build Process**:
```
✓ Installing dependencies
✓ Building application
✓ Optimizing production build
✓ Deploying to Vercel Edge Network
```

### Step 5: Access Your Deployed Frontend

Once deployment succeeds, Vercel will provide URLs:

**Production URL**: `https://your-project-name.vercel.app`
- Example: `https://hackathon-ii-phase-i-todo-app.vercel.app`

**Custom domains** can be added later in project settings.

### Step 6: Verify Deployment

1. **Visit your Vercel URL**
2. **Test the application**:
   - ✅ Landing page loads
   - ✅ Sign up creates new account
   - ✅ Login authenticates successfully
   - ✅ Dashboard loads user's tasks
   - ✅ Create, update, delete tasks work
   - ✅ Logout clears session

### Step 7: Check Backend Connection

Open browser DevTools (F12) and check:

**Network Tab**:
- API calls should go to: `https://hackathon-ii-phase-i-todo-app-production.up.railway.app`
- Status codes should be `200 OK` for successful requests
- No CORS errors

**Console Tab**:
- No error messages about API connection
- Check that `NEXT_PUBLIC_API_URL` is correctly set

## Troubleshooting

### Issue: "Failed to fetch" or CORS errors

**Solution**: Verify Railway backend CORS settings

1. Check your Railway backend has proper CORS configuration
2. Backend should allow origins from your Vercel domain
3. In your FastAPI backend `main.py`:
   ```python
   from fastapi.middleware.cors import CORSMiddleware

   app.add_middleware(
       CORSMiddleware,
       allow_origins=[
           "http://localhost:3000",
           "https://your-project-name.vercel.app",  # Add your Vercel URL
           "https://*.vercel.app"  # Allow all Vercel preview deployments
       ],
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```
4. Redeploy your Railway backend after CORS update

### Issue: Environment variable not found

**Solution**:
1. Go to Vercel Dashboard > Your Project > Settings > Environment Variables
2. Verify `NEXT_PUBLIC_API_URL` is set
3. Trigger a new deployment: Deployments > ⋯ > Redeploy

### Issue: Build fails with "Module not found"

**Solution**:
1. Check `package.json` has all dependencies
2. Verify `node_modules` is in `.gitignore`
3. Clear build cache: Settings > General > Clear Build Cache
4. Redeploy

### Issue: Pages show 404

**Solution**:
1. Verify Next.js App Router structure (`app/` directory exists)
2. Check `next.config.ts` is at project root
3. Ensure `package.json` is at project root

## Auto-Deployment Setup

Once deployed, Vercel automatically sets up:

✅ **Continuous Deployment**: Every push to `main` branch triggers new deployment

✅ **Preview Deployments**: Pull requests get unique preview URLs

✅ **Rollbacks**: Instant rollback to previous deployments if needed

### Managing Auto-Deployments

**To trigger deployment**:
```bash
git add .
git commit -m "Your changes"
git push origin main
```

**To disable auto-deployment**:
1. Go to Project Settings > Git
2. Toggle "Auto-deploy" off for specific branches

## Environment Management

### Local Development
```bash
# .env.local
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### Vercel Production
```bash
# Set in Vercel Dashboard
NEXT_PUBLIC_API_URL=https://hackathon-ii-phase-i-todo-app-production.up.railway.app
```

## Post-Deployment Checklist

- [ ] Frontend accessible via Vercel URL
- [ ] Sign up flow creates users successfully
- [ ] Login authenticates and redirects to dashboard
- [ ] Tasks CRUD operations work
- [ ] Logout clears authentication
- [ ] No console errors
- [ ] API calls reach Railway backend
- [ ] HTTPS is enabled (automatic with Vercel)
- [ ] Custom domain configured (optional)

## Monitoring & Analytics

**Vercel Dashboard provides**:
- Build logs and deployment history
- Performance metrics
- Error tracking
- Analytics (on paid plans)

**Access logs**:
1. Go to Project > Deployments
2. Click on a deployment
3. View "Building" and "Runtime Logs"

## Custom Domain (Optional)

To use your own domain:

1. Go to Project Settings > Domains
2. Click "Add Domain"
3. Enter your domain name
4. Follow DNS configuration instructions
5. Wait for DNS propagation (5-60 minutes)

## Useful Links

- **Vercel Dashboard**: https://vercel.com/dashboard
- **Your Frontend**: https://[your-project].vercel.app
- **Your Backend**: https://hackathon-ii-phase-i-todo-app-production.up.railway.app
- **GitHub Repo**: https://github.com/umernasir1/hackathon-ii-phase-i-todo-app
- **Vercel Docs**: https://vercel.com/docs

## Quick Reference Commands

```bash
# View deployment status
vercel --prod

# View logs
vercel logs

# List deployments
vercel ls

# Rollback to previous deployment
# (Do this from Vercel Dashboard)
```

## Support

If you encounter issues:
1. Check Vercel build logs
2. Verify Railway backend is running
3. Test backend API directly: https://hackathon-ii-phase-i-todo-app-production.up.railway.app/health
4. Check browser DevTools console and network tab
5. Review this guide's troubleshooting section

---

**Ready to Deploy!** Follow the steps above to get your frontend live on Vercel.
