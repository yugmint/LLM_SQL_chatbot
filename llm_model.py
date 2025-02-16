import os
import streamlit as st
from langchain.chat_models import init_chat_model

# Load API Key from Streamlit Secrets
grok_api_key = st.secrets.get("grok_api_key")

if not grok_api_key:
    raise ValueError("GROQ_API_KEY is missing! Make sure it's set in Streamlit Secrets.")

# Set environment variable securely
os.environ["GROQ_API_KEY"] = grok_api_key

def get_llm():
    """Initialize and return the LLM model."""
    return init_chat_model("llama3-8b-8192", model_provider="groq")

llm = get_llm()
