import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
import nltk


st.set_page_config(
    page_title="Threat Intel: Fake News Detector", 
    page_icon="🛡️", 
    layout="wide"
)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103130.png", width=100) # Add a generic security icon
    st.title("About the Engine")
    st.info("This tool uses Natural Language Processing (NLP) and Logistic Regression to classify text integrity.")
    st.write("---")
    st.write("**Model Accuracy:** 92%")
    st.write("**Vectorization:** TF-IDF")

# Create two columns with a 60/40 width ratio
col1, col2 = st.columns([6, 4])

with col1:
    st.markdown("### 📝 Input Article")
    user_input = st.text_area("Paste the news text here:", height=300)
    analyze_button = st.button("Run Analysis", use_container_width=True)

with col2:
    st.markdown("### 📊 Forensic Analysis Results")
    # The results will go here when the button is clicked

import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
import nltk

# 1. Page Config
st.set_page_config(page_title="Fake News Detector", page_icon="🛡️", layout="wide")

# Ensure stop words are downloaded quietly
try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

# Load the saved model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    cleaned_words = [w for w in words if w not in stop_words]
    return ' '.join(cleaned_words)

# 2. Sidebar
with st.sidebar:
    st.title("🔍 Digital Forensics")
    st.info("This AI scans structural patterns, keyword frequencies, and vocabulary to flag deceptive content.")
    st.write("---")
    st.write("### Engine Specs")
    st.write("- **Algorithm:** Logistic Regression")
    st.write("- **Feature Extraction:** TF-IDF")
    st.write("---")
    st.caption("Developed for Mini-Project Demo")

# Main Header
st.title("Misinformation Detection Terminal")
st.write("Analyze text for signs of fabricated news.")

# 3. Column Layout
col1, col2 = st.columns([6, 4])

with col1:
    st.markdown("### 📝 Target Text")
    user_input = st.text_area("Paste the article or headline below:", height=250)
    analyze_button = st.button("Run AI Analysis", type="primary", use_container_width=True)

with col2:
    st.markdown("### 📊 Verdict")
    if analyze_button:
        if user_input.strip() == "":
            st.warning("Please provide text to analyze.")
        else:
            with st.spinner("Analyzing text patterns..."):
                cleaned_input = clean_text(user_input)
                vectorized_input = vectorizer.transform([cleaned_input])
                prediction = model.predict(vectorized_input)
                
                st.write("---")
                if prediction[0] == 1:
                    st.error("🚨 **THREAT DETECTED**")
                    st.write("The model classifies this text as **FAKE NEWS**.")
                    st.progress(100) # Visual indicator
                else:
                    st.success("✅ **CLEAN**")
                    st.write("The model classifies this text as **REAL NEWS**.")
                    st.progress(100)
    else:
        st.info("Awaiting input. Click 'Run AI Analysis' to see results here.")