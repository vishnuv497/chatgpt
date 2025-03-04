import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"

st.title("Chatbot using OpenAI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.text_input("You:", "")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        reply = response["choices"][0]["message"]["content"]
        st.session_state.messages.append({"role": "assistant", "content": reply})
        
        with st.chat_message("assistant"):
            st.markdown(reply)
    except Exception as e:
        st.error(f"Error: {e}")
