# Import dependencies
from dataclasses import dataclass
from typing import Literal

import streamlit as st
import streamlit.components.v1 as components

from langchain import OpenAI
from langchain.callbacks import get_openai_callback
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationSummaryMemory

@dataclass
class Message:
    """ Keeping track of a chat message"""
    origin: Literal["human", "ai"]
    message: str

# Function to load CSS
def load_css():
    css = """
    <style>
        .chat-row {
            display: flex;
            align-items: center;
            margin-top: 10px;
            margin-bottom: 10px;
            word-break: break-all;
        }
        .ai-bubble {
            background-color: #eee;
            border-radius: 10px;
            padding: 10px;
            margin-left: 10px;
        }
        .human-bubble {
            background-color: #70B7FD;
            color: white;
            border-radius: 10px;
            padding: 10px;
            margin-right: 10px;
        }
        .chat-icon {
            margin-right: 10px;
        }
        .row-reverse {
            flex-direction: row-reverse;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Function to initialize session state
def initialize_session_state():
    # Creating session variables if non existant
    if "history" not in st.session_state:
        st.session_state.history = []
    if "token_count" not in st.session_state:
        st.session_state.token_count = 0
    if "conversation" not in st.session_state:
        llm = OpenAI(
        temperature=0,
        openai_api_key=st.secrets["openai_api_key"],
        model_name="text-davinci-003"
    )
        st.session_state.conversation = ConversationChain(
            llm=llm,
            memory=ConversationSummaryMemory(llm=llm),
        )

# Function called on submit button click
def on_submit():
    with get_openai_callback() as cb:
        human_prompt = st.session_state.human_prompt
        llm_response = st.session_state.conversation.run(human_prompt)
        st.session_state.history.append(Message("human", human_prompt))
        st.session_state.history.append(Message("ai", llm_response))
        st.session_state.token_count += cb.total_tokens

# Displaying the app and piecing it all together
# Loading CSS
load_css()

# Initializing session state
initialize_session_state()

# Displaying title
st.title("Ryan GPT🤖")

# Defining placeholders for the app
chat_placeholder = st.empty()
prompt_placeholder = st.form("chat-form")
credit_card_placeholder = st.empty()

# Displaying the chat history
with chat_placeholder:
    for chat in st.session_state.history:
        div = f"""
        <div class="chat-row {'row-reverse' if chat.origin == 'human' else ''}">
            <img class="chat-icon" src="https://storage.googleapis.com/groundai-web-prod/media%2Fusers%2Fuser_14%2Fproject_387142%2Fimages%2FMan_1024.png" width=25 height=25>
            <div class="chat-bubble {'ai-bubble' if chat.origin == 'ai' else 'human-bubble'}">
                &#8203;{chat.message}
            </div>
        </div>
        """
        st.markdown(div, unsafe_allow_html=True)
    for _ in range(3):
        st.write('')

# Getting user input
with prompt_placeholder:
    cols = st.columns((6, 1))
    cols[0].text_input("Chat", value="Hello bot", label_visibility="collapsed", key="human_prompt")
    cols[1].form_submit_button("Submit", on_click=on_submit)

credit_card_placeholder.caption(f"""
    Used {st.session_state.token_count} tokens
    Debug Langchain conversation: 
    {st.session_state.conversation.memory.buffer}
""")

# Adding Javascript to submit the form on 'Enter' press
components.html("""
    <script>
        const streamlitDoc = window.parent.document;

        const buttons = Array.from(streamlitDoc.querySelectorAll('.stButton > button'));
        const submitButton = buttons.find((el) => el.innerText === 'Submit');

        streamlitDoc.addEventListener('keydown', function(e) {
            switch (e.key) {
                case 'Enter':
                    submitButton.click();
                    break;
            }
        });
    </script>
""")    
