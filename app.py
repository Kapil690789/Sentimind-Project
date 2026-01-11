import streamlit as st
import utils

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Sentimind | Mental Health Monitor",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- SESSION STATE ---
if 'history' not in st.session_state:
    st.session_state['history'] = []

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3062/3062634.png", width=80)
    st.title("Sentimind")
    st.subheader("Mental Health Monitoring System")
    st.markdown("---")
    st.info("**Developer:** Kapil\n\n**Roll No:** 220010130101")
    st.success("**Guide:** Prof. Om Prakash Sangwan")
    st.caption("© 2026 GJU, Hisar")

# --- MAIN LAYOUT ---
st.title("🧠 Sentimind: AI-Powered Mental Health Analyzer")
st.markdown("An intelligent system for early detection of emotional distress using Gemini 2.0 AI.")

# Tabs
tab1, tab2, tab3 = st.tabs(["📊 Live Analysis", "📝 Session History", "ℹ️ About"])

# --- TAB 1: LIVE ANALYSIS ---
with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("How are you feeling?")
        user_input = st.text_area(
            "Share your thoughts:", 
            height=150,
            placeholder="Example: I am feeling very anxious about my exams..."
        )
        analyze_btn = st.button("Analyze Mental State", type="primary")

    with col2:
        st.info("💡 **Tip:** Detailed text gives better results.")
        st.warning("⚠️ **Disclaimer:** Not for medical diagnosis.")

    # Logic (UPDATED: No configure_genai call)
    if analyze_btn:
        if user_input.strip():
            with st.spinner("Sentimind is analyzing (Using Gemini 2.0)..."):
                # Direct call to analysis function
                result = utils.get_sentiment_analysis(user_input)
                
                st.session_state['history'].append({"input": user_input, "output": result})
                
                st.markdown("### 📋 Analysis Report")
                st.markdown("---")
                st.markdown(result)
        else:
            st.error("Please enter some text.")

# --- TAB 2: HISTORY ---
with tab2:
    st.subheader("Session History")
    for i, item in enumerate(reversed(st.session_state['history'])):
        with st.expander(f"Entry #{len(st.session_state['history'])-i}"):
            st.write(f"**Input:** {item['input']}")
            st.markdown(item['output'])

# --- TAB 3: ABOUT ---
with tab3:
    st.markdown("""
    ### Project Overview
    **Sentimind** uses advanced AI (Gemini 2.0 Flash) to analyze sentiment and mental health indicators.
    
    **Tech Stack:**
    * Python & Streamlit
    * Google GenAI SDK (New)
    * Natural Language Processing
    """)