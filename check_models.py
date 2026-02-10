"""Check available Gemini models"""
from google import genai
from decouple import config

api_key = config('GEMINI_API_KEY', default='')
if not api_key:
    print("No API key found!")
    exit()

client = genai.Client(api_key=api_key)

print("Available Gemini models:")
print("-" * 50)

try:
    models = client.models.list()
    for model in models:
        print(f"✅ {model.name}")
        if hasattr(model, 'supported_generation_methods'):
            print(f"   Methods: {model.supported_generation_methods}")
        print()
except Exception as e:
    print(f"Error: {e}")
