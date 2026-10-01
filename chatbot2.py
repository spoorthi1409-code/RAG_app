import streamlit as st
from ollama import chat
st.set_page_config(page_title="Ollama Chatbot", page_icon=":robot_face:")
st.title("Ollama Chatbot-here to help you with your queries")

personality = "Friendly and a humourous tutor named alex .Answer warmly . keep answers short and concise. Use emojis in your answers."
personality_2 = "You are a strict but fair tutor named Sarah. Provide detailed explanations and use formal language."   
if "history" not in st.session_state:
    st.session_state.history = [{'role': 'system', 'content': personality}]

if "toast_msg" not in st.session_state:
    st.session_state.toast_msg = None

if st.session_state.toast_msg:
    st.toast(st.session_state.toast_msg[0],st.session_state.toast_msg[1])
    st.session_state.toast_msg = None

with st.sidebar:
    st.write("chat controls")
    if st.button("clear chat", type="primary"):
        st.session_state.history = [{'role': 'system', 'content': personality}]
        st.rerun()
    if st.button("change personality"):
        st.session_state.history[0]["content"] = personality_2
        st.session_state.toast_msg = ("chat cleared successfully", "success")
        st.rerun()
        
with st.chat_message("assistant"):
    st.write("Hello! I'm Alex, your friendly and humorous tutor. How can I assist you today? 😄")

for msg in st.session_state.history[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question = st.chat_input("Ask me anything...")
if question:
    st.session_state.history.append({"role": "user", "content": question})
    with st.chat_message("user" ):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat(model="llama3.2", messages=st.session_state.history)
            reply = response['message']['content']
            st.session_state.history.append({"role": "assistant", "content": reply})
            st.write(reply)