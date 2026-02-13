import os
from deepgram import DeepgramClient, PrerecordedOptions
from dotenv import load_dotenv

load_dotenv()

class SpeechToText:
    """Web-compatible Speech-to-Text using Deepgram"""
    
    def __init__(self):
        self.api_key = os.getenv("DEEPGRAM_API_KEY")
        self.client = DeepgramClient(self.api_key)
    
    def transcribe_audio(self, audio_bytes):
        """Transcribe audio bytes to text"""
        if not audio_bytes or len(audio_bytes) == 0:
            return None
        
        try:
            # Configure Deepgram options
            options = PrerecordedOptions(
                model="nova-2",
                smart_format=True,
                language="en",
            )
            
            # Create payload with audio bytes
            payload = {"buffer": audio_bytes}
            
            # Transcribe
            response = self.client.listen.prerecorded.v("1").transcribe_file(
                payload, options
            )
            
            # Extract transcript
            if response.results and response.results.channels:
                transcript = response.results.channels[0].alternatives[0].transcript
                return transcript.strip() if transcript else None
            
            return None
            
        except Exception as e:
            print(f"[STT Error] {e}")
            return None
