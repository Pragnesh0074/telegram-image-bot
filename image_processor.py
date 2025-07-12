import os
import requests
from PIL import Image
import io
from typing import Optional, Tuple
import logging
from config import MAX_IMAGE_SIZE, SUPPORTED_FORMATS

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ImageProcessor:
    """Handles image processing and validation for the BLIP model."""
    
    def __init__(self):
        self.max_size = MAX_IMAGE_SIZE
        self.supported_formats = SUPPORTED_FORMATS
    
    def download_image(self, file_path: str) -> Optional[Image.Image]:
        """
        Download image from Telegram file path.
        
        Args:
            file_path: Telegram file path
            
        Returns:
            PIL Image object or None if failed
        """
        try:
            # Construct the correct URL for downloading Telegram files
            bot_token = os.getenv('BOT_TOKEN')
            if not bot_token:
                logger.error("BOT_TOKEN not found in environment variables")
                return None
            
            # Check if file_path already contains the base URL
            if file_path.startswith('https://api.telegram.org/file/bot'):
                download_url = file_path
            elif file_path.startswith('http'):
                download_url = file_path
            else:
                # The file_path from Telegram is relative, so we need to construct the full URL
                download_url = f"https://api.telegram.org/file/bot{bot_token}/{file_path}"
            
            logger.info(f"Downloading image from: {download_url}")
            
            # Download the file from Telegram
            response = requests.get(download_url, timeout=30)
            response.raise_for_status()
            
            # Open image from bytes
            image = Image.open(io.BytesIO(response.content))
            logger.info(f"Successfully downloaded image: {image.size} {image.mode}")
            return image
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Network error downloading image: {e}")
            return None
        except Exception as e:
            logger.error(f"Error downloading image: {e}")
            return None
    
    def validate_image(self, image: Image.Image) -> Tuple[bool, str]:
        """
        Validate image format and size.
        
        Args:
            image: PIL Image object
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        try:
            # Map file extensions to PIL format names
            format_mapping = {
                '.jpg': 'JPEG',
                '.jpeg': 'JPEG', 
                '.png': 'PNG',
                '.bmp': 'BMP',
                '.webp': 'WEBP'
            }
            
            # Get supported PIL format names
            supported_pil_formats = [format_mapping[fmt] for fmt in self.supported_formats if fmt in format_mapping]
            
            # Check image format
            if not image.format or image.format.upper() not in supported_pil_formats:
                return False, f"Unsupported image format. Supported formats: {', '.join(self.supported_formats)}"
            
            # Note: Size validation is now handled in preprocess_image with auto-resizing
            # Only reject extremely large images (over 4x the max size)
            if max(image.size) > self.max_size * 4:
                return False, f"Image too large. Maximum size: {self.max_size * 4}px"
            
            return True, ""
            
        except Exception as e:
            return False, f"Invalid image: {str(e)}"
    
    def preprocess_image(self, image: Image.Image) -> Image.Image:
        """
        Preprocess image for BLIP model.
        
        Args:
            image: PIL Image object
            
        Returns:
            Preprocessed PIL Image object
        """
        try:
            # Convert to RGB if necessary
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Resize if too large while maintaining aspect ratio
            if max(image.size) > self.max_size:
                ratio = self.max_size / max(image.size)
                new_size = (int(image.size[0] * ratio), int(image.size[1] * ratio))
                image = image.resize(new_size, Image.Resampling.LANCZOS)
            
            return image
            
        except Exception as e:
            logger.error(f"Error preprocessing image: {e}")
            raise
    
    def process_telegram_image(self, file_path: str) -> Optional[Image.Image]:
        """
        Complete image processing pipeline for Telegram images.
        
        Args:
            file_path: Telegram file path
            
        Returns:
            Processed PIL Image object or None if failed
        """
        try:
            # Download image
            image = self.download_image(file_path)
            if image is None:
                return None
            
            # Validate image
            is_valid, error_msg = self.validate_image(image)
            if not is_valid:
                logger.error(f"Image validation failed: {error_msg}")
                return None
            
            # Preprocess image
            processed_image = self.preprocess_image(image)
            
            return processed_image
            
        except Exception as e:
            logger.error(f"Error processing image: {e}")
            return None 