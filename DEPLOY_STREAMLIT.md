# 🚀 Deploy to Streamlit Cloud (FREE)

Simple step-by-step guide to deploy your AI Voice Assistant.

---

## Prerequisites

✅ GitHub account (free)  
✅ Streamlit account (free)  
✅ Deepgram API key (free)  
✅ Groq API key (free)

---

## Step 1: Get Your FREE API Keys

### Deepgram API Key
1. Go to https://console.deepgram.com
2. Sign up for free account
3. Click "Create API Key"
4. Copy and save your key

### Groq API Key
1. Go to https://console.groq.com
2. Sign up for free account
3. Click "Create API Key"
4. Copy and save your key

---

## Step 2: Push to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "AI Voice Assistant ready for deployment"

# Create a new repo on GitHub at https://github.com/new
# Then connect and push:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

---

## Step 3: Deploy on Streamlit Cloud

### 3.1 Sign in to Streamlit
1. Go to https://share.streamlit.io
2. Click "Sign in"
3. Sign in with your GitHub account

### 3.2 Create New App
1. Click "New app" button
2. Select your repository from the dropdown
3. Branch: `main`
4. Main file path: `app.py`
5. App URL: Choose a custom name (e.g., `my-ai-assistant`)

### 3.3 Add API Keys (IMPORTANT!)
1. Click "Advanced settings"
2. Under "Secrets", paste this:
   ```toml
   DEEPGRAM_API_KEY = "paste_your_deepgram_key_here"
   GROQ_API_KEY = "paste_your_groq_key_here"
   ```
3. Replace the placeholder text with your actual API keys

### 3.4 Deploy!
1. Click "Deploy"
2. Wait 2-3 minutes for deployment
3. Your app will be live!

---

## 🎉 You're Live!

Your app URL will be:
```
https://your-app-name.streamlit.app
```

Share this URL with anyone - they can use your AI assistant!

---

## 🔄 Updating Your App

Whenever you push changes to GitHub, Streamlit automatically redeploys:

```bash
git add .
git commit -m "Update message"
git push
```

Wait 1-2 minutes and your changes are live!

---

## 🐛 Troubleshooting

### "API Key Not Found"
- Make sure you added secrets in Step 3.3
- No extra spaces around the `=` sign
- Keys are in quotes
- Click "Reboot app" after adding secrets

### "Module Not Found"
- Check that `requirements.txt` is in your repo
- Click "Reboot app" in Streamlit dashboard

### "App Not Loading"
- Click "Manage app" → View logs
- Check for error messages
- Verify API keys are valid

### Need to Restart?
1. Go to https://share.streamlit.io
2. Find your app
3. Click "⋮" → "Reboot app"

---

## ⚙️ App Settings

### Change App Name/URL
1. Go to app dashboard
2. Click "⋮" → "Settings"
3. Change name
4. Save

### Delete App
1. Go to app dashboard
2. Click "⋮" → "Delete app"
3. Confirm

### View Logs
1. Click "Manage app" (bottom right of your deployed app)
2. View real-time logs

---

## 💡 Tips

- **Free tier limits**: Unlimited public apps, 1GB resources
- **Custom domain**: Available on paid plans
- **Private apps**: Available on paid plans ($20/month)
- **Auto-sleep**: Apps sleep after 7 days of no traffic (free tier)
- **Wake-up**: Apps auto-wake when someone visits

---

## 📱 Sharing Your App

Send this link to anyone:
```
https://your-app-name.streamlit.app
```

They can:
- Chat with AI
- Get voice responses
- Use it on mobile/desktop
- No installation needed!

---

## 🎯 Quick Reference

| Task | Command/Link |
|------|-------------|
| Deploy | https://share.streamlit.io |
| Test locally | `streamlit run app.py` |
| Update app | `git push` |
| View logs | Click "Manage app" |
| Get API keys | Deepgram + Groq consoles |

---

**That's it! Your AI Voice Assistant is live on the internet!** 🎉
