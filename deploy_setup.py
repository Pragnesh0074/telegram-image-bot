#!/usr/bin/env python3
"""
Deployment Setup Script
Helps you prepare your bot for cloud deployment
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_git_installed():
    """Check if Git is installed."""
    try:
        subprocess.run(["git", "--version"], check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def setup_git_repository():
    """Set up Git repository and prepare for deployment."""
    
    print("🚀 Setting up Git repository for deployment...")
    
    # Check if Git is installed
    if not check_git_installed():
        print("❌ Git is not installed. Please install Git first:")
        print("   Download from: https://git-scm.com/downloads")
        return False
    
    # Check if already a Git repository
    if os.path.exists(".git"):
        print("ℹ️  Git repository already exists")
        return True
    
    # Initialize Git repository
    if not run_command("git init", "Initializing Git repository"):
        return False
    
    # Add all files
    if not run_command("git add .", "Adding files to Git"):
        return False
    
    # Create initial commit
    if not run_command('git commit -m "Initial commit: Telegram Image Bot"', "Creating initial commit"):
        return False
    
    # Set main branch
    if not run_command("git branch -M main", "Setting main branch"):
        return False
    
    print("\n✅ Git repository setup completed!")
    print("\n📝 Next steps:")
    print("1. Create a GitHub repository at: https://github.com/new")
    print("2. Copy the repository URL")
    print("3. Run: git remote add origin YOUR_REPOSITORY_URL")
    print("4. Run: git push -u origin main")
    print("5. Follow the deployment guide in DEPLOYMENT.md")
    
    return True

def check_environment():
    """Check if environment is ready for deployment."""
    print("🔍 Checking deployment environment...")
    
    # Check required files
    required_files = [
        "bot.py",
        "config.py", 
        "image_processor.py",
        "caption_model.py",
        "requirements.txt",
        "Procfile"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        return False
    
    # Check BOT_TOKEN
    bot_token = os.getenv('BOT_TOKEN')
    if not bot_token:
        print("⚠️  Warning: BOT_TOKEN environment variable not set")
        print("   You'll need to set this in your cloud platform")
    else:
        print("✅ BOT_TOKEN environment variable is set")
    
    print("✅ Environment check completed")
    return True

def main():
    """Main function."""
    print("🤖 Telegram Image Bot - Deployment Setup")
    print("=" * 50)
    
    # Check environment
    if not check_environment():
        print("\n❌ Environment check failed. Please fix the issues above.")
        return
    
    # Setup Git repository
    if not setup_git_repository():
        print("\n❌ Git setup failed. Please check the errors above.")
        return
    
    print("\n🎉 Setup completed successfully!")
    print("\n📚 Read DEPLOYMENT.md for detailed deployment instructions")
    print("🚀 Your bot is ready for cloud deployment!")

if __name__ == "__main__":
    main() 