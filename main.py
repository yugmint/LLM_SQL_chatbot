import streamlit as st
from chatbot_logic import build_chatbot_graph
import warnings

warnings.filterwarnings("ignore")

# Initialize chatbot graph
graph = build_chatbot_graph()

# Streamlit App Title
st.set_page_config(page_title="SQL Chatbot", layout="centered")
st.title("💬 SQL-Powered Chatbot")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask me anything about your database...")

if user_input:
    # Add user query to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Process user query
    final_answer = ""
    for step in graph.stream({"question": user_input}, stream_mode="updates"):
        if "generate_answer" in step and "answer" in step["generate_answer"]:
            final_answer = step["generate_answer"]["answer"]

    # Add bot response to chat history
    with st.chat_message("assistant"):
        st.markdown(final_answer)

    st.session_state.messages.append({"role": "assistant", "content": final_answer})
