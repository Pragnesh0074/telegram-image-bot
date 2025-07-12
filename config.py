import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot Configuration
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is required")

# Model Configuration
MODEL_NAME = "Salesforce/blip-image-captioning-base"
MAX_LENGTH = 100
NUM_BEAMS = 5
TEMPERATURE = 1.0

# Image Processing
MAX_IMAGE_SIZE = 5120 # Maximum image size to process
SUPPORTED_FORMATS = ['.jpg', '.jpeg', '.png', '.bmp', '.webp']

# Bot Messages
WELCOME_MESSAGE = """
🤖 Welcome to the Image Description Bot!

I can analyze images and provide detailed descriptions of what I see.

📸 Simply send me an image and I'll describe it for you!

Features:
• Accurate object detection
• Detailed scene descriptions
• Support for various image formats
• Powered by Salesforce BLIP model

Send an image to get started!
"""

ERROR_MESSAGE = "❌ Sorry, I encountered an error processing your image. Please try again with a different image."

PROCESSING_MESSAGE = "🔄 Analyzing your image... Please wait a moment." 