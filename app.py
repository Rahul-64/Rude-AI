import streamlit as st
import streamlit.components.v1 as components
from audio_recorder_streamlit import audio_recorder
from src.agents.agent import Agent
from src.speech_processing.text_to_speech import TextToSpeech
from src.speech_processing.speech_to_text_web import SpeechToText
import os
from dotenv import load_dotenv
import time

load_dotenv()

# Page config - MUST be first Streamlit command
st.set_page_config(
    page_title="AI Companion",
    page_icon="🎤",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for pastel gradient design
st.markdown("""
<style>
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Pastel gradient background */
    .stApp {
        background: linear-gradient(135deg, 
            #FFF9C4 0%, 
            #FFE0EC 35%,
            #F8BBD0 50%, 
            #E1BEE7 100%) !important;
    }
    
    /* Black header */
    .header-bar {
        background-color: #000000;
        color: white;
        text-align: center;
        padding: 15px;
        width: 100%;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 1000;
        font-size: 18px;
        font-weight: 500;
    }
    
    /* Main content container */
    .main-container {
        background: rgba(150, 130, 180, 0.6);
        border-radius: 12px;
        padding: 60px 50px;
        max-width: 700px;
        margin: 100px auto 50px auto;
        text-align: center;
        min-height: 500px;
    }
    
    /* Body label */
    .body-label {
        font-size: 16px;
        color: #2c2c2c;
        margin-bottom: 40px;
        font-weight: 500;
    }
    
    /* Circular pink button */
    .circle-button {
        width: 220px;
        height: 220px;
        border-radius: 50%;
        background: linear-gradient(135deg, #F48FB1 0%, #F06292 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 40px auto;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        border: none;
    }
    
    .circle-button:hover {
        background: linear-gradient(135deg, #F06292 0%, #EC407A 100%);
        transform: scale(1.05);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3);
    }
    
    .circle-button:active {
        transform: scale(0.98);
    }
    
    .button-text {
        color: #2c2c2c;
        font-size: 16px;
        font-weight: 500;
        line-height: 1.4;
        padding: 20px;
    }
    
    /* Instructions box */
    .instructions-box {
        background-color: #F8BBD0;
        padding: 20px 30px;
        border-radius: 8px;
        max-width: 340px;
        margin: 40px auto;
        text-align: left;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    
    .instructions-title {
        font-weight: 600;
        margin-bottom: 10px;
        color: #2c2c2c;
        font-size: 15px;
    }
    
    .instructions-text {
        color: #2c2c2c;
        font-size: 14px;
        line-height: 1.8;
        margin: 0;
    }
    
    /* State indicators */
    .state-indicator {
        padding: 12px 24px;
        border-radius: 20px;
        margin: 20px auto;
        font-size: 16px;
        font-weight: 600;
        max-width: 300px;
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    
    .state-listening {
        background-color: #C8E6C9;
        color: #2E7D32;
        box-shadow: 0 0 20px rgba(46, 125, 50, 0.4);
    }
    
    .state-processing {
        background-color: #FFECB3;
        color: #F57F17;
        box-shadow: 0 0 20px rgba(245, 127, 23, 0.4);
    }
    
    .state-speaking {
        background-color: #BBDEFB;
        color: #1565C0;
        box-shadow: 0 0 20px rgba(21, 101, 192, 0.4);
    }
    
    /* Hide audio recorder default UI */
    .stAudio {
        display: none !important;
    }
    
    /* Conversation transcript */
    .conversation-container {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 8px;
        padding: 20px;
        margin: 20px auto;
        max-width: 600px;
        max-height: 200px;
        overflow-y: auto;
        text-align: left;
    }
    
    .message {
        margin: 10px 0;
        padding: 10px;
        border-radius: 6px;
        font-size: 14px;
    }
    
    .user-message {
        background-color: #E8EAF6;
        color: #283593;
    }
    
    .ai-message {
        background-color: #F3E5F5;
        color: #4A148C;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'conversation_state' not in st.session_state:
    st.session_state.conversation_state = 'idle'  # idle, listening, processing, speaking
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []
if 'agent' not in st.session_state:
    model = "groq/llama-3.3-70b-versatile"
    simple_prompt = """You are a helpful and friendly AI companion.

Your personality:
- Warm and conversational
- Empathetic and understanding
- Concise and clear
- Supportive and encouraging

Guidelines:
- Keep responses brief (2-3 sentences)
- Be natural and friendly
- Listen actively and respond thoughtfully
- Stay positive and helpful

Keep your responses conversational and concise.
"""
    st.session_state.agent = Agent("AI Companion", model, tools=[], system_prompt=simple_prompt)

if 'stt' not in st.session_state:
    st.session_state.stt = SpeechToText()

if 'tts' not in st.session_state:
    st.session_state.tts = TextToSpeech()

if 'conversation_active' not in st.session_state:
    st.session_state.conversation_active = False

# Header
st.markdown('<div class="header-bar">Header</div>', unsafe_allow_html=True)

# Main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<div class="body-label">Body</div>', unsafe_allow_html=True)

# Check API keys
deepgram_key = os.getenv("DEEPGRAM_API_KEY")
groq_key = os.getenv("GROQ_API_KEY")

if not deepgram_key or not groq_key:
    st.markdown("""
    <div style="background-color: #FFCDD2; padding: 20px; border-radius: 8px; margin: 20px 0;">
        <h3 style="color: #C62828; margin: 0 0 10px 0;">⚠️ API Keys Missing</h3>
        <p style="color: #2c2c2c; margin: 0;">Please add your API keys in Streamlit Secrets:</p>
        <ul style="color: #2c2c2c; text-align: left;">
            <li>DEEPGRAM_API_KEY</li>
            <li>GROQ_API_KEY</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
else:
    # State indicator
    if st.session_state.conversation_state == 'listening':
        st.markdown('<div class="state-indicator state-listening">🎤 Listening...</div>', unsafe_allow_html=True)
    elif st.session_state.conversation_state == 'processing':
        st.markdown('<div class="state-indicator state-processing">🤔 Thinking...</div>', unsafe_allow_html=True)
    elif st.session_state.conversation_state == 'speaking':
        st.markdown('<div class="state-indicator state-speaking">🔊 Speaking...</div>', unsafe_allow_html=True)
    
    # Circular button to start/stop conversation
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if not st.session_state.conversation_active:
            if st.button("", key="start_button", help="Tap to start voice conversation", use_container_width=True):
                st.session_state.conversation_active = True
                st.session_state.conversation_state = 'listening'
                st.rerun()
            
            st.markdown("""
            <div class="circle-button">
                <div class="button-text">tap to start<br>conversation</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            if st.button("", key="stop_button", help="Tap to stop conversation", use_container_width=True):
                st.session_state.conversation_active = False
                st.session_state.conversation_state = 'idle'
                st.rerun()
            
            st.markdown("""
            <div class="circle-button" style="background: linear-gradient(135deg, #EF5350 0%, #E53935 100%);">
                <div class="button-text">tap to stop<br>conversation</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Voice recording (only when conversation is active)
    if st.session_state.conversation_active and st.session_state.conversation_state == 'listening':
        st.markdown('<p style="text-align: center; color: #2E7D32; font-weight: 600;">🎤 Recording... Speak now!</p>', unsafe_allow_html=True)
        
        audio_bytes = audio_recorder(
            text="",
            recording_color="#2E7D32",
            neutral_color="#9E9E9E",
            icon_name="microphone",
            icon_size="3x",
            pause_threshold=2.0,
            sample_rate=16000
        )
        
        if audio_bytes:
            # Process audio
            st.session_state.conversation_state = 'processing'
            
            # Transcribe
            transcript = st.session_state.stt.transcribe_audio(audio_bytes)
            
            if transcript:
                # Add to history
                st.session_state.conversation_history.append({
                    "role": "user",
                    "content": transcript
                })
                
                # Check for goodbye
                if "goodbye" in transcript.lower() or "bye" in transcript.lower():
                    st.session_state.conversation_history.append({
                        "role": "assistant",
                        "content": "Goodbye! It was nice talking to you."
                    })
                    
                    # Generate goodbye speech
                    audio_response = st.session_state.tts.generate_speech("Goodbye! It was nice talking to you.")
                    if audio_response:
                        st.session_state.conversation_state = 'speaking'
                        st.audio(audio_response, format='audio/wav', autoplay=True)
                        time.sleep(3)
                    
                    # End conversation
                    st.session_state.conversation_active = False
                    st.session_state.conversation_state = 'idle'
                    st.rerun()
                else:
                    # Get AI response
                    try:
                        response = st.session_state.agent.process_request(transcript)
                        
                        # Add to history
                        st.session_state.conversation_history.append({
                            "role": "assistant",
                            "content": response
                        })
                        
                        # Generate speech
                        audio_response = st.session_state.tts.generate_speech(response)
                        
                        if audio_response:
                            st.session_state.conversation_state = 'speaking'
                            st.audio(audio_response, format='audio/wav', autoplay=True)
                            
                            # Wait for audio to finish, then loop back to listening
                            time.sleep(len(response) * 0.1)  # Rough estimate
                            st.session_state.conversation_state = 'listening'
                            st.rerun()
                        else:
                            st.session_state.conversation_state = 'listening'
                            st.rerun()
                            
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
                        st.session_state.conversation_state = 'listening'
                        st.rerun()
            else:
                # No transcript, go back to listening
                st.session_state.conversation_state = 'listening'
                st.rerun()
    
    # Display conversation history
    if st.session_state.conversation_history:
        st.markdown('<div class="conversation-container">', unsafe_allow_html=True)
        for msg in st.session_state.conversation_history[-6:]:  # Show last 6 messages
            if msg["role"] == "user":
                st.markdown(f'<div class="message user-message">👤 You: {msg["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="message ai-message">🤖 AI: {msg["content"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Instructions box
    st.markdown("""
    <div class="instructions-box">
        <div class="instructions-title">instructions -</div>
        <div class="instructions-text">
            -press space to interrupt<br>
            -say "goodbye" to end this chat
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Space key to interrupt
components.html("""
<script>
document.addEventListener('keydown', function(e) {
    if (e.key === ' ' && e.target.tagName !== 'INPUT' && e.target.tagName !== 'TEXTAREA') {
        e.preventDefault();
        const audio = window.parent.document.querySelector('audio');
        if (audio) {
            audio.pause();
            audio.currentTime = 0;
        }
    }
});
</script>
""", height=0)
