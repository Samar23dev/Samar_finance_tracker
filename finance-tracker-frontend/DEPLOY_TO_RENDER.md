# Deploy React Frontend to Render

## Quick Deploy Steps

### 1. Push Frontend to GitHub
The frontend code is already in your repository under `finance-tracker-frontend/` folder.

### 2. Create New Static Site on Render

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New +" → "Static Site"
3. Connect your GitHub repository: `Samar23dev/Samar_finance_tracker`
4. Configure the service:

**Basic Settings:**
- **Name:** `finance-tracker-frontend` (or any name you prefer)
- **Root Directory:** `finance-tracker-frontend`
- **Build Command:** `npm install && npm run build`
- **Publish Directory:** `dist`

**Environment Variables:**
- `NODE_VERSION` = `18.17.0`
- `VITE_API_URL` = `https://samar-finance-tracker-1.onrender.com/api`

5. Click "Create Static Site"

### 3. Update Backend CORS

After deployment, you'll get a URL like: `https://finance-tracker-frontend-xxxx.onrender.com`

Update the backend CORS settings:
1. Go to backend service on Render
2. Add environment variable or update `settings.py`:
   ```python
   CORS_ALLOWED_ORIGINS = [
       "https://your-frontend-url.onrender.com",
       "http://localhost:5173",
   ]
   ```
3. Redeploy backend if needed

### 4. Test Your App

Visit your frontend URL and test:
- ✅ Registration
- ✅ Login
- ✅ Google OAuth
- ✅ Dashboard
- ✅ Transactions
- ✅ Categories
- ✅ Budgets

## Alternative: Deploy Using render.yaml

You can also use the included `render.yaml` file:

1. In Render Dashboard, click "New +" → "Blueprint"
2. Select your repository
3. Render will detect the `render.yaml` file
4. Review and create the service

## Environment Variables

The frontend uses these environment variables:

- **Development:** `.env.development`
  - `VITE_API_URL=http://localhost:8000/api`

- **Production:** `.env.production`
  - `VITE_API_URL=https://samar-finance-tracker-1.onrender.com/api`

Vite automatically loads the correct file based on the build mode.

## Troubleshooting

### CORS Errors
- Make sure backend CORS_ALLOWED_ORIGINS includes your frontend URL
- Check browser console for exact error
- Verify API_URL is correct in frontend

### API Connection Failed
- Check if backend is running: `https://samar-finance-tracker-1.onrender.com/api/`
- Verify VITE_API_URL environment variable
- Check network tab in browser dev tools

### Build Failures
- Ensure Node version is 18.x
- Check build logs for specific errors
- Verify all dependencies are in package.json

## Free Tier Notes

Render's free tier for static sites includes:
- ✅ 100 GB bandwidth/month
- ✅ Automatic SSL certificates
- ✅ Global CDN
- ✅ Automatic deploys from GitHub
- ✅ Custom domains

Perfect for your finance tracker frontend!
