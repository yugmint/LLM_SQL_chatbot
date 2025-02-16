import os
import getpass
from langchain.chat_models import init_chat_model

from config import config

# Load API Key securely
if not os.environ.get("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = config.get("grok_api_key")

def get_llm():
    """Initialize and return the LLM model."""
    return init_chat_model("llama3-8b-8192", model_provider="groq")

llm = get_llm()
