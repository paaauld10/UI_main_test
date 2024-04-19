import re
import warnings

import streamlit as st
# from snowflake.snowpark.exceptions import SnowparkSQLException

# from chain import load_chain

# from utils.snow_connect import SnowflakeConnection
# from utils.snowchat_ui import StreamlitUICallbackHandler, message_func
# from utils.snowddl import Snowddl

# warnings.filterwarnings("ignore")
# chat_history = []
# snow_ddl = Snowddl()

gradient_text_html = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap');

.gradient-text {
    font-family: 'Open Sans', sans-serif;
    font-weight: 700;
    background: -webkit-linear-gradient(left, violet, blue);
    background: linear-gradient(to right, violet, blue);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline;
    font-size: 3em;  /* Choose a suitable size for your application */
    /* Make the text shadow more obvious */
    text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.5);
}
</style>
<div class="gradient-text">Doraemon</div>
"""


st.markdown(gradient_text_html, unsafe_allow_html=True)

st.caption("Hello ako si Doramon at may mahiwagang batuta")

# model = st.radio(
#     "",
#     options=["mistral-large", "reka-flash", "mixtral-8x7b", "lama-2-70b-chat"],
#     index=0,
#     horizontal=True,
# )

model = st.selectbox(
    "Select a Model",  # Label for the selectbox
    options=["mistral-large", "reka-flash", "mixtral-8x7b", "lama-2-70b-chat"],
    index=0,  # Default option index (can be changed as per your preference)
)

st.session_state["model"] = model












































#################simple setup

# # from openai import OpenAI
# import streamlit as st

# st.title("☃️ GAME NA CHATBOT")
# st.button("CLICK MO KO DITO PRE")
# st.file_uploader("DITO KA UPLOAD MADAM")

# # Initialize the chat messages history
# if "messages" not in st.session_state.keys():
#     st.session_state.messages = [{"role": "assistant", "content": "How can I help?"}]

# # Prompt for user input and save
# if prompt := st.chat_input():
#     st.session_state.messages.append({"role": "user", "content": prompt})

# # display the existing chat messages
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.write(message["content"])

# # If last message is not from assistant, we need to generate a new response
# if st.session_state.messages[-1]["role"] != "assistant":
#     # Call LLM
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             r = OpenAI().chat.completions.create(
#                 messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
#                 model="gpt-3.5-turbo",
#             )
#             response = r.choices[0].message.content
#             st.write(response)

#     message = {"role": "assistant", "content": response}
#     st.session_state.messages.append(message)
