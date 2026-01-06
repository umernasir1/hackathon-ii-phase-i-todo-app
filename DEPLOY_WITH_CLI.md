# 🚀 Deploy with Vercel CLI (Bypass GitHub Limit)

Since you've hit the GitHub repository limit, let's deploy directly using Vercel CLI!

**Time Required**: 5 minutes

---

## Step 1: Install Vercel CLI

Open your terminal and run:

```bash
npm install -g vercel
```

Wait for installation to complete...

---

## Step 2: Navigate to Your Project

```bash
cd "D:\PIAIC Batch 76\HackatonII"
```

---

## Step 3: Login to Vercel

```bash
vercel login
```

This will:
1. Open your browser
2. Ask you to confirm login
3. Authenticate your CLI

Click "Confirm" in the browser, then return to terminal.

---

## Step 4: Deploy Your Project

```bash
vercel
```

### Answer These Questions:

```
? Set up and deploy "D:\PIAIC Batch 76\HackatonII"?
→ Y (press Enter)

? Which scope do you want to deploy to?
→ Select your account (press Enter)

? Link to existing project?
→ N (press Enter)

? What's your project's name?
→ hackathon-ii-todo-app (or press Enter for default)

? In which directory is your code located?
→ ./ (press Enter)

? Want to override the settings?
→ N (press Enter)
```

Vercel will now:
- 📦 Upload your files
- 🔨 Build your Next.js app
- 🚀 Deploy to a preview URL

You'll see output like:
```
🔗 Preview: https://hackathon-ii-todo-app-abc123.vercel.app
```

---

## Step 5: Add Environment Variable

```bash
vercel env add NEXT_PUBLIC_API_URL
```

### Answer These Questions:

```
? What's the value of NEXT_PUBLIC_API_URL?
→ https://hackathon-ii-phase-i-todo-app-production.up.railway.app

? Add NEXT_PUBLIC_API_URL to which Environments?
→ Select all (Production, Preview, Development)
   - Use SPACE to select
   - Press ENTER when done
```

---

## Step 6: Deploy to Production

```bash
vercel --prod
```

This deploys to your production URL!

You'll see:
```
✅ Production: https://hackathon-ii-todo-app.vercel.app
```

**Copy this URL!** This is your live app!

---

## Step 7: Update Railway Backend CORS

1. Go to: https://railway.app/dashboard
2. Click your backend project
3. Go to **Variables** tab
4. Add/Update:
   ```
   Name:  FRONTEND_URL
   Value: https://hackathon-ii-todo-app.vercel.app
   ```
   (Use your actual Vercel URL from Step 6)

5. Save → Railway will auto-redeploy

---

## Step 8: Test Your App! 🎉

1. Visit your production URL from Step 6
2. Sign up for an account
3. Create, edit, delete tasks
4. Verify everything works!

---

## 🔄 Future Deployments (Auto-Deploy)

Now that you've deployed once, future deployments are automatic:

### For Preview Deployments:
```bash
git add .
git commit -m "Your changes"
git push origin main
```

Then in your project directory:
```bash
vercel
```

### For Production Deployments:
```bash
vercel --prod
```

---

## 📋 Useful CLI Commands

```bash
# View your deployments
vercel ls

# View project info
vercel project

# View logs
vercel logs

# Remove a deployment
vercel rm [deployment-url]

# Add more environment variables
vercel env add [VARIABLE_NAME]

# List environment variables
vercel env ls

# Link to existing project (for auto-deploy)
vercel link
```

---

## ✅ Verification Checklist

After deployment:

- [ ] Got production URL from `vercel --prod`
- [ ] Updated `FRONTEND_URL` in Railway
- [ ] Visited the production URL
- [ ] Successfully signed up
- [ ] Successfully logged in
- [ ] Can create tasks
- [ ] Can edit tasks
- [ ] Can delete tasks
- [ ] No console errors (F12 → Console)
- [ ] API calls work (F12 → Network shows 200 OK)

---

## 🆘 Troubleshooting

### Error: "Command not found: vercel"

**Fix**: Reinstall globally
```bash
npm install -g vercel
```

Or use npx (no install needed):
```bash
npx vercel
```

### Error: Build failed

**Fix**: Check build logs and ensure:
- `package.json` is at project root
- `next.config.ts` is at project root
- `app/` directory exists

### Error: CORS issues after deployment

**Fix**:
1. Double-check `FRONTEND_URL` in Railway matches your Vercel URL exactly
2. Make sure Railway backend redeployed
3. Clear browser cache (F12 → Application → Clear Storage)

---

## 🎯 Summary

You just deployed your app using Vercel CLI!

**Your app is live at**: `https://[your-project].vercel.app`

**Auto-deployment**: Run `vercel --prod` after each `git push` for production updates.

---

**Next**: Visit your app and share it with others! 🚀
