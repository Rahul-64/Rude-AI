import streamlit as st
import streamlit.components.v1 as components
from src.agents.agent import Agent
from src.speech_processing.text_to_speech import TextToSpeech
import os
from dotenv import load_dotenv

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
        font-size: 14px;
        font-weight: 500;
        max-width: 300px;
    }
    
    .state-listening {
        background-color: #C8E6C9;
        color: #2E7D32;
    }
    
    .state-processing {
        background-color: #FFECB3;
        color: #F57F17;
    }
    
    .state-speaking {
        background-color: #BBDEFB;
        color: #1565C0;
    }
    
    /* Conversation display */
    .conversation-container {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 8px;
        padding: 20px;
        margin: 20px auto;
        max-width: 600px;
        max-height: 300px;
        overflow-y: auto;
        text-align: left;
    }
    
    .message {
        margin: 10px 0;
        padding: 10px;
        border-radius: 6px;
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
    
    # Main interaction - Text input for now (voice coming soon)
    user_input = st.text_input("", placeholder="Type your message or use voice input...", label_visibility="collapsed", key="user_input")
    
    # Circular button
    start_clicked = st.button("", key="start_button", help="Click or press Tab to start")
    
    # Custom button styling using HTML
    st.markdown("""
    <div class="circle-button" onclick="document.querySelector('[data-testid=\"stButton\"] button').click()">
        <div class="button-text">tab to start<br>conversation</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Handle button click or Enter key
    if start_clicked or (user_input and user_input.strip()):
        if user_input and user_input.strip():
            # Add user message
            st.session_state.conversation_history.append({
                "role": "user",
                "content": user_input
            })
            
            # Set processing state
            st.session_state.conversation_state = 'processing'
            
            # Get AI response
            try:
                response = st.session_state.agent.process_request(user_input)
                
                # Add AI response
                st.session_state.conversation_history.append({
                    "role": "assistant",
                    "content": response
                })
                
                # Generate audio
                st.session_state.conversation_state = 'speaking'
                tts = TextToSpeech()
                audio_bytes = tts.generate_speech(response)
                
                if audio_bytes:
                    st.session_state.last_audio = audio_bytes
                
                st.session_state.conversation_state = 'idle'
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.session_state.conversation_state = 'idle'
            
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
        
        # Play last audio
        if hasattr(st.session_state, 'last_audio') and st.session_state.last_audio:
            st.audio(st.session_state.last_audio, format='audio/wav')
    
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

# Keyboard controls (Tab and Space)
components.html("""
<script>
document.addEventListener('keydown', function(e) {
    // Tab key to start conversation
    if (e.key === 'Tab') {
        e.preventDefault();
        const input = window.parent.document.querySelector('input[type="text"]');
        if (input) {
            input.focus();
        }
    }
    
    // Space key to interrupt (stop audio)
    if (e.key === ' ' && e.target.tagName !== 'INPUT') {
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
