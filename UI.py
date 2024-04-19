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

st.markdown(
    """
    <style>
    /* Customize the selectbox label */
    label[for="Select a Model"] {
        font-family: 'Arial', sans-serif;  /* Change font style */
        font-size: 1.2em;  /* Adjust font size */
        font-weight: bold;  /* Make the label bold */
        color: #4B0082;  /* Set text color to indigo/violet */
    }

    /* Customize the selectbox */
    div[data-baseweb="select"] {
        /* Apply violet to blue gradient background */
        background: -webkit-linear-gradient(left, violet, blue);
        background: linear-gradient(to right, violet, blue);
        color: white;  /* Text color */
        border-radius: 8px;  /* Rounded corners */
        padding: 10px;  /* Padding around the content */
        box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.3);  /* Add shadow to the selectbox */
    }

    /* Customize the dropdown options */
    div[data-baseweb="menu"] {
        background: -webkit-linear-gradient(left, violet, blue);
        background: linear-gradient(to right, violet, blue);
        color: white;  /* Text color */
    }

    /* Customize the dropdown option hover effect */
    div[data-baseweb="menu"] :hover {
        background-color: #7B1FA2;  /* Darker shade for hover effect */
    }
    </style>
    """,
    unsafe_allow_html=True
)

model = st.selectbox(
    "Select a Model",  # Label for the selectbox
    options=["mistral-large", "reka-flash", "mixtral-8x7b", "lama-2-70b-chat"],
    index=0,  # Default option index
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
