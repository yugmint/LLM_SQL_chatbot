import os
import streamlit as st
from langchain.chat_models import init_chat_model

# Debugging: Check if the key is retrieved correctly
grok_api_key = st.secrets.get("grok_api_key")

if grok_api_key:
    os.environ["GROQ_API_KEY"] = grok_api_key
else:
    st.error("❌ GROQ_API_KEY is missing! Check your Streamlit Secrets.")
    raise ValueError("GROQ_API_KEY is missing! Make sure it's set in Streamlit Secrets.")

def get_llm():
    """Initialize and return the LLM model."""
    return init_chat_model("llama3-8b-8192", model_provider="groq")

llm = get_llm()
