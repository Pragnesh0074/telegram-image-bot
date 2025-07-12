#!/usr/bin/env python3
"""
Test script to verify the Telegram Image Description Bot setup.
Run this script to check if all dependencies and components are working correctly.
"""

import sys
import os
from pathlib import Path

def test_imports():
    """Test if all required packages can be imported."""
    print("🔍 Testing imports...")
    
    try:
        import telegram
        print("✅ python-telegram-bot imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import python-telegram-bot: {e}")
        return False
    
    try:
        import torch
        print(f"✅ PyTorch imported successfully (version: {torch.__version__})")
    except ImportError as e:
        print(f"❌ Failed to import PyTorch: {e}")
        return False
    
    try:
        import transformers
        print(f"✅ Transformers imported successfully (version: {transformers.__version__})")
    except ImportError as e:
        print(f"❌ Failed to import Transformers: {e}")
        return False
    
    try:
        from PIL import Image
        print("✅ Pillow imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Pillow: {e}")
        return False
    
    try:
        import requests
        print("✅ Requests imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Requests: {e}")
        return False
    
    try:
        from dotenv import load_dotenv
        print("✅ python-dotenv imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import python-dotenv: {e}")
        return False
    
    try:
        import torchvision
        print(f"✅ TorchVision imported successfully (version: {torchvision.__version__})")
    except ImportError as e:
        print(f"❌ Failed to import TorchVision: {e}")
        return False
    
    return True

def test_config():
    """Test configuration loading."""
    print("\n🔍 Testing configuration...")
    
    try:
        from config import MODEL_NAME, MAX_LENGTH, NUM_BEAMS, TEMPERATURE
        print(f"✅ Configuration loaded successfully")
        print(f"   Model: {MODEL_NAME}")
        print(f"   Max Length: {MAX_LENGTH}")
        print(f"   Beams: {NUM_BEAMS}")
        print(f"   Temperature: {TEMPERATURE}")
        return True
    except Exception as e:
        print(f"❌ Failed to load configuration: {e}")
        return False

def test_components():
    """Test if bot components can be initialized."""
    print("\n🔍 Testing components...")
    
    try:
        from image_processor import ImageProcessor
        processor = ImageProcessor()
        print("✅ ImageProcessor initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize ImageProcessor: {e}")
        return False
    
    try:
        from caption_model import CaptionModel
        print("✅ CaptionModel imported successfully")
        print("   Note: Model will be downloaded on first use")
        return True
    except Exception as e:
        print(f"❌ Failed to import CaptionModel: {e}")
        return False

def test_environment():
    """Test environment setup."""
    print("\n🔍 Testing environment...")
    
    # Check if .env file exists
    env_file = Path(".env")
    if env_file.exists():
        print("✅ .env file found")
        
        # Load and check BOT_TOKEN
        from dotenv import load_dotenv
        load_dotenv()
        
        bot_token = os.getenv('BOT_TOKEN')
        if bot_token and bot_token != "your_telegram_bot_token_here":
            print("✅ BOT_TOKEN is set")
        else:
            print("⚠️  BOT_TOKEN not set or using default value")
            print("   Please set your actual bot token in .env file")
    else:
        print("⚠️  .env file not found")
        print("   Please create .env file with your BOT_TOKEN")
    
    return True

def test_cuda():
    """Test CUDA availability."""
    print("\n🔍 Testing CUDA availability...")
    
    try:
        import torch
        if torch.cuda.is_available():
            print(f"✅ CUDA available: {torch.cuda.get_device_name(0)}")
            print(f"   CUDA version: {torch.version.cuda}")
        else:
            print("ℹ️  CUDA not available, will use CPU")
        return True
    except Exception as e:
        print(f"❌ Error checking CUDA: {e}")
        return False

def main():
    """Run all tests."""
    print("🚀 Testing Telegram Image Description Bot Setup")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_config,
        test_components,
        test_environment,
        test_cuda
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your setup is ready.")
        print("\nNext steps:")
        print("1. Set your BOT_TOKEN in .env file")
        print("2. Run: python bot.py")
        print("3. Start your bot in Telegram with /start")
    else:
        print("❌ Some tests failed. Please fix the issues above.")
        print("\nCommon solutions:")
        print("1. Install missing dependencies: pip install -r requirements.txt")
        print("2. Check your Python version (3.8+ required)")
        print("3. Set up your .env file with BOT_TOKEN")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 