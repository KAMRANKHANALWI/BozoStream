import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from langchain.globals import set_verbose

# Set verbosity (optional, set to True if you want debug logs)
set_verbose(False)

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize the ChatGroq LLM
llm = ChatGroq(
    temperature=0.2,
    model_name="llama-3.3-70b-versatile",
    # model_name="deepseek-r1-distill-llama-70b",
    groq_api_key=groq_api_key,
)

# Initialize Streamlit UI and Session State
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Full history for display
if "context" not in st.session_state:
    st.session_state.context = []  # Limited to the last 5 exchanges for LLM processing
if "conversations" not in st.session_state:
    st.session_state.conversations = {"Chat 1": []}
if "active_chat" not in st.session_state:
    st.session_state.active_chat = "Chat 1"


def normalize_roles(chat_history):
    """Ensure all roles are valid for LangChain."""
    for message in chat_history:
        if message["role"] == "bot":
            message["role"] = "assistant"
        elif message["role"] == "user":
            message["role"] = "human"
    return chat_history


# Sidebar: Chat History
st.sidebar.title("Chat History")
for chat_name in st.session_state.conversations.keys():
    if st.sidebar.button(chat_name):
        st.session_state.active_chat = chat_name
        # Load and normalize the selected chat's history
        st.session_state.chat_history = normalize_roles(
            st.session_state.conversations[chat_name]
        )
        # Reload context with valid messages
        st.session_state.context = st.session_state.chat_history[-10:]

if st.sidebar.button("New Chat"):
    new_chat_name = f"Chat {len(st.session_state.conversations) + 1}"
    st.session_state.conversations[new_chat_name] = []
    st.session_state.chat_history = []  # Reset display history
    st.session_state.context = []  # Reset processing context
    st.session_state.active_chat = new_chat_name

# Main Chat UI
st.title("Bozo Bot", anchor="top", help="AI-powered chatbot!")
st.write("Ask the most revolutionary questions!")

# Display Chat Messages with updated UI styles
chat_messages = st.session_state.chat_history
for message in chat_messages:
    if message["role"] == "human":  # User message
        st.markdown(
            f"""
            <div style="background-color: #f0f8ff; padding: 12px 16px; border-radius: 12px; margin: 6px 0; max-width: 100%; word-wrap: break-word; font-family: 'Arial', sans-serif;">
                <strong style="color: #0077b6; font-size: 16px; font-weight: bold;">USER:</strong>
                <p style="color: #003366; font-size: 18px; margin: 6px 0; line-height: 1.6;">{message['content']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    elif message["role"] == "assistant":  # Bot message
        st.markdown(
            f"""
            <div style="background-color: #e9f7ef; padding: 12px 16px; border-radius: 12px; margin: 6px 0; max-width: 100%; word-wrap: break-word; align-self: flex-start; font-family: 'Arial', sans-serif;">
                <strong style="color: #1b5e20; font-size: 16px; font-weight: bold;">BOT:</strong>
                <p style="color: #2c6e3d; font-size: 18px; margin: 6px 0; line-height: 1.6;">{message['content']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


# Process user input with context
def process_input():
    if st.session_state.temp_input:
        # Append user message to display history
        user_message = {"role": "human", "content": st.session_state.temp_input}
        st.session_state.chat_history.append(user_message)

        # Add to context (trim to last 5 exchanges)
        st.session_state.context.append(
            {"role": "human", "content": st.session_state.temp_input}
        )
        if (
            len(st.session_state.context) > 10
        ):  # Keep last 5 exchanges (10 messages total)
            st.session_state.context = st.session_state.context[-10:]

        # Generate response with limited context
        response = llm.invoke(st.session_state.context)
        bot_response = {"role": "assistant", "content": response.content}

        # Append bot response to display history and context
        st.session_state.chat_history.append(bot_response)
        st.session_state.context.append(
            {"role": "assistant", "content": response.content}
        )

        # Save conversation history
        st.session_state.conversations[st.session_state.active_chat] = (
            st.session_state.chat_history
        )

        # Clear user input
        st.session_state.temp_input = ""

        # Trigger auto-scroll
        st.session_state.scroll_to_end = True


# Input Box at Bottom with updated design
st.write("---")
st.text_input(
    "Type your question here...",
    key="temp_input",
    on_change=process_input,  # Process input when the user presses Enter or interacts
    placeholder="Ask a question...",
    max_chars=500,
    label_visibility="collapsed",  # Hide label for better design
)

# Auto-scroll to the latest message
if "scroll_to_end" not in st.session_state:
    st.session_state.scroll_to_end = False

if st.session_state.scroll_to_end:
    st.markdown(
        """<script>
           var chatDiv = window.parent.document.getElementsByClassName('main')[0];
           chatDiv.scrollTo(0, chatDiv.scrollHeight);
        </script>""",
        unsafe_allow_html=True,
    )
    st.session_state.scroll_to_end = False
