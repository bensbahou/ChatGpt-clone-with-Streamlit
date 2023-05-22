import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)


def init():
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    st.set_page_config(page_title="ChatGPT Clone", page_icon=":robot_face:")


init()

st.title("ChatGPT Clone :robot_face:")

with st.sidebar:
    st.write("## About")
    st.write("This is a clone of [ChatGPT](https://chat.openai.com/)")
    user_input = st.text_input("You", value="", key="user_input", type="default")


chat = ChatOpenAI(temperature=0.9)
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(
            content="You're now connected to a random person for a text chat."
        ),
    ]
if user_input:
    message(user_input, is_user=True)
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.spinner("Thinking..."):
        response = chat(messages=st.session_state.messages)
    message(response.content)
    st.session_state.messages.append(AIMessage(content=response.content))


# write messages contents in the end of the page
st.write(st.session_state.messages)
