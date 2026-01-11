import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ Error: API Key not found in .env file")
else:
    genai.configure(api_key=api_key)
    print(f"✅ API Key Found: {api_key[:5]}...*****")
    print("\n🔍 Checking available models for your key...")
    
    try:
        found = False
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"   - {m.name}")
                found = True
        if not found:
            print("⚠️ No content generation models found. Check your API Key permissions.")
    except Exception as e:
        print(f"❌ Error fetching models: {e}")