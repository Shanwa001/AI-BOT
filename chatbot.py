import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st


load_dotenv()
os.environ["GROQ_API_KEY"]      =   os.getenv("GROQ_API_KEY")

llm  = ChatGroq(
                model           =   "llama3-70b-8192",
                temperature     =   0
                )

st.title("🤖 AI bot using LLAMA-3 ")
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []


for chats in st.session_state.chat_history:
    with st.chat_message(chats["role"]):
        st.markdown(chats['content'])



if user_input := st.chat_input("How Can I Help YOU"):
    with st.chat_message("User"):
        st.markdown(user_input)
        st.session_state.chat_history.append({"role":"User", "content": user_input})
    system_msg = {
                    "role"      : "system", 
                    "content"   : "'''You are name is irfa and you are AI assistant who helps to answer User queries'''" 
                }

    Human_msg   = {
                    "role"      : "user", 
                    "content"   : f"'''User Query:'{user_input}''''"
                }
    prompt      = [system_msg, Human_msg]

    llm_response = llm.invoke(prompt)
    with st.chat_message("Assistant"):
        st.markdown(llm_response.content)
        st.session_state.chat_history.append({"role":"Assistant", "content": llm_response.content})