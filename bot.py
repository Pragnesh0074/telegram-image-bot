import asyncio
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.constants import ParseMode

from config import BOT_TOKEN, WELCOME_MESSAGE, ERROR_MESSAGE, PROCESSING_MESSAGE
from image_processor import ImageProcessor
from caption_model import CaptionModel

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class ImageCaptionBot:
    """Telegram bot for image captioning using BLIP model."""
    
    def __init__(self):
        self.image_processor = ImageProcessor()
        self.caption_model = CaptionModel()
        logger.info("Bot initialized successfully!")
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command."""
        if update.message is not None:
            await update.message.reply_text(
                WELCOME_MESSAGE,
                parse_mode=ParseMode.HTML
            )
        else:
            logger.warning("No message found in update for /start command.")
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /help command."""
        if update.message is None:
            logger.warning("No message found in update for /help command.")
            return
            
        help_text = """
🤖 <b>Image Description Bot Help</b>

<b>Commands:</b>
/start - Start the bot and see welcome message
/help - Show this help message
/status - Show bot and model status

<b>How to use:</b>
1. Send me any image (JPG, PNG, BMP, WebP)
2. I'll analyze it and provide a detailed description
3. The description will include all objects and details I can see

<b>Features:</b>
• Powered by Salesforce BLIP model
• Accurate object detection
• Detailed scene descriptions
• Support for various image formats

<b>Tips:</b>
• Send clear, well-lit images for best results
• Images should be under 1024px for optimal processing
• The bot works best with images containing recognizable objects
        """
        await update.message.reply_text(help_text, parse_mode=ParseMode.HTML)
    
    async def status_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /status command."""
        if update.message is None:
            logger.warning("No message found in update for /status command.")
            return
            
        model_info = self.caption_model.get_model_info()
        status_text = f"""
🤖 <b>Bot Status</b>

<b>Model Information:</b>
• Model: {model_info['model_name']}
• Device: {model_info['device']}
• Max Length: {model_info['max_length']}
• Beams: {model_info['num_beams']}
• Temperature: {model_info['temperature']}

<b>Bot Status:</b>
✅ Ready to process images
✅ Model loaded successfully
✅ Image processor initialized
        """
        await update.message.reply_text(status_text, parse_mode=ParseMode.HTML)
    
    async def handle_image(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle incoming images."""
        if update.message is None:
            logger.warning("No message found in update for image handling.")
            return
            
        try:
            # Get the photo with highest quality
            photo = update.message.photo[-1]
            
            # Send processing message
            processing_msg = await update.message.reply_text(PROCESSING_MESSAGE)
            
            # Get file path
            file = await context.bot.get_file(photo.file_id)
            file_path = file.file_path
            
            if file_path is None:
                await processing_msg.edit_text(ERROR_MESSAGE)
                return
            
            # Process image
            processed_image = self.image_processor.process_telegram_image(file_path)
            
            if processed_image is None:
                await processing_msg.edit_text(ERROR_MESSAGE)
                return
            
            # Generate caption
            caption = self.caption_model.generate_caption(processed_image)
            
            if caption is None:
                await processing_msg.edit_text(ERROR_MESSAGE)
                return
            
            # Send the caption
            response_text = f"📸 <b>Image Description:</b>\n\n{caption}"
            await processing_msg.edit_text(response_text, parse_mode=ParseMode.HTML)
            
            user_id = update.effective_user.id if update.effective_user else "unknown"
            logger.info(f"Successfully processed image for user {user_id}")
            
        except Exception as e:
            logger.error(f"Error handling image: {e}")
            if update.message:
                await update.message.reply_text(ERROR_MESSAGE)
    
    async def handle_document(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle document uploads (images sent as files)."""
        if update.message is None:
            logger.warning("No message found in update for document handling.")
            return
            
        try:
            document = update.message.document
            
            if document is None:
                await update.message.reply_text("❌ Please send an image file (JPG, PNG, etc.)")
                return
            
            # Check if it's an image
            if not document.mime_type or not document.mime_type.startswith('image/'):
                await update.message.reply_text("❌ Please send an image file (JPG, PNG, etc.)")
                return
            
            # Send processing message
            processing_msg = await update.message.reply_text(PROCESSING_MESSAGE)
            
            # Get file path
            file = await context.bot.get_file(document.file_id)
            file_path = file.file_path
            
            if file_path is None:
                await processing_msg.edit_text(ERROR_MESSAGE)
                return
            
            # Process image
            processed_image = self.image_processor.process_telegram_image(file_path)
            
            if processed_image is None:
                await processing_msg.edit_text(ERROR_MESSAGE)
                return
            
            # Generate caption
            caption = self.caption_model.generate_caption(processed_image)
            
            if caption is None:
                await processing_msg.edit_text(ERROR_MESSAGE)
                return
            
            # Send the caption
            response_text = f"📸 <b>Image Description:</b>\n\n{caption}"
            await processing_msg.edit_text(response_text, parse_mode=ParseMode.HTML)
            
            user_id = update.effective_user.id if update.effective_user else "unknown"
            logger.info(f"Successfully processed document for user {user_id}")
            
        except Exception as e:
            logger.error(f"Error handling document: {e}")
            if update.message:
                await update.message.reply_text(ERROR_MESSAGE)
    
    async def handle_text(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle text messages."""
        if update.message is None:
            logger.warning("No message found in update for text handling.")
            return
            
        await update.message.reply_text(
            "📸 Please send me an image to describe! Use /help for more information."
        )
    
    async def on_startup(self, application: Application):
        """Called when the bot starts up."""
        logger.info("🎉 Bot startup complete!")
        logger.info("📊 Model info:")
        model_info = self.caption_model.get_model_info()
        for key, value in model_info.items():
            logger.info(f"   {key}: {value}")
        logger.info("✅ Bot is ready to process images!")

    def run(self):
        """Run the bot."""
        if BOT_TOKEN is None:
            logger.error("BOT_TOKEN is not set in environment variables")
            raise ValueError("BOT_TOKEN is required")
            
        logger.info("🤖 Initializing Image Caption Bot...")
        logger.info("📥 Loading BLIP model...")
        
        # Create application
        application = Application.builder().token(BOT_TOKEN).build()
        
        # Add handlers
        application.add_handler(CommandHandler("start", self.start_command))
        application.add_handler(CommandHandler("help", self.help_command))
        application.add_handler(CommandHandler("status", self.status_command))
        
        # Handle images
        application.add_handler(MessageHandler(filters.PHOTO, self.handle_image))
        
        # Handle documents (images sent as files)
        application.add_handler(MessageHandler(filters.Document.IMAGE, self.handle_document))
        
        # Handle text messages
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_text))
        
        # Add startup callback
        application.post_init = self.on_startup
        
        # Start the bot
        logger.info("🚀 Starting bot...")
        logger.info("✅ Bot is now running and ready to receive messages!")
        logger.info("📱 You can now send images to your bot on Telegram")
        logger.info("🛑 Press Ctrl+C to stop the bot")
        
        try:
            application.run_polling(allowed_updates=Update.ALL_TYPES)
        except KeyboardInterrupt:
            logger.info("🛑 Bot stopped by user")
        except Exception as e:
            logger.error(f"❌ Bot crashed: {e}")
            raise

def main():
    """Main function to run the bot."""
    try:
        bot = ImageCaptionBot()
        bot.run()
    except Exception as e:
        logger.error(f"Error running bot: {e}")
        raise

if __name__ == "__main__":
    main() 