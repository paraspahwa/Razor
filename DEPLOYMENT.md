# Deployment Guide

## 🚀 Deploying AnimeForge

### 1. Backend Deployment (Railway/Render)

**Railway:**
1. Push code to GitHub
2. Connect Railway to repo
3. Add environment variables
4. Deploy

**Required Environment Variables:**
```
DATABASE_URL=postgresql://...
REPLICATE_API_TOKEN=r8_...
RAZORPAY_KEY_ID=rzp_test_...
RAZORPAY_KEY_SECRET=...
SUPABASE_URL=https://...
SUPABASE_KEY=eyJ...
SECRET_KEY=your-secret-key
```

### 2. Frontend Deployment (Vercel/Netlify)

**Vercel:**
1. Connect GitHub repo
2. Set build command: `npm run build`
3. Set output directory: `build`
4. Add environment variable: `REACT_APP_API_URL`

### 3. Database Setup

**Supabase:**
1. Create new project
2. Run SQL migrations
3. Get connection string
4. Add to environment variables

### 4. Payment Setup

**Razorpay:**
1. Create account at razorpay.com
2. Get API keys from dashboard
3. Set up webhook URL: `https://your-api.com/api/v1/payments/webhook`
4. Add webhook secret to env

### 5. AI Service Setup

**Replicate:**
1. Get API token from replicate.com
2. Add to environment variables
3. Ensure billing is enabled

---

Your app will be live at:
- Frontend: https://your-app.vercel.app
- Backend: https://your-api.railway.app
- API Docs: https://your-api.railway.app/docs
