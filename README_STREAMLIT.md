# 🎤 AI Voice Assistant - Web Version

A simple AI chatbot with text-to-speech responses. Deploy to Streamlit Cloud for free!

![Deploy](https://img.shields.io/badge/Deploy-Streamlit-FF4B4B)
![Python](https://img.shields.io/badge/python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ✨ Features

- 💬 Text-based chat interface
- 🤖 AI-powered responses (Groq Llama 3.3 70B)
- 🔊 Text-to-speech audio output (Deepgram)
- 📱 Mobile-friendly
- 🌐 Deploy in minutes
- 💰 100% FREE hosting

---

## 🚀 Quick Deploy (5 minutes)

### 1. Get FREE API Keys

**Deepgram** (for speech): https://console.deepgram.com  
**Groq** (for AI): https://console.groq.com

### 2. Fork/Clone This Repo

```bash
git clone https://github.com/YOUR_USERNAME/AI-Voice-assistant-main.git
```

### 3. Deploy to Streamlit Cloud

1. Go to **https://share.streamlit.io**
2. Sign in with GitHub
3. Click "New app"
4. Select this repository
5. Main file: `app.py`
6. Add secrets (API keys):
   ```toml
   DEEPGRAM_API_KEY = "your_key_here"
   GROQ_API_KEY = "your_key_here"
   ```
7. Click Deploy!

**Your app will be live at:** `https://your-app.streamlit.app`

---

## 📖 Full Deployment Guide

See **[DEPLOY_STREAMLIT.md](DEPLOY_STREAMLIT.md)** for detailed step-by-step instructions with screenshots.

---

## 🧪 Test Locally (Optional)

```bash
# Install dependencies
pip install -r requirements.txt

# Create .env file
DEEPGRAM_API_KEY=your_key
GROQ_API_KEY=your_key

# Run
streamlit run app.py
```

Visit: http://localhost:8501

---

## 📂 Project Structure

```
AI-Voice-assistant-main/
├── app.py                    # Streamlit web interface
├── requirements.txt          # Python dependencies
├── .streamlit/
│   └── config.toml          # Streamlit settings
├── src/
│   ├── agents/
│   │   └── agent.py         # AI agent logic
│   └── speech_processing/
│       └── text_to_speech.py # TTS functionality
└── DEPLOY_STREAMLIT.md      # Deployment guide
```

---

## 🔧 Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Groq (Llama 3.3 70B)
- **Text-to-Speech**: Deepgram Aura
- **Hosting**: Streamlit Cloud (FREE)

---

## 🎨 Customization

### Change AI Personality

Edit `app.py` around line 18-31:

```python
simple_prompt = """You are a helpful and friendly AI assistant.
Your personality:
- Friendly and conversational
...
"""
```

### Change UI Colors

Edit `.streamlit/config.toml`:

```toml
[theme]
primaryColor="#FF4B4B"
backgroundColor="#FFFFFF"
```

---

## 🐛 Troubleshooting

**App won't deploy?**
- Check API keys are added in Streamlit secrets
- Verify `requirements.txt` is present
- Click "Reboot app" in dashboard

**No audio playing?**
- Check browser allows audio playback
- Verify Deepgram API key is valid

**API errors?**
- Ensure API keys have no extra spaces
- Verify keys are active (check console)

See [DEPLOY_STREAMLIT.md](DEPLOY_STREAMLIT.md) for more troubleshooting.

---

## 📝 License

MIT License - Free to use and modify

---

## 🙏 Credits

- **Groq** - Fast LLM inference
- **Deepgram** - Text-to-speech API
- **Streamlit** - Web framework

---

## 🎯 What's Next?

1. **Deploy**: Follow [DEPLOY_STREAMLIT.md](DEPLOY_STREAMLIT.md)
2. **Customize**: Change AI personality in `app.py`
3. **Share**: Send your Streamlit URL to friends!

---

**Ready to deploy? See [DEPLOY_STREAMLIT.md](DEPLOY_STREAMLIT.md) for step-by-step guide!**

---

*Built for easy deployment on Streamlit Cloud*
