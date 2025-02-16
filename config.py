import streamlit as st

def load_config():
    return st.secrets["database"]  # Load from Streamlit Secrets

config = load_config()