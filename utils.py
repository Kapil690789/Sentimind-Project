from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

def get_api_key():
    """Fetch API Key securely from Streamlit secrets or .env"""
    try:
        return st.secrets["GOOGLE_API_KEY"]
    except:
        return os.getenv("GOOGLE_API_KEY")

def get_client():
    """Initialize the new GenAI Client"""
    api_key = get_api_key()
    if not api_key:
        st.error("⚠️ API Key missing! Please check your .env file.")
        return None
    return genai.Client(api_key=api_key)

def get_sentiment_analysis(user_text):
    """
    Analyzes text using the best available Gemini model.
    """
    client = get_client()
    if not client:
        return "System Error: Client not initialized."

    # Prompt Engineering
    sys_instruction = """
    Act as 'Sentimind', a professional AI Mental Health Assistant.
    Analyze the user's text and provide a structured report in Markdown:
    1. **Emotional State**: (Positive/Negative/Neutral) & specific emotion.
    2. **Risk Assessment**: (Low/Medium/High) signs of stress/anxiety/depression.
    3. **Empathetic Feedback**: Validate their feelings kindly.
    4. **Coping Strategy**: A simple, actionable suggestion (breathing, walk, etc.).
    """

    # List of models to try (Based on your test_api.py results)
    models_to_try = [
        "gemini-2.5-flash",       # Latest Stable
        "gemini-2.0-flash-exp",   # Experimental Fast
        "gemini-1.5-flash",       # Reliable Fallback
    ]

    for model_name in models_to_try:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=user_text,
                config=types.GenerateContentConfig(
                    system_instruction=sys_instruction,
                    temperature=0.7
                )
            )
            return response.text
        except Exception:
            continue  # Agar ek model fail ho, toh agla try karo
            
    return "⚠️ Error: Could not connect to AI. Please check your internet or API Quota."