#!/bin/bash
# AnimeForge Setup Script

echo "🚀 Setting up AnimeForge..."

# Backend setup
echo "📦 Setting up backend..."
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Frontend setup
echo "📦 Setting up frontend..."
cd ../frontend
npm install

# Mobile setup
echo "📦 Setting up mobile app..."
cd ../mobile
npm install

echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Copy backend/.env.example to backend/.env"
echo "2. Fill in your API keys in .env"
echo "3. Run: cd backend && uvicorn main:app --reload"
echo "4. Run: cd frontend && npm start"
