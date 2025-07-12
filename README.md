# Telegram Image Description Bot

A powerful Telegram bot that converts images to detailed text descriptions using the Salesforce BLIP image captioning model. The bot provides accurate and comprehensive descriptions of all objects and details in uploaded images.

## Features

- 🤖 **Powered by Salesforce BLIP Model**: Uses the state-of-the-art BLIP image captioning model for accurate descriptions
- 📸 **Multiple Image Formats**: Supports JPG, PNG, BMP, and WebP formats
- 🔍 **Detailed Descriptions**: Provides comprehensive descriptions of all objects and scenes in images
- ⚡ **Fast Processing**: Optimized for quick response times
- 🛡️ **Error Handling**: Robust error handling and user-friendly messages
- 📱 **Telegram Integration**: Seamless integration with Telegram's interface

## Requirements

- Python 3.8 or higher
- Telegram Bot Token (get from @BotFather)
- Internet connection for model downloads and Telegram API

## Installation

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd telegram-image-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Copy `env_example.txt` to `.env`
   - Add your Telegram bot token:
   ```
   BOT_TOKEN=your_actual_bot_token_here
   ```

4. **Get a Telegram Bot Token**
   - Open Telegram and search for @BotFather
   - Send `/newbot` command
   - Follow the instructions to create your bot
   - Copy the token and add it to your `.env` file

## Usage

1. **Run the bot**
   ```bash
   python bot.py
   ```

2. **Start the bot in Telegram**
   - Find your bot in Telegram
   - Send `/start` to begin

3. **Send images**
   - Send any image to the bot
   - Wait for the detailed description
   - The bot will describe all objects and details it can see

## Bot Commands

- `/start` - Start the bot and see welcome message
- `/help` - Show help information and usage tips
- `/status` - Show bot and model status information

## How It Works

1. **Image Processing**: The bot downloads and validates incoming images
2. **Preprocessing**: Images are converted to RGB format and resized if necessary
3. **Caption Generation**: The BLIP model analyzes the image and generates detailed descriptions
4. **Response**: The bot sends back a formatted description of the image

## Model Configuration

The bot uses the following optimized settings for the BLIP model:

- **Model**: `Salesforce/blip-image-captioning-base`
- **Max Length**: 100 tokens
- **Beam Search**: 5 beams for better quality
- **Temperature**: 1.0 for balanced creativity and accuracy
- **Top-p**: 0.9 for controlled randomness
- **Repetition Penalty**: 1.5 to avoid repetitive text

## Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- WebP (.webp)

## Error Handling

The bot includes comprehensive error handling for:
- Invalid image formats
- Corrupted images
- Network issues
- Model loading errors
- Processing failures

## Performance Tips

- **Image Size**: Images under 1024px work best
- **Image Quality**: Clear, well-lit images provide better descriptions
- **Content**: Images with recognizable objects work best
- **Format**: JPEG and PNG are recommended

## Troubleshooting

### Common Issues

1. **Bot not responding**
   - Check if the bot token is correct
   - Ensure the bot is running
   - Check internet connection

2. **Model loading errors**
   - Ensure you have enough disk space for model downloads
   - Check internet connection for initial model download
   - Verify PyTorch installation

3. **Image processing errors**
   - Try sending a different image
   - Check image format and size
   - Ensure image is not corrupted

4. **Installation issues with Python 3.13+**
   - The bot requires PyTorch 2.6.0+ for Python 3.13
   - If installation fails, try: `pip install -r requirements_minimal.txt`
   - Or install manually: `pip install python-telegram-bot transformers torch torchvision Pillow requests python-dotenv`

### Getting Help

If you encounter issues:
1. Check the console output for error messages
2. Verify your bot token is correct
3. Ensure all dependencies are installed
4. Try restarting the bot
5. Run `python test_setup.py` to diagnose issues

## Technical Details

### Architecture

- **bot.py**: Main bot logic and Telegram handlers
- **caption_model.py**: BLIP model integration and caption generation
- **image_processor.py**: Image downloading, validation, and preprocessing
- **config.py**: Configuration settings and constants

### Dependencies

- `python-telegram-bot`: Telegram Bot API wrapper
- `transformers`: Hugging Face transformers library for BLIP model
- `torch`: PyTorch for deep learning
- `Pillow`: Image processing
- `requests`: HTTP requests for image downloading
- `python-dotenv`: Environment variable management

## Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Improving documentation
- Optimizing performance

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Salesforce for the BLIP image captioning model
- Telegram for the Bot API
- Hugging Face for the transformers library 