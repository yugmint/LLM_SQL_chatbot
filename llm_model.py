import os
import streamlit as st
from langchain.chat_models import init_chat_model

# Debugging: Print all secrets to check the structure
st.write("Secrets:", st.secrets)

try:
    # Access nested API key correctly
    grok_api_key = st.secrets["api"]["grok_api_key"]
except KeyError:
    st.error("❌ Error: Could not find 'grok_api_key' in Streamlit Secrets. Check your secrets file.")
    raise ValueError("GROQ_API_KEY is missing! Make sure it's set in Streamlit Secrets.")

# Set environment variable
os.environ["GROQ_API_KEY"] = grok_api_key

def get_llm():
    """Initialize and return the LLM model."""
    return init_chat_model("llama3-8b-8192", model_provider="groq")

llm = get_llm()
