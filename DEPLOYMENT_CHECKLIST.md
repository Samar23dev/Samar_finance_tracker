# ✅ Deployment Checklist

Complete this checklist before and after deploying to Render.

---

## 📋 Pre-Deployment Checklist

### Code Preparation
- [ ] All code committed to Git
- [ ] `.env` file is in `.gitignore` (never commit secrets!)
- [ ] `requirements.txt` is up to date
- [ ] `build.sh` is executable
- [ ] `runtime.txt` specifies Python version
- [ ] All tests passing locally (if you have tests)

### Configuration Files
- [ ] `requirements.txt` exists
- [ ] `build.sh` exists
- [ ] `render.yaml` exists (optional but recommended)
- [ ] `runtime.txt` exists
- [ ] `Procfile` exists (backup)
- [ ] `.gitignore` includes sensitive files

### Django Settings
- [ ] `DEBUG=False` for production
- [ ] `SECRET_KEY` uses environment variable
- [ ] `ALLOWED_HOSTS` configured
- [ ] `DATABASES` uses `DATABASE_URL`
- [ ] `WhiteNoise` middleware added
- [ ] `CORS_ALLOWED_ORIGINS` configured
- [ ] Static files configuration correct

### Dependencies
- [ ] `gunicorn` in requirements.txt
- [ ] `whitenoise` in requirements.txt
- [ ] `dj-database-url` in requirements.txt
- [ ] `psycopg2-binary` in requirements.txt
- [ ] All other dependencies listed

---

## 🚀 Deployment Steps

### GitHub
- [ ] Repository created on GitHub
- [ ] Code pushed to `main` branch
- [ ] Repository is public or Render has access

### Render Account
- [ ] Render account created
- [ ] GitHub connected to Render
- [ ] Payment method added (if using paid features)

### Backend Deployment
- [ ] Web service created
- [ ] Repository connected
- [ ] Build command set: `./build.sh`
- [ ] Start command set: `gunicorn finance_tracker.wsgi:application`
- [ ] Python runtime selected
- [ ] Region selected (Oregon recommended)

### Database Setup
- [ ] PostgreSQL database created
- [ ] Database name: `finance_tracker`
- [ ] Same region as web service
- [ ] Database connected to web service

### Environment Variables
- [ ] `SECRET_KEY` set (50+ random characters)
- [ ] `DEBUG` set to `False`
- [ ] `ALLOWED_HOSTS` includes Render URL
- [ ] `DATABASE_URL` connected to database
- [ ] `EMAIL_BACKEND` configured
- [ ] `EMAIL_HOST` set to `smtp.gmail.com`
- [ ] `EMAIL_PORT` set to `587`
- [ ] `EMAIL_USE_TLS` set to `True`
- [ ] `EMAIL_HOST_USER` set (your Gmail)
- [ ] `EMAIL_HOST_PASSWORD` set (Gmail App Password)
- [ ] `DEFAULT_FROM_EMAIL` set
- [ ] `GOOGLE_CLIENT_ID` set (if using OAuth)
- [ ] `GOOGLE_CLIENT_SECRET` set (if using OAuth)

### First Deployment
- [ ] Deployment started
- [ ] Build logs checked for errors
- [ ] Deployment successful (green status)
- [ ] Service is live

---

## 🔍 Post-Deployment Verification

### Backend Health Check
- [ ] Backend URL accessible: `https://your-app.onrender.com`
- [ ] Admin panel loads: `https://your-app.onrender.com/admin`
- [ ] API root loads: `https://your-app.onrender.com/api/`
- [ ] No 500 errors in logs

### Database
- [ ] Migrations ran successfully
- [ ] Database tables created
- [ ] Can connect to database

### Admin Setup
- [ ] Superuser created via Shell
- [ ] Can login to admin panel
- [ ] Can view/edit data in admin

### API Testing
- [ ] `/api/auth/login/` works
- [ ] `/api/transactions/` accessible
- [ ] `/api/categories/` accessible
- [ ] `/api/budgets/` accessible
- [ ] `/api/dashboard/` accessible

### Static Files
- [ ] Admin CSS loads correctly
- [ ] No 404 errors for static files
- [ ] WhiteNoise serving files

### Media Files
- [ ] Can upload receipts
- [ ] Receipts accessible via URL
- [ ] Media files persist (or cloud storage configured)

### Email Service
- [ ] Email configuration correct
- [ ] Test email sent successfully
- [ ] Email reports working
- [ ] Budget alerts working (if configured)

### OAuth (if configured)
- [ ] Google OAuth redirect URIs updated
- [ ] Can login with Google
- [ ] OAuth callback works
- [ ] User created after OAuth login

---

## 🎨 Frontend Deployment

### Preparation
- [ ] API URL updated in frontend code
- [ ] Environment variables configured
- [ ] Build tested locally: `npm run build`
- [ ] No console errors

### Deployment
- [ ] Frontend deployed (Render/Vercel/Netlify)
- [ ] Frontend URL accessible
- [ ] Can connect to backend API
- [ ] No CORS errors

