# 🚀 Deploy Finance Tracker to Render

Complete guide to deploy your Django backend and React frontend to Render.

---

## 📋 Prerequisites

Before deploying, make sure you have:

1. ✅ GitHub account
2. ✅ Render account (sign up at https://render.com)
3. ✅ Your code pushed to GitHub repository
4. ✅ Gmail App Password (for email features)
5. ✅ Google OAuth credentials (optional, for Google login)

---

## 🎯 Deployment Overview

We'll deploy:
1. **Django Backend** → Render Web Service
2. **PostgreSQL Database** → Render PostgreSQL
3. **React Frontend** → Render Static Site (or Vercel/Netlify)

---

## Part 1: Prepare Your Code

### 1. Push Code to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Prepare for Render deployment"

# Create GitHub repository and push
git remote add origin https://github.com/YOUR_USERNAME/finance-tracker.git
git branch -M main
git push -u origin main
```

### 2. Verify Files Are Created

Make sure these files exist in your repository:
- ✅ `requirements.txt` - Python dependencies
- ✅ `build.sh` - Build script for Render
- ✅ `render.yaml` - Render configuration
- ✅ `runtime.txt` - Python version
- ✅ `.gitignore` - Git ignore rules

---

## Part 2: Deploy Backend to Render

### Step 1: Create New Web Service

1. Go to https://dashboard.render.com
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Select your `finance-tracker` repository

### Step 2: Configure Web Service

**Basic Settings:**
```
Name: finance-tracker-backend
Region: Oregon (US West)
Branch: main
Root Directory: (leave empty)
Runtime: Python 3
```

**Build & Deploy:**
```
Build Command: ./build.sh
Start Command: gunicorn finance_tracker.wsgi:application
```

**Instance Type:**
```
Free (or Starter if you need more resources)
```

### Step 3: Add Environment Variables

Click **"Advanced"** → **"Add Environment Variable"**

Add these variables:

#### Required Variables:

```bash
# Django Settings
SECRET_KEY=your-secret-key-here-generate-a-long-random-string
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com,localhost,127.0.0.1

# Database (Render will auto-populate DATABASE_URL)
# No need to add DATABASE_URL manually

# Email Configuration (Gmail SMTP)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=samarmittal123456789@gmail.com
EMAIL_HOST_PASSWORD=your_gmail_app_password_here
DEFAULT_FROM_EMAIL=samarmittal123456789@gmail.com
```

#### Optional Variables (for Google OAuth):

```bash
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
```

**How to generate SECRET_KEY:**
```python
# Run in Python shell
import secrets
print(secrets.token_urlsafe(50))
```

### Step 4: Create PostgreSQL Database

1. In Render Dashboard, click **"New +"** → **"PostgreSQL"**
2. Configure:
   ```
   Name: finance-tracker-db
   Database: finance_tracker
   User: finance_tracker_user
   Region: Oregon (same as web service)
   Plan: Free
   ```
3. Click **"Create Database"**
4. Wait for database to be created

### Step 5: Connect Database to Web Service

1. Go to your web service settings
2. Scroll to **"Environment"** section
3. Click **"Add Environment Variable"**
4. Add:
   ```
   Key: DATABASE_URL
   Value: [Select from database dropdown] → finance-tracker-db
   ```

### Step 6: Deploy!

1. Click **"Create Web Service"**
2. Render will automatically:
   - Install dependencies
   - Run migrations
   - Collect static files
   - Start the server
3. Wait 5-10 minutes for first deployment
4. Check logs for any errors

### Step 7: Verify Backend is Running

Once deployed, test your backend:

```bash
# Replace with your actual Render URL
https://your-app-name.onrender.com/admin
https://your-app-name.onrender.com/api/
```

You should see:
- Admin login page at `/admin`
- API root at `/api/`

---

## Part 3: Deploy Frontend to Render

### Option A: Deploy React to Render Static Site

#### Step 1: Update Frontend API URL

Edit `finance-tracker-frontend/src/App.jsx`:

```javascript
// Find this line (around line 20-30)
const API_URL = 'http://localhost:8000';

// Change to your Render backend URL
const API_URL = 'https://your-app-name.onrender.com';
```

#### Step 2: Build Frontend Locally

```bash
cd finance-tracker-frontend
npm run build
```

This creates a `dist/` folder with production build.

#### Step 3: Create Static Site on Render

1. Go to Render Dashboard
2. Click **"New +"** → **"Static Site"**
3. Connect your GitHub repository
4. Configure:
   ```
   Name: finance-tracker-frontend
   Branch: main
   Root Directory: finance-tracker-frontend
   Build Command: npm run build
   Publish Directory: dist
   ```
5. Click **"Create Static Site"**

#### Step 4: Update CORS Settings

Go back to your backend web service and update environment variables:

```bash
ALLOWED_HOSTS=your-backend.onrender.com,your-frontend.onrender.com,localhost
```

Add to `finance_tracker/settings.py` CORS settings:
```python
CORS_ALLOWED_ORIGINS = [
    "https://your-frontend.onrender.com",
    "http://localhost:5173",
]
```

Commit and push changes to trigger redeployment.

---

## Part 4: Configure Google OAuth (Optional)

### Step 1: Update Google OAuth Redirect URIs

1. Go to https://console.cloud.google.com
2. Select your project
3. Go to **"Credentials"**
4. Edit your OAuth 2.0 Client ID
5. Add Authorized Redirect URIs:
   ```
   https://your-backend.onrender.com/auth/google/callback/
   https://your-backend.onrender.com/accounts/google/login/callback/
   ```
6. Save changes

### Step 2: Update Environment Variables

In Render backend service, add:
```bash
GOOGLE_CLIENT_ID=your-client-id
GOOGLE_CLIENT_SECRET=your-client-secret
```

---

## Part 5: Post-Deployment Setup

### 1. Create Superuser

Access your backend shell:

1. Go to Render Dashboard → Your Web Service
2. Click **"Shell"** tab
3. Run:
   ```bash
   python manage.py createsuperuser
   ```
4. Follow prompts to create admin user

### 2. Test All Features

Visit your deployed app and test:
- ✅ User registration
- ✅ Login/Logout
- ✅ Create transactions
- ✅ Create budgets
- ✅ View dashboard
- ✅ Upload receipts
- ✅ Email reports
- ✅ Google OAuth (if configured)

### 3. Monitor Logs

Check logs for any errors:
1. Go to Render Dashboard
2. Click on your web service
3. Click **"Logs"** tab
4. Monitor for errors

---

## 🔧 Troubleshooting

### Issue: "Application failed to start"

**Solution:**
1. Check logs in Render Dashboard
2. Verify all environment variables are set
3. Make sure `build.sh` has execute permissions:
   ```bash
   chmod +x build.sh
   git add build.sh
   git commit -m "Make build.sh executable"
   git push
   ```

### Issue: "Database connection failed"

**Solution:**
1. Verify DATABASE_URL is set correctly
2. Make sure database and web service are in same region
3. Check database is running (green status)

### Issue: "Static files not loading"

**Solution:**
1. Run `python manage.py collectstatic` in shell
2. Verify WhiteNoise is in MIDDLEWARE
3. Check STATIC_ROOT and STATIC_URL settings

### Issue: "CORS errors in frontend"

**Solution:**
1. Update CORS_ALLOWED_ORIGINS in settings.py
2. Add frontend URL to ALLOWED_HOSTS
3. Redeploy backend

### Issue: "Email not sending"

**Solution:**
1. Verify Gmail App Password is correct
2. Check EMAIL_HOST_PASSWORD environment variable
3. Test email in Django shell:
   ```python
   from django.core.mail import send_mail
   send_mail('Test', 'Test message', 'from@example.com', ['to@example.com'])
   ```

### Issue: "Media files (receipts) not persisting"

**Solution:**
Render's free tier has ephemeral storage. For persistent media files:

**Option 1: Use Render Disk (Paid)**
1. Add persistent disk to your web service
2. Mount at `/opt/render/project/src/media`

**Option 2: Use Cloud Storage (Recommended)**
1. Use AWS S3, Cloudinary, or similar
2. Install `django-storages`
3. Configure in settings.py

---

## 📊 Render Free Tier Limits

**Web Service:**
- ✅ 750 hours/month (enough for 1 service)
- ✅ Sleeps after 15 min of inactivity
- ✅ Wakes up on request (takes ~30 seconds)

**PostgreSQL:**
- ✅ 1 GB storage
- ✅ 90 days retention
- ✅ Expires after 90 days (upgrade to keep)

**Static Site:**
- ✅ 100 GB bandwidth/month
- ✅ Always on (no sleep)
- ✅ Global CDN

---

## 🚀 Production Checklist

Before going live, ensure:

- [ ] DEBUG=False in production
- [ ] SECRET_KEY is strong and unique
- [ ] ALLOWED_HOSTS includes your domain
- [ ] CORS_ALLOWED_ORIGINS includes frontend URL
- [ ] Database backups enabled (paid plan)
- [ ] Email service configured and tested
- [ ] SSL/HTTPS enabled (automatic on Render)
- [ ] Environment variables secured
- [ ] Error monitoring set up (Sentry, etc.)
- [ ] Regular database backups scheduled

---

## 🎯 Alternative: Deploy Frontend to Vercel/Netlify

If you prefer Vercel or Netlify for frontend:

### Vercel:
1. Go to https://vercel.com
2. Import your GitHub repository
3. Set root directory: `finance-tracker-frontend`
4. Build command: `npm run build`
5. Output directory: `dist`
6. Add environment variable: `VITE_API_URL=https://your-backend.onrender.com`

### Netlify:
1. Go to https://netlify.com
2. Import your GitHub repository
3. Base directory: `finance-tracker-frontend`
4. Build command: `npm run build`
5. Publish directory: `dist`
6. Add environment variable: `VITE_API_URL=https://your-backend.onrender.com`

---

## 📝 Environment Variables Summary

### Backend (Render Web Service):

```bash
# Required
SECRET_KEY=<generate-random-string>
DEBUG=False
ALLOWED_HOSTS=your-app.onrender.com
DATABASE_URL=<auto-populated-by-render>

# Email (Gmail SMTP)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=<gmail-app-password>
DEFAULT_FROM_EMAIL=your-email@gmail.com

# Optional (Google OAuth)
GOOGLE_CLIENT_ID=<your-client-id>
GOOGLE_CLIENT_SECRET=<your-client-secret>
```

---

## 🎉 Success!

Your Finance Tracker is now deployed and accessible worldwide!

**Backend URL:** https://your-backend.onrender.com
**Frontend URL:** https://your-frontend.onrender.com
**Admin Panel:** https://your-backend.onrender.com/admin

---

## 📞 Support

**Render Documentation:**
- https://render.com/docs
- https://render.com/docs/deploy-django

**Common Issues:**
- Check Render status: https://status.render.com
- Community forum: https://community.render.com

---

*Deployment guide created: February 10, 2026*
*Ready for production deployment!* 🚀
