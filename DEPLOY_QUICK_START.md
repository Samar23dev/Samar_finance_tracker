# 🚀 Quick Deploy to Render (5 Minutes)

Fast track deployment guide for Finance Tracker.

---

## ⚡ Quick Steps

### 1. Push to GitHub (2 minutes)

```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

### 2. Create Render Account (1 minute)

- Go to https://render.com
- Sign up with GitHub
- Authorize Render to access your repositories

### 3. Deploy Backend (2 minutes)

1. **Create Web Service:**
   - Click "New +" → "Web Service"
   - Select your repository
   - Name: `finance-tracker-backend`
   - Build Command: `./build.sh`
   - Start Command: `gunicorn finance_tracker.wsgi:application`

2. **Add Environment Variables:**
   ```bash
   SECRET_KEY=<generate-random-50-char-string>
   DEBUG=False
   ALLOWED_HOSTS=*.onrender.com
   EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=samarmittal123456789@gmail.com
   EMAIL_HOST_PASSWORD=<your-gmail-app-password>
   DEFAULT_FROM_EMAIL=samarmittal123456789@gmail.com
   ```

3. **Create Database:**
   - Click "New +" → "PostgreSQL"
   - Name: `finance-tracker-db`
   - Click "Create Database"

4. **Connect Database:**
   - Go back to web service
   - Add environment variable:
     - Key: `DATABASE_URL`
     - Value: Select `finance-tracker-db` from dropdown

5. **Deploy:**
   - Click "Create Web Service"
   - Wait 5-10 minutes

### 4. Create Admin User

Once deployed:
1. Go to your web service
2. Click "Shell" tab
3. Run:
   ```bash
   python manage.py createsuperuser
   ```

### 5. Test Your App

Visit: `https://your-app-name.onrender.com/admin`

---

## 🎯 That's It!

Your backend is now live at: `https://your-app-name.onrender.com`

---

## 📝 Next Steps

1. **Deploy Frontend:**
   - Update API URL in `finance-tracker-frontend/src/App.jsx`
   - Deploy to Render Static Site or Vercel

2. **Configure OAuth:**
   - Add redirect URIs in Google Console
   - Add GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET to Render

3. **Test Everything:**
   - Create transactions
   - Test email reports
   - Upload receipts

---

## 🔧 Quick Fixes

**App not starting?**
```bash
# Make build.sh executable
chmod +x build.sh
git add build.sh
git commit -m "Fix build script"
git push
```

**Database errors?**
- Make sure DATABASE_URL is connected
- Check database is in same region as web service

**CORS errors?**
- Add frontend URL to ALLOWED_HOSTS
- Update CORS_ALLOWED_ORIGINS in settings.py

---

## 📞 Need Help?

See full guide: `RENDER_DEPLOYMENT_GUIDE.md`

---

*Quick start guide - Get deployed in 5 minutes!* ⚡
