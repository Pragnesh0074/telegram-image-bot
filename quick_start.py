#!/usr/bin/env python3
"""
Quick start script for the Telegram Image Description Bot.
This script helps users set up the bot easily with guided prompts.
"""

import os
import sys
from pathlib import Path

def print_banner():
    """Print the bot banner."""
    print("""
🤖 Telegram Image Description Bot
================================
Powered by Salesforce BLIP Model
    """)

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required!")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def install_dependencies():
    """Install required dependencies."""
    print("\n📦 Installing dependencies...")
    
    try:
        import subprocess
        print("Installing packages from requirements.txt...")
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Dependencies installed successfully!")
            return True
        else:
            print(f"❌ Failed to install dependencies: {result.stderr}")
            print("\n💡 Try installing manually:")
            print("pip install python-telegram-bot transformers torch torchvision Pillow requests python-dotenv")
            return False
    except Exception as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def setup_environment():
    """Set up environment variables."""
    print("\n🔧 Setting up environment...")
    
    env_file = Path(".env")
    
    if env_file.exists():
        print("✅ .env file already exists")
        return True
    
    print("📝 Creating .env file...")
    
    bot_token = input("Enter your Telegram Bot Token (get from @BotFather): ").strip()
    
    if not bot_token:
        print("❌ Bot token is required!")
        return False
    
    try:
        with open(".env", "w") as f:
            f.write(f"BOT_TOKEN={bot_token}\n")
        print("✅ .env file created successfully!")
        return True
    except Exception as e:
        print(f"❌ Failed to create .env file: {e}")
        return False

def test_setup():
    """Test the setup."""
    print("\n🧪 Testing setup...")
    
    try:
        from test_setup import main as test_main
        return test_main()
    except Exception as e:
        print(f"❌ Failed to run tests: {e}")
        return False

def show_next_steps():
    """Show next steps to the user."""
    print("""
🎉 Setup Complete!
==================

Next steps:
1. Start your bot: python bot.py
2. Open Telegram and find your bot
3. Send /start to begin
4. Send images to get descriptions!

Commands:
- /start - Start the bot
- /help - Show help
- /status - Show bot status

For help, check README.md or run: python test_setup.py
    """)

def main():
    """Main setup function."""
    print_banner()
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Install dependencies
    if not install_dependencies():
        print("\n❌ Failed to install dependencies.")
        print("Try running: pip install -r requirements.txt")
        return False
    
    # Setup environment
    if not setup_environment():
        print("\n❌ Failed to setup environment.")
        return False
    
    # Test setup
    if not test_setup():
        print("\n⚠️  Setup completed but some tests failed.")
        print("You can still try running the bot.")
    
    show_next_steps()
    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1) 