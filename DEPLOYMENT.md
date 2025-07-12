# 🚀 Deployment Guide

This guide will help you deploy your Telegram Image Bot to the cloud so it can run 24/7.

## 📋 Prerequisites

1. **GitHub Repository**: Push your code to GitHub
2. **Telegram Bot Token**: You already have this
3. **Git Account**: For version control

## 🎯 Option 1: Railway (Recommended)

### Why Railway?
- ✅ **Free tier available**
- ✅ **Easy deployment**
- ✅ **Automatic HTTPS**
- ✅ **Good for Python bots**

### Steps:

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/telegram-image-bot.git
   git push -u origin main
   ```

2. **Deploy on Railway**:
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Add environment variable:
     - Key: `BOT_TOKEN`
     - Value: Your bot token
   - Deploy!

3. **Your bot will be live in minutes!**

---

## 🎯 Option 2: Render

### Why Render?
- ✅ **Free tier available**
- ✅ **Simple deployment**
- ✅ **Good documentation**

### Steps:

1. **Push to GitHub** (same as above)

2. **Deploy on Render**:
   - Go to [render.com](https://render.com)
   - Sign up with GitHub
   - Click "New" → "Web Service"
   - Connect your GitHub repo
   - Configure:
     - **Name**: `telegram-image-bot`
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `python bot.py`
   - Add environment variable:
     - Key: `BOT_TOKEN`
     - Value: Your bot token
   - Deploy!

---

## 🎯 Option 3: Heroku

### Why Heroku?
- ✅ **Classic platform**
- ✅ **Good documentation**
- ⚠️ **Paid after free tier ended**

### Steps:

1. **Install Heroku CLI**:
   ```bash
   # Windows
   winget install --id=Heroku.HerokuCLI
   
   # Or download from: https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login and Deploy**:
   ```bash
   heroku login
   heroku create your-bot-name
   git push heroku main
   heroku config:set BOT_TOKEN=your_bot_token_here
   heroku ps:scale worker=1
   ```

---

## 🎯 Option 4: DigitalOcean App Platform

### Why DigitalOcean?
- ✅ **Reliable**
- ✅ **Good performance**
- ⚠️ **Paid service**

### Steps:

1. **Push to GitHub** (same as above)

2. **Deploy on DigitalOcean**:
   - Go to [digitalocean.com](https://digitalocean.com)
   - Create account
   - Go to "Apps" → "Create App"
   - Connect GitHub repo
   - Configure:
     - **Source**: Your repo
     - **Branch**: `main`
     - **Build Command**: `pip install -r requirements.txt`
     - **Run Command**: `python bot.py`
   - Add environment variable: `BOT_TOKEN`
   - Deploy!

---

## 🔧 Environment Variables

All platforms need this environment variable:

| Key | Value | Description |
|-----|-------|-------------|
| `BOT_TOKEN` | `your_bot_token_here` | Your Telegram bot token |

---

## 🚨 Important Notes

### 1. **Model Loading Time**
- The BLIP model takes time to load on first deployment
- Be patient during the first startup (2-5 minutes)

### 2. **Memory Requirements**
- The model needs ~1GB RAM
- Free tiers might have limitations
- Consider upgrading if you get memory errors

### 3. **Cold Starts**
- Free tiers may have cold starts
- Bot might be slow to respond initially
- Consider paid tiers for better performance

### 4. **Logs and Monitoring**
- Check platform logs for errors
- Monitor bot performance
- Set up alerts if needed

---

## 🧪 Testing Your Deployment

1. **Send `/start`** to your bot
2. **Send an image** to test functionality
3. **Check logs** on your platform
4. **Verify 24/7 operation**

---

## 🔄 Updating Your Bot

To update your bot:

1. **Make changes locally**
2. **Test locally**
3. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Update bot functionality"
   git push
   ```
4. **Platform will auto-deploy** (Railway/Render) or manually deploy (Heroku)

---

## 🆘 Troubleshooting

### Common Issues:

1. **Bot not responding**:
   - Check platform logs
   - Verify `BOT_TOKEN` is correct
   - Ensure bot is running

2. **Model loading errors**:
   - Check memory limits
   - Verify dependencies in `requirements.txt`
   - Check Python version compatibility

3. **Image processing errors**:
   - Check image size limits
   - Verify supported formats
   - Check network connectivity

### Getting Help:
- Check platform documentation
- Review logs carefully
- Test locally first
- Ask in platform communities

---

## 🎉 Success!

Once deployed, your bot will:
- ✅ Run 24/7
- ✅ Be accessible worldwide
- ✅ Auto-restart on crashes
- ✅ Scale automatically
- ✅ Be secure with HTTPS

**Your bot is now live and ready for users!** 🚀 