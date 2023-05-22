import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="ChatGPT Clone", page_icon=":robot_face:")
# st.write(OPENAI_API_KEY[0:3] + "*" * 32 + OPENAI_API_KEY[-3:])
st.title("ChatGPT Clone :robot_face:")

with st.sidebar:
    st.write("## About")
    st.write("This is a clone of [ChatGPT](https://chat.openai.com/)")
    user_input = st.text_input("You", value="", key="user_input", type="default")

message("Hello, How can I help you today?")
message("I'm user", is_user=True)
