# AI Features Setup

## Quick Setup

### 1. Install Dependencies
```bash
pip install openai==0.28.1 PyPDF2==3.0.1
```

### 2. Get OpenAI API Key
1. Go to https://platform.openai.com/
2. Sign up/login
3. Create API key
4. Add to `.env`:
```env
OPENAI_API_KEY=sk-your-key-here
```

### 3. Run Migrations
```bash
python manage.py makemigrations ai_features
python manage.py migrate
```

### 4. Start Server
```bash
python manage.py runserver
```

## API Endpoints

### Chat Bot
**POST** `/api/ai/chat/`
```json
{
  "message": "How can I save money?"
}
```

**Response:**
```json
{
  "message": "How can I save money?",
  "response": "Here are some tips..."
}
```

### Upload Bank Statement
**POST** `/api/ai/upload/`
- Upload PDF or CSV file
- Get AI analysis

**Response:**
```json
{
  "id": 1,
  "file_name": "statement.pdf",
  "analysis": "Total income: $5000...",
  "uploaded_at": "2026-02-10T..."
}
```

### Chat History
**GET** `/api/ai/chat/history/`

### Statement History
**GET** `/api/ai/statements/`

## Testing

### Test Chat
```bash
curl -X POST http://localhost:8000/api/ai/chat/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello!"}'
```

### Test Upload
```bash
curl -X POST http://localhost:8000/api/ai/upload/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -F "file=@statement.pdf"
```

## Frontend Integration

Add these to your React app:

### 1. Chat Component
```javascript
const [message, setMessage] = useState('');
const [response, setResponse] = useState('');

const sendMessage = async () => {
  const res = await fetch('/api/ai/chat/', {
    method: 'POST',
    headers: {
      'Authorization': `Token ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ message })
  });
  const data = await res.json();
  setResponse(data.response);
};
```

### 2. Upload Component
```javascript
const uploadFile = async (file) => {
  const formData = new FormData();
  formData.append('file', file);
  
  const res = await fetch('/api/ai/upload/', {
    method: 'POST',
    headers: {
      'Authorization': `Token ${token}`
    },
    body: formData
  });
  const data = await res.json();
  console.log(data.analysis);
};
```

## Cost Estimate

- Chat: ~$0.001 per message
- File analysis: ~$0.01 per file
- Monthly (100 chats + 10 files): ~$0.20

## Deploy to Render

1. Push code to GitHub
2. Add to Render environment variables:
```
OPENAI_API_KEY=sk-your-key-here
```
3. Deploy!

## Done!

You now have:
✅ AI Chat Bot
✅ Bank Statement Upload & Analysis
✅ Chat History
✅ Statement History
