#!/usr/bin/env python3
"""
Deployment script for Replit
This script handles the complete setup and deployment of the Telegram bot
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def check_environment():
    """Check if all required environment variables are set."""
    print("🔍 Checking environment...")
    
    bot_token = os.getenv('BOT_TOKEN')
    if not bot_token:
        print("❌ BOT_TOKEN environment variable is not set!")
        print("Please set your bot token in the Secrets tab in Replit.")
        return False
    
    print("✅ BOT_TOKEN found")
    return True

def install_dependencies():
    """Install Python dependencies."""
    print("📦 Installing dependencies...")
    
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      check=True, capture_output=True, text=True)
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        print(f"Error output: {e.stderr}")
        return False

def run_bot():
    """Run the bot with keep-alive web server."""
    print("🚀 Starting bot with keep-alive server...")
    
    try:
        # Import and run the keep-alive script
        from keep_alive import app
        import threading
        
        # Start the bot in a separate thread
        def run_bot_thread():
            from bot import main
            main()
        
        bot_thread = threading.Thread(target=run_bot_thread)
        bot_thread.daemon = True
        bot_thread.start()
        
        # Run the Flask app
        app.run(host='0.0.0.0', port=8080)
        
    except Exception as e:
        print(f"❌ Error running bot: {e}")
        return False

def main():
    """Main deployment function."""
    print("🤖 Telegram Image Bot - Replit Deployment")
    print("=" * 50)
    
    # Check environment
    if not check_environment():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Run the bot
    print("🎉 Deployment complete! Starting bot...")
    run_bot()

if __name__ == "__main__":
    main() 