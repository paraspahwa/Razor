# AnimeForge - Complete Codebase

## 🎬 AI-Powered Avatar & Faceless Video Generator

Complete implementation of AnimeForge with all features from FacelessReels integrated.

### ✅ Features Implemented

**Phase 1: Foundation**
- User authentication (JWT)
- Database models (Users, Videos, Avatars, Payments)
- API structure with FastAPI

**Phase 2: Core AI**
- AI Avatar generation from text
- Avatar style transfer (Ghibli, Cyberpunk, etc.)
- Faceless video generation with AI voice
- Visual generation from script segments

**Phase 3: Editing**
- Avatar editor with expressions
- Video timeline editor
- Caption generation
- Background music mixing

**Phase 4: Payments & Mobile**
- Razorpay integration (India)
- Stripe integration (International)
- Subscription management
- React Native mobile app

**FacelessReels Features Added:**
- Auto-publishing to social media
- Series/channel creation
- 3-step video workflow
- Multiple art styles
- Background music upload
- Animated captions
- Vertical video format (9:16)

### 📁 Project Structure

```
animeforge/
├── backend/
│   ├── app/
│   │   ├── api/v1/endpoints/    # API routes
│   │   ├── core/                # Config & security
│   │   ├── db/                  # Database
│   │   ├── models/              # SQLAlchemy models
│   │   ├── schemas/             # Pydantic schemas
│   │   └── services/            # Business logic
│   ├── main.py                  # Entry point
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── pages/               # React pages
│   │   ├── store/               # Zustand stores
│   │   └── lib/                 # API client
│   └── package.json
└── mobile/                      # React Native app
```

### 🚀 Quick Start

**Backend:**
```bash
cd backend
pip install -r requirements.txt
# Copy .env.example to .env and fill in your keys
uvicorn main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm start
```

**Environment Variables:**
- `REPLICATE_API_TOKEN` - For AI generation
- `RAZORPAY_KEY_ID/SECRET` - For payments
- `SUPABASE_URL/KEY` - For database

### 💰 Pricing Plans (INR)

| Plan | Price | Features |
|------|-------|----------|
| Free | ₹0 | 1 Avatar, 2 Videos |
| Starter | ₹199/mo | 5 Avatars, 10 Videos |
| Creator | ₹499/mo | 15 Avatars, 50 Videos |
| Pro | ₹999/mo | Unlimited everything |

### 📝 API Endpoints

- `POST /api/v1/auth/register` - Register user
- `POST /api/v1/auth/login` - Login
- `POST /api/v1/videos/generate-faceless` - Create faceless video
- `POST /api/v1/avatars/generate` - Generate avatar
- `GET /api/v1/payments/plans` - Get pricing plans

### 🔗 GitHub Repository

Your repository: https://github.com/paraspahwa/animeforge.git

---

Built with ❤️ using React, FastAPI, and Replicate AI.
