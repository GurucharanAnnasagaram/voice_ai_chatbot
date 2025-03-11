import os

import streamlit as st
from utils import get_answer, text_to_speech, autoplay_audio, speech_to_text
from audio_recorder_streamlit import audio_recorder
from streamlit_float import *

float_init()


def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hi ! How may i assist you today?"}]


initialize_session_state()

st.title("OPENAI Conversational chatbot")

footer_container = st.container()
with footer_container:
    audio_bytes = audio_recorder()

if audio_bytes:
    with st.spinner("Transcribing"):
        webm_file_path = "temp_audio.mp3"
        with open(webm_file_path,"wb") as f:
            f.write(audio_bytes)
        transcript = speech_to_text(webm_file_path)
        if transcript:
            st.session_state.messages.append({"role" : "user","content" : transcript})
            with st.chat_message("user"):
                st.write(transcript)
            os.remove(webm_file_path)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking🤔..."):
            final_response = get_answer(st.session_state.messages)
        with st.spinner("Generating audio response"):
            audio_file = text_to_speech(final_response)
            autoplay_audio(audio_file)
        st.write(final_response)
        st.session_state.messages.append({"role" :"assistant","content" :final_response})
        os.remove(audio_file)

footer_container.float("bottom: 0rem;")
