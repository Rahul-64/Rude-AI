import os
from dotenv import load_dotenv
from deepgram import DeepgramClient

load_dotenv()

class TextToSpeech:
    """Web-compatible Text-to-Speech using Deepgram"""
    
    def __init__(self):
        self.api_key = os.getenv("DEEPGRAM_API_KEY")
    
    def generate_speech(self, text):
        """Generate speech and return audio bytes for web playback"""
        if not text or len(text.strip()) == 0:
            return None
        
        try:
            # Create Deepgram client
            deepgram = DeepgramClient(api_key=self.api_key)

            # Generate audio
            response = deepgram.speak.v1.audio.generate(
                text=text,
                model="aura-asteria-en",
                encoding="linear16",
                sample_rate=16000
            )

            # Collect audio data
            audio_data = b""
            for chunk in response:
                audio_data += chunk
            
            return audio_data
            
        except Exception as e:
            print(f"[TTS Error] {e}")
            return None

# Legacy class for CLI compatibility
class TTS:
    def __init__(self):
        self.filename = "output.wav"
        try:
            import pygame
            pygame.mixer.quit()
        except:
            pass
        
        try:
            import pygame
            pygame.mixer.init(frequency=16000, size=-16, channels=1, buffer=512)
            print("[TTS] Pygame mixer initialized successfully")
        except Exception as e:
            print(f"[TTS Warning] Pygame init issue: {e}")
    
    def speak(self, text, interruption_flag=None):
        import pygame
        import threading
        
        if not text or len(text.strip()) == 0:
            print("[TTS] No text to speak")
            return
        
        try:
            print(f"[TTS] Generating speech for: {text[:50]}...")
            
            deepgram = DeepgramClient(api_key=os.getenv("DEEPGRAM_API_KEY"))

            response = deepgram.speak.v1.audio.generate(
                text=text,
                model="aura-asteria-en",
                encoding="linear16",
                sample_rate=16000
            )

            audio_data = b""
            for chunk in response:
                if interruption_flag and interruption_flag.is_set():
                    print("[TTS] Interrupted during audio generation")
                    return
                audio_data += chunk
            
            print(f"[TTS] Audio generated: {len(audio_data)} bytes")
            
            with open(self.filename, "wb") as audio_file:
                audio_file.write(audio_data)
            
            print(f"[TTS] Audio saved to {self.filename}")

            try:
                pygame.mixer.quit()
                pygame.mixer.init(frequency=16000, size=-16, channels=1, buffer=512)
                
                pygame.mixer.music.load(self.filename)
                pygame.mixer.music.play()
                
                print("[TTS] Playing audio...")
                
                while pygame.mixer.music.get_busy():
                    if interruption_flag and interruption_flag.is_set():
                        pygame.mixer.music.stop()
                        print("[TTS] Playback interrupted by user!")
                        return
                    pygame.time.Clock().tick(10)
                    import time
                    time.sleep(0.1)
                
                print("[TTS] Playback complete")
                
            except Exception as play_error:
                print(f"[TTS Error] Playback failed: {play_error}")

        except Exception as e:
            print(f"[TTS Error] Exception: {e}")

