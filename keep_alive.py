from flask import Flask
import threading
import time
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 Telegram Image Bot is running!"

@app.route('/health')
def health():
    return "✅ Bot is healthy and running!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def run_bot():
    # Import and run the bot
    from bot import main
    main()

if __name__ == "__main__":
    # Start Flask server in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # Run the bot
    run_bot() 