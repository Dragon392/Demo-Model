import streamlit as st
from gtts import gTTS
import tempfile

# Predefined questions and answers
qa_pairs = {
    "what is my account balance": "Your account balance is fifty thousand rupees.",
    "how can I open a new account": "You can open a new account by providing us with your ID card and proof of salary."
}

st.title("AI Voice Demo for Bank KIOSK")

st.write("Ask me a banking question, and I'll respond!")

# User input
user_input = st.text_input("Type your question here:")

if user_input:
    # Get the answer from predefined questions
    response = qa_pairs.get(user_input.lower(), "Sorry, I don't have an answer for that.")
    
    # Display the response
    st.write(f"AI: {response}")
    
    # Convert the response to audio
    tts = gTTS(response)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        tts.save(temp_audio.name)
        st.audio(temp_audio.name, format="audio/mp3")
