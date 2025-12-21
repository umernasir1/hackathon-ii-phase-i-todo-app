# Deployment Guide - Phase II

This guide covers deploying the full-stack Todo application to production.

## Overview

- **Frontend**: Deploy to Vercel (recommended)
- **Backend**: Deploy to Railway, Render, or Fly.io
- **Database**: Neon PostgreSQL (already set up)

## Prerequisites

- GitHub repository with your code
- Neon PostgreSQL database created
- Accounts created on deployment platforms

## 🎯 Step 1: Deploy Backend

### Option A: Railway (Recommended)

1. **Create Account**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Select the `backend` directory

3. **Configure Environment Variables**
   - Go to Variables tab
   - Add these variables:
   ```
   DATABASE_URL=<your-neon-connection-string>
   JWT_SECRET=<generate-with-openssl-rand-hex-32>
   JWT_ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_DAYS=7
   FRONTEND_URL=https://your-app.vercel.app
   ```

4. **Configure Build Settings**
   - Root directory: `backend`
   - Build command: `pip install -r requirements.txt`
   - Start command: `python -m alembic upgrade head && python -m uvicorn main:app --host 0.0.0.0 --port $PORT`

5. **Deploy**
   - Railway will auto-deploy
   - Copy the public URL (e.g., `https://your-app.up.railway.app`)

### Option B: Render

1. **Create Account**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect GitHub repository
   - Name: "todo-backend"
   - Root directory: `backend`
   - Environment: Python 3
   - Build command: `pip install -r requirements.txt`
   - Start command: `python -m alembic upgrade head && python -m uvicorn main:app --host 0.0.0.0 --port $PORT`

3. **Add Environment Variables**
   ```
   DATABASE_URL=<your-neon-connection-string>
   JWT_SECRET=<generate-with-openssl-rand-hex-32>
   JWT_ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_DAYS=7
   FRONTEND_URL=https://your-app.vercel.app
   ```

4. **Deploy**
   - Click "Create Web Service"
   - Copy the public URL

## 🎯 Step 2: Deploy Frontend

### Vercel Deployment

1. **Create Account**
   - Go to [vercel.com](https://vercel.com)
   - Sign up with GitHub

2. **Import Project**
   - Click "Add New..." → "Project"
   - Import your GitHub repository
   - Framework preset: Next.js
   - Root directory: `frontend`

3. **Configure Environment Variables**
   - Go to Settings → Environment Variables
   - Add:
   ```
   NEXT_PUBLIC_API_URL=https://your-backend.up.railway.app
   ```
   (Use the backend URL from Step 1)

4. **Configure Build Settings**
   - Build command: `npm run build` (auto-detected)
   - Output directory: `.next` (auto-detected)
   - Install command: `npm install` (auto-detected)

5. **Deploy**
   - Click "Deploy"
   - Vercel will build and deploy
   - Copy the production URL (e.g., `https://your-app.vercel.app`)

6. **Update Backend CORS**
   - Go back to your backend deployment (Railway/Render)
   - Update `FRONTEND_URL` environment variable with your Vercel URL
   - Redeploy backend

## 🔄 Step 3: Final Configuration

### Update Backend CORS
Make sure your backend `FRONTEND_URL` environment variable matches your Vercel deployment URL.

### Test Production Deployment

1. **Test Backend Health**
   ```bash
   curl https://your-backend.up.railway.app/health
   # Should return: {"status":"healthy"}
   ```

2. **Test Frontend**
   - Open `https://your-app.vercel.app`
   - Sign up with a test account
   - Create a task
   - Verify all CRUD operations work

3. **Test Authentication**
   - Logout and login again
   - Verify JWT tokens work
   - Check tasks persist across sessions

## 📋 Deployment Checklist

### Backend
- [ ] Environment variables configured
- [ ] Database migrations run successfully
- [ ] Health endpoint returns 200
- [ ] CORS configured for frontend URL
- [ ] API documentation accessible at `/docs`

### Frontend
- [ ] Backend API URL configured
- [ ] Build completes without errors
- [ ] Authentication flow works
- [ ] All CRUD operations functional
- [ ] Responsive design works on mobile

### Security
- [ ] JWT secret is strong (32+ characters)
- [ ] Database credentials not exposed
- [ ] HTTPS enabled (automatic on Vercel/Railway)
- [ ] CORS only allows your frontend domain

## 🐛 Troubleshooting

### Backend Issues

**Migrations fail**:
- Check `DATABASE_URL` is correct
- Ensure Neon database is accessible
- Run migrations manually: `python -m alembic upgrade head`

**500 errors**:
- Check application logs on Railway/Render
- Verify all environment variables are set
- Test database connection

**CORS errors**:
- Verify `FRONTEND_URL` matches your Vercel deployment
- Check CORS middleware in `main.py`
- Redeploy backend after changing environment variables

### Frontend Issues

**Cannot connect to backend**:
- Verify `NEXT_PUBLIC_API_URL` is correct
- Check backend is running (test `/health` endpoint)
- Look for CORS errors in browser console

**Build fails**:
- Check TypeScript errors: `npm run build` locally
- Verify all dependencies in `package.json`
- Check Node.js version (18+ required)

**Authentication not working**:
- Verify JWT tokens are being sent
- Check browser console for errors
- Test backend auth endpoints directly

## 🔐 Security Best Practices

1. **JWT Secret**
   - Generate strong secret: `openssl rand -hex 32`
   - Never commit to Git
   - Rotate periodically in production

2. **Database**
   - Use Neon's connection pooling
   - Enable SSL mode (already in connection string)
   - Regularly backup data

3. **Environment Variables**
   - Never hardcode secrets
   - Use deployment platform's secrets management
   - Different values for dev/staging/prod

## 📊 Monitoring

### Backend Monitoring
- Railway/Render provides built-in metrics
- Monitor response times and error rates
- Set up alerts for downtime

### Frontend Monitoring
- Vercel Analytics (built-in)
- Monitor Core Web Vitals
- Track deployment frequency

## 🚀 Continuous Deployment

### Auto-Deploy on Push
Both Vercel and Railway support automatic deployments:

1. **Enable Auto-Deploy**
   - Railway/Vercel: Already enabled by default
   - Pushes to `main` branch trigger deployments

2. **Deploy Previews**
   - Vercel creates preview URLs for pull requests
   - Test changes before merging to main

## 📈 Scaling

### Backend Scaling
- **Railway**: Automatically scales based on load
- **Render**: Configure number of instances

### Database Scaling
- **Neon**: Upgrade plan if needed
- Free tier: 0.5 GB storage, 100 hours compute/month
- Monitor usage in Neon dashboard

## ✅ Production Readiness

Before launching:
- [ ] All tests pass
- [ ] Documentation updated
- [ ] Environment variables secured
- [ ] Monitoring configured
- [ ] Backup strategy in place
- [ ] SSL certificates active
- [ ] Performance tested
- [ ] Error handling verified

## 🎉 Deployment Complete!

Your full-stack Todo application is now live!

**Frontend**: `https://your-app.vercel.app`
**Backend**: `https://your-backend.up.railway.app`
**API Docs**: `https://your-backend.up.railway.app/docs`

Share your deployment URLs and enjoy your production app!

## 📞 Support

For deployment issues:
- **Vercel**: [vercel.com/docs](https://vercel.com/docs)
- **Railway**: [docs.railway.app](https://docs.railway.app)
- **Render**: [render.com/docs](https://render.com/docs)
- **Neon**: [neon.tech/docs](https://neon.tech/docs)
