# Deploying Telegram Image Bot on Replit

This guide will help you deploy your Telegram Image Bot on Replit.

## Prerequisites

1. **Telegram Bot Token**: You need a bot token from [@BotFather](https://t.me/botfather)
2. **Replit Account**: Sign up at [replit.com](https://replit.com)

## Step-by-Step Deployment

### 1. Create a New Repl

1. Go to [replit.com](https://replit.com) and sign in
2. Click "Create Repl"
3. Choose "Import from GitHub" 
4. Enter your repository URL or upload your files

### 2. Set Up Environment Variables

1. In your Repl, click on the "Secrets" tab (lock icon)
2. Add a new secret:
   - **Key**: `BOT_TOKEN`
   - **Value**: Your Telegram bot token from @BotFather

### 3. Configure the Repl

The following files are already set up for you:

- `.replit` - Tells Replit how to run your bot
- `replit.nix` - Provides necessary system dependencies
- `start.sh` - Startup script with error handling

### 4. Run the Bot

1. Click the "Run" button in Replit
2. The bot will automatically:
   - Install Python dependencies
   - Download the BLIP model (first run only)
   - Start the bot

### 5. Keep the Bot Running

To keep your bot running 24/7:

1. **Use UptimeRobot** (Recommended):
   - Sign up at [uptimerobot.com](https://uptimerobot.com)
   - Add a new monitor
   - Set the URL to your Repl's webview URL
   - Set check interval to 5 minutes

2. **Alternative**: Use Replit's built-in "Always On" feature (requires Replit Pro)

## Troubleshooting

### Common Issues

1. **"BOT_TOKEN not set"**
   - Make sure you've added the secret in the Secrets tab
   - Check that the key is exactly `BOT_TOKEN`

2. **Model download fails**
   - This is normal on first run
   - The model is large (~1GB) and may take several minutes
   - Check the console for download progress

3. **Bot doesn't respond**
   - Check the console for error messages
   - Verify your bot token is correct
   - Make sure the bot is running (green "Run" button)

### Performance Notes

- **First Run**: Model download may take 5-10 minutes
- **Memory Usage**: The BLIP model uses ~2GB RAM
- **Response Time**: Image processing takes 3-5 seconds per image

## Monitoring

- Check the console for bot logs
- Monitor memory usage in Replit's stats
- Use `/status` command in Telegram to check bot health

## Security

- Never share your bot token
- Keep your Repl private if needed
- Regularly rotate your bot token

## Support

If you encounter issues:
1. Check the console logs
2. Verify all environment variables are set
3. Try restarting the Repl
4. Check Replit's status page for service issues

Your bot should now be running and ready to process images! 🎉 