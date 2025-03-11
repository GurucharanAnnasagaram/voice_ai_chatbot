Project Description: OpenAI Conversational Chatbot with Speech Capabilities
This project is a Conversational AI chatbot built using OpenAI's API, Streamlit, and speech processing tools. It enables text and voice-based interactions, allowing users to communicate with the chatbot via typed messages or voice input. The bot responds using both text and synthesized speech.

🔹 Key Features:
Interactive Chat Interface – Users can type messages or record audio.
Speech-to-Text (STT) Support – Converts recorded speech into text using speech_to_text().
Conversational AI Responses – Uses get_answer() to generate chatbot responses based on OpenAI.
Text-to-Speech (TTS) Output – Converts chatbot responses into audio using text_to_speech().
Auto-Playing Audio Responses – Automatically plays the chatbot's generated voice response.
Session Memory – Maintains chat history for smooth, contextual conversations.
Floating UI Elements – Utilizes streamlit_float for a fixed footer.
🔹 How It Works:
Session Initialization

The chatbot starts with a default greeting message.
st.session_state.messages stores the conversation history.
User Interaction

Users can either type messages or record audio using audio_recorder().
If audio is recorded, it is temporarily saved as temp_audio.mp3 and transcribed into text.
Chatbot Response

The OpenAI API processes user input via get_answer(), generating a context-aware response.
The response is displayed as text and converted into speech (text_to_speech()).
The audio is played automatically using autoplay_audio().
Session Updates & Cleanup

The chatbot’s response is stored in st.session_state.messages for context retention.
Temporary files (audio and speech output) are deleted after use.
🔹 Tech Stack:
Frontend: Streamlit (UI for chatbot interaction)
Backend: OpenAI API (for response generation)
Audio Processing:
speech_to_text() → Converts recorded voice to text
text_to_speech() → Converts chatbot text to voice
autoplay_audio() → Plays the AI-generated response
Session Management: st.session_state
