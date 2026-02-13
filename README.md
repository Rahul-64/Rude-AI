# 🎤 AI Companion - Pastel Design

Beautiful AI companion with voice interaction and pastel gradient interface.

![Design](https://img.shields.io/badge/Design-Pastel_Gradient-FF69B4)
![Python](https://img.shields.io/badge/python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32-FF4B4B)

---

## 🚀 Quick Deploy to Streamlit Cloud

### 1. Get FREE API Keys

**Deepgram**: https://console.deepgram.com  
**Groq**: https://console.groq.com

### 2. Deploy

1. Go to **https://share.streamlit.io**
2. Sign in with GitHub
3. Click "New app"
4. Repository: Select this repo
5. Main file: `app.py`
6. Add secrets:
   ```toml
   DEEPGRAM_API_KEY = "your_key_here"
   GROQ_API_KEY = "your_key_here"
   ```
7. Click **Deploy**!

---

## 🎨 Design Specifications

### Color Palette
- Background Gradient: `#FFF9C4` → `#F8BBD0` → `#E1BEE7`
- Header: `#000000` (black)
- Main Container: `rgba(150, 130, 180, 0.6)`
- Button: `#F48FB1` (pink)
- Instructions Box: `#F8BBD0` (light pink)

### Layout
```
┌──────────────────────────────┐
│         Header (black)        │
├──────────────────────────────┤
│                               │
│   ┌────────────────────┐     │
│   │       Body          │     │
│   │                     │     │
│   │   ⭕ Circular       │     │
│   │     Button          │     │
│   │                     │     │
│   │   📋 Instructions   │     │
│   └────────────────────┘     │
│                               │
└──────────────────────────────┘
```

---

## 🎯 Features

- 💬 **Text Chat** - Type messages to AI
- 🗣️ **Voice Responses** - AI speaks back (Deepgram TTS)
- 🤖 **Smart AI** - Powered by Groq Llama 3.3
- ⌨️ **Tab Key** - Focus input to start
- ⏸️ **Space Key** - Interrupt AI speech
- 📱 **Responsive** - Works on mobile & desktop

---

## 🧪 Test Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Create .env
DEEPGRAM_API_KEY=your_key
GROQ_API_KEY=your_key

# Run
streamlit run app.py
```

Visit: http://localhost:8501

---

## ⌨️ Keyboard Controls

| Key | Action |
|-----|--------|
| **Tab** | Focus input to start conversation |
| **Space** | Interrupt AI while speaking |
| **Enter** | Send message |

---

## 🎨 Customization

### Change Colors

Edit `app.py` CSS section:

```css
.stApp {
    background: linear-gradient(135deg, 
        #YOUR_COLOR1 0%, 
        #YOUR_COLOR2 50%, 
        #YOUR_COLOR3 100%) !important;
}
```

### Change AI Personality

Edit `app.py` around line 130:

```python
simple_prompt = """You are a [YOUR PERSONALITY HERE]..."""
```

---

## 📂 Project Structure

```
AI-Voice-assistant-main/
├── app.py                    # Main Streamlit app with pastel design
├── requirements.txt          # Dependencies
├── .streamlit/
│   ├── config.toml          # Theme: pink & pastel
│   └── secrets.toml         # API keys (template)
├── src/
│   ├── agents/
│   │   └── agent.py         # AI logic
│   └── speech_processing/
│       └── text_to_speech.py # TTS
└── README.md                # This file
```

---

## 🐛 Troubleshooting

**Gradient not showing?**
- Clear browser cache
- Hard refresh (Ctrl+F5)

**Button not circular?**
- Check browser supports modern CSS
- Try different browser (Chrome recommended)

**API errors?**
- Verify API keys in Streamlit secrets
- Check keys have no extra spaces

---

## 🎯 Design Philosophy

- **Calm & Friendly** - Pastel colors create welcoming atmosphere
- **Minimal** - Clean interface, focus on conversation
- **Intuitive** - Clear instructions, simple interaction
- **Accessible** - Keyboard shortcuts for power users

---

## 📸 Screenshot Match

This design matches the specification:
- ✅ Yellow-pink-purple gradient background
- ✅ Black header bar
- ✅ Semi-transparent purple container
- ✅ Large circular pink button
- ✅ "Body" label
- ✅ Instructions box with guidelines
- ✅ Clean, minimal aesthetic

---

## 🚀 Deploy Now

Your app is ready to deploy on Streamlit Cloud!

**Live URL will be**: `https://your-app-name.streamlit.app`

Share it with friends!

---

## 📝 License

MIT License - Free to use and modify

---

**Built with beautiful pastel gradients and modern UI design** 🎨
