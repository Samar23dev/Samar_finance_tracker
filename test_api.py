"""
Quick test script for AI features
"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000/api"

# Create user and get token
print("Creating test user...")
user_data = {
    "username": "aitest",
    "email": "aitest@example.com",
    "password": "test123456",
    "password2": "test123456",
    "first_name": "AI",
    "last_name": "Test"
}

try:
    response = requests.post(f"{BASE_URL}/users/", json=user_data)
    print(f"User creation: {response.status_code}")
except:
    print("User might already exist")

# Login
print("\nLogging in...")
login_data = {
    "username": "aitest",
    "password": "test123456"
}
response = requests.post(f"{BASE_URL}/auth/login/", json=login_data)
if response.status_code == 200:
    token = response.json()['token']
    print(f"✅ Got token: {token[:20]}...")
    
    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }
    
    # Test chat
    print("\n--- Testing AI Chat ---")
    chat_data = {"message": "Hello! Can you help me save money?"}
    response = requests.post(f"{BASE_URL}/ai/chat/", json=chat_data, headers=headers)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"Message: {data['message']}")
        print(f"Response: {data['response']}")
    else:
        print(f"Error: {response.text}")
    
    # Test chat history
    print("\n--- Testing Chat History ---")
    response = requests.get(f"{BASE_URL}/ai/chat/history/", headers=headers)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        history = response.json()
        print(f"Chat history count: {len(history)}")
    
    # Test file upload (create a sample CSV)
    print("\n--- Testing File Upload ---")
    csv_content = """Date,Description,Amount
2026-02-01,Salary,5000
2026-02-02,Grocery Store,-150
2026-02-03,Restaurant,-45
2026-02-04,Gas Station,-60
2026-02-05,Electric Bill,-120
"""
    
    with open('test_statement.csv', 'w') as f:
        f.write(csv_content)
    
    with open('test_statement.csv', 'rb') as f:
        files = {'file': ('test_statement.csv', f, 'text/csv')}
        response = requests.post(f"{BASE_URL}/ai/upload/", files=files, headers={'Authorization': f"Token {token}"})
    
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"File: {data['file_name']}")
        print(f"Analysis:\n{data['analysis']}")
    else:
        print(f"Error: {response.text}")
    
    print("\n✅ All tests completed!")
else:
    print(f"❌ Login failed: {response.text}")
