#!/bin/bash

echo "🤖 Starting Telegram Image Bot on Replit..."

# Check if BOT_TOKEN is set
if [ -z "$BOT_TOKEN" ]; then
    echo "❌ Error: BOT_TOKEN environment variable is not set!"
    echo "Please set your bot token in the Secrets tab in Replit."
    exit 1
fi

echo "✅ Bot token found"
echo "📦 Installing dependencies..."

# Install Python dependencies
pip install -r requirements.txt

echo "🚀 Starting bot..."
python bot.py 