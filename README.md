# 💰 Personal Finance Tracker

A comprehensive full-stack finance management application with AI-powered insights, built with Django REST Framework and React.

## ✨ Features

### Core Functionality
- ✅ User Authentication (Register, Login, Profile Management)
- ✅ Google OAuth Integration
- ✅ Transaction Management (Income, Expenses, Transfers)
- ✅ Budget Goals and Tracking
- ✅ Receipt Upload and Management
- ✅ Financial Dashboard with Charts
- ✅ Email Notifications (Mailgun)

### AI Features 🤖
- ✅ AI Financial Advisor (Google Gemini 2.5 Flash)
- ✅ Bank Statement Upload (PDF/CSV)
- ✅ Auto-Transaction Creation from Statements
- ✅ Smart Financial Recommendations

## 🛠️ Tech Stack

### Backend
- Django 6.0.2
- Django REST Framework
- PostgreSQL
- Google Gemini AI
- Mailgun (Email)
- WhiteNoise (Static Files)

### Frontend
- React 18
- Vite
- Axios
- Modern CSS

### Deployment
- Render (Backend & Frontend)
- PostgreSQL (Render)

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL 14+

### Backend Setup

1. Clone and navigate:
```bash
git clone https://github.com/Samar23dev/Samar_finance_tracker.git
cd Samar_finance_tracker
```

2. Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Setup environment variables:
```bash
copy .env.example .env
# Edit .env with your credentials
```

5. Run migrations:
```bash
python manage.py migrate
python manage.py create_superuser_if_none
python manage.py populate_sample_data
```

6. Start server:
```bash
python manage.py runserver
```

Backend runs at: http://localhost:8000

### Frontend Setup

1. Navigate to frontend:
```bash
cd finance-tracker-frontend
```

2. Install dependencies:
```bash
npm install
```

3. Setup environment:
```bash
copy .env.development .env
# Edit VITE_API_URL if needed
```

4. Start dev server:
```bash
npm run dev
```

Frontend runs at: http://localhost:5173

## 🔑 Environment Variables

### Backend (.env)
```env
# Django
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/finance_tracker

# Google OAuth
GOOGLE_CLIENT_ID=your-client-id
GOOGLE_CLIENT_SECRET=your-client-secret

# Google Gemini AI (Free at https://ai.google.dev/)
GEMINI_API_KEY=your-gemini-api-key

# Mailgun
MAILGUN_API_KEY=your-mailgun-key
MAILGUN_DOMAIN=your-mailgun-domain
```

### Frontend (.env)
```env
VITE_API_URL=http://localhost:8000/api
```

## 📡 API Endpoints

### Authentication
- `POST /api/auth/register/` - Register user
- `POST /api/auth/login/` - Login
- `POST /api/auth/google/` - Google OAuth
- `GET /api/auth/profile/` - User profile

### Transactions
- `GET /api/transactions/` - List transactions
- `POST /api/transactions/` - Create transaction
- `PUT /api/transactions/{id}/` - Update transaction
- `DELETE /api/transactions/{id}/` - Delete transaction

### AI Features
- `POST /api/ai/chat/` - Chat with AI advisor
- `GET /api/ai/chat/history/` - Get chat history
- `POST /api/ai/upload/` - Upload bank statement
- `GET /api/ai/statements/` - Get upload history

### Budget & Reports
- `GET /api/budgets/` - List budgets
- `POST /api/budgets/` - Create budget
- `GET /api/reports/monthly/` - Monthly report

## 🎯 AI Features Usage

### AI Chat Bot
1. Navigate to "AI Advisor" tab
2. Ask questions like:
   - "How can I save more money?"
   - "Analyze my spending patterns"
   - "Should I increase my budget?"

### Bank Statement Upload
1. Go to "Upload Statement" tab
2. Upload CSV or PDF file
3. AI automatically:
   - Extracts transactions
   - Categorizes them
   - Creates entries in your account
   - Detects duplicates

## 🌐 Production URLs

- **Backend**: https://samar-finance-tracker-1.onrender.com
- **Frontend**: https://finance-tracker-frontend-804q.onrender.com
- **GitHub**: https://github.com/Samar23dev/Samar_finance_tracker

## 📦 Project Structure

```
Samar_finance_tracker/
├── accounts/                 # User authentication & OAuth
├── transactions/             # Transaction management
├── ai_features/             # AI chat & bank upload
├── dashboard/               # Dashboard views
├── finance_tracker/         # Django settings
├── media/                   # Uploaded files
├── finance-tracker-frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── AIChat.jsx
│   │   └── BankUpload.jsx
│   └── package.json
├── requirements.txt
└── manage.py
```

## 🧪 Testing

Run backend tests:
```bash
python manage.py test
```

Test API endpoints:
```bash
python test_api.py
```

## 🚢 Deployment

### Render Deployment

1. Push to GitHub
2. Connect Render to your repo
3. Add environment variables
4. Deploy automatically

See deployment guides in the repo for detailed instructions.

## 🆓 Free Tier Services

- **Google Gemini**: 60 requests/min, completely free
- **Mailgun**: 5,000 emails/month
- **Render**: Free tier for web services
- **PostgreSQL**: Free 256MB database on Render

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open pull request

## 📄 License

MIT License

## 👨‍💻 Author

Samar Mittal
- GitHub: [@Samar23dev](https://github.com/Samar23dev)

## 🙏 Acknowledgments

- Google Gemini for free AI API
- Render for hosting
- Django & React communities

---

**Note**: This project was built as part of a full-stack development challenge, implementing modern web technologies with AI integration.
