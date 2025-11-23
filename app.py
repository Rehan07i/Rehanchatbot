import streamlit as st
import google.generativeai as genai

# Title
st.title("Rehan's Happy Bot 😊")
st.write("Trained to make people happy. Be happy be kind!")

# Setup API Key (Securely)
# You will add this in the Streamlit settings later!
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Missing API Key in Secrets")

# Define the persona here!
sys_prompt = """
You are Rehan.Ai, a helpful assistant trained by Rehan.
Your goal is to make people happy.
Always be friendly and kind.
If asked who created you, say 'Rehan'.
"""

model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=sys_prompt)

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Logic
if prompt := st.chat_input("Say something nice..."):
    # User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Bot response
    try:
        response = model.generate_content(prompt)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:

        st.error(f"oops! Something went wrong: {e}")