### Testing
- [ ] Can register new user
- [ ] Can login
- [ ] Can create transactions
- [ ] Can create budgets
- [ ] Dashboard loads with data
- [ ] Charts render correctly
- [ ] Can upload receipts
- [ ] Can send email reports
- [ ] Google OAuth works (if configured)

---

## 🔒 Security Checklist

### Django Security
- [ ] `DEBUG=False` in production
- [ ] `SECRET_KEY` is strong and unique
- [ ] `ALLOWED_HOSTS` properly configured
- [ ] HTTPS enabled (automatic on Render)
- [ ] CSRF protection enabled
- [ ] SQL injection protection (Django ORM)
- [ ] XSS protection enabled

### Environment Variables
- [ ] No secrets in code
- [ ] `.env` in `.gitignore`
- [ ] Environment variables in Render only
- [ ] Sensitive data encrypted

### Database
- [ ] Strong database password
- [ ] Database not publicly accessible
- [ ] Regular backups enabled (paid plan)
- [ ] Connection pooling configured

### API Security
- [ ] Authentication required for endpoints
- [ ] Token authentication working
- [ ] CORS properly configured
- [ ] Rate limiting considered (future)

---

## 📊 Monitoring Setup

### Logs
- [ ] Can access Render logs
- [ ] Error logging configured
- [ ] Log retention understood

### Performance
- [ ] Response times acceptable
- [ ] Database queries optimized
- [ ] Static files cached
- [ ] CDN configured (if needed)

### Uptime
- [ ] Uptime monitoring set up (UptimeRobot, etc.)
- [ ] Alerts configured
- [ ] Status page created (optional)

### Errors
- [ ] Error tracking set up (Sentry, etc.)
- [ ] Email alerts for errors
- [ ] Error dashboard accessible

---

## 🎯 Optional Enhancements

### Performance
- [ ] Redis cache configured
- [ ] Database connection pooling
- [ ] Query optimization
- [ ] Image optimization

### Storage
- [ ] Cloud storage for media files (S3, Cloudinary)
- [ ] CDN for static files
- [ ] Database backups automated

### Monitoring
- [ ] Application monitoring (New Relic, etc.)
- [ ] Performance monitoring
- [ ] User analytics
- [ ] Error tracking

### CI/CD
- [ ] Automated tests
- [ ] GitHub Actions configured
- [ ] Automatic deployments on push
- [ ] Staging environment

---

## 🐛 Troubleshooting Checklist

If something goes wrong:

### Build Failures
- [ ] Check build logs in Render
- [ ] Verify `build.sh` is executable
- [ ] Check all dependencies in requirements.txt
- [ ] Verify Python version in runtime.txt

### Runtime Errors
- [ ] Check application logs
- [ ] Verify environment variables
- [ ] Check database connection
- [ ] Verify static files collected

### Database Issues
- [ ] Check DATABASE_URL is set
- [ ] Verify migrations ran
- [ ] Check database is running
- [ ] Verify connection string

### CORS Errors
- [ ] Check CORS_ALLOWED_ORIGINS
- [ ] Verify ALLOWED_HOSTS
- [ ] Check frontend URL is correct
- [ ] Verify credentials allowed

### Email Issues
- [ ] Check Gmail App Password
- [ ] Verify EMAIL_HOST_PASSWORD
- [ ] Test email in Django shell
- [ ] Check spam folder

---

## 📝 Documentation

### Update Documentation
- [ ] README.md updated with deployment info
- [ ] API documentation updated
- [ ] Environment variables documented
- [ ] Deployment process documented

### Team Communication
- [ ] Team notified of deployment
- [ ] Deployment notes shared
- [ ] Known issues documented
- [ ] Rollback plan documented

---

## 🎉 Launch Checklist

### Final Checks
- [ ] All features tested in production
- [ ] Performance acceptable
- [ ] No critical bugs
- [ ] Backup plan ready
- [ ] Monitoring active

### Go Live
- [ ] DNS configured (if custom domain)
- [ ] SSL certificate active
- [ ] Users can access app
- [ ] Support channels ready

### Post-Launch
- [ ] Monitor logs for 24 hours
- [ ] Check error rates
- [ ] Verify email notifications
- [ ] Collect user feedback

---

## 📞 Support Contacts

**Render Support:**
- Documentation: https://render.com/docs
- Community: https://community.render.com
- Status: https://status.render.com

**Your Team:**
- Developer: [Your Name]
- Email: [Your Email]
- GitHub: [Your GitHub]

---

## ✅ Deployment Complete!

Once all items are checked:

- [ ] **Deployment successful** ✅
- [ ] **All features working** ✅
- [ ] **Monitoring active** ✅
- [ ] **Documentation updated** ✅
- [ ] **Team notified** ✅

**🎉 Congratulations! Your Finance Tracker is live!**

---

*Deployment checklist - Ensure nothing is missed!* ✅
