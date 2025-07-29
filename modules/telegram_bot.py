#!/usr/bin/env python3
"""
Telegram Bot Module for NeuraX AI Tool
Author: Alex Butler [Vritra Security Organization]
Version: 1.0.0
NeuraX is prepared with well-structured comments by Alex for future contributors.
"""

import asyncio
import logging
import json
import sys
import os
import time
from typing import Optional, Dict
from datetime import datetime
import requests

os.environ['TZ'] = 'UTC'
try:
    time.tzset()
except AttributeError:
    pass 

try:
    from telegram import Update
    from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
    import pytz
   
    TELEGRAM_AVAILABLE = True
except ImportError:
    TELEGRAM_AVAILABLE = False

from .colors import Colors
from .config import ConfigManager
from .ai_client import PerplexityAI

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class TelegramBot:
    """Telegram bot for NeuraX AI"""
    
    def __init__(self, config_manager: ConfigManager):
        self.config_manager = config_manager
        self.bot_token = config_manager.get_telegram_token()
        self.api_key = config_manager.get_api_key()
        self.user_sessions = {}  # Store user chat sessions
        
        if not self.bot_token:
            raise ValueError("Telegram bot token not configured")
        
        if not self.api_key:
            raise ValueError("Perplexity API key not configured")
        
        # Set timezone environment variable to UTC to avoid pytz errors
        os.environ['TZ'] = 'UTC'
        try:
            time.tzset()  # Apply the timezone change
        except AttributeError:
            pass  # tzset not available on all platforms
        
        # Configure timezone to avoid pytz errors - multiple fallback approaches
        timezone = None
        try:
            import pytz
            timezone = pytz.UTC  # Use UTC as default timezone
        except ImportError:
            try:
                from datetime import timezone as dt_timezone
                timezone = dt_timezone.utc  # Fallback to datetime.timezone
            except ImportError:
                timezone = None
        
        # Build application without explicit timezone to avoid pytz errors
        # The TZ environment variable set above should handle timezone issues
        self.application = Application.builder().token(self.bot_token).build()
        self.setup_handlers()
    
    def get_user_ai(self, user_id: int) -> PerplexityAI:
        """Get or create AI instance for user"""
        if user_id not in self.user_sessions:
            self.user_sessions[user_id] = PerplexityAI(self.api_key)
        return self.user_sessions[user_id]
    
    def setup_handlers(self):
        """Setup bot command and message handlers"""
        # Command handlers
        self.application.add_handler(CommandHandler("start", self.start_command))
        self.application.add_handler(CommandHandler("help", self.help_command))
        self.application.add_handler(CommandHandler("clear", self.clear_command))
        self.application.add_handler(CommandHandler("about", self.about_command))
        self.application.add_handler(CommandHandler("status", self.status_command))
        
        # Message handler for all text messages
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command"""
        user = update.effective_user
        welcome_message = f"""
🧠 **Welcome to NeuraX AI Assistant!**

Hello {user.first_name}! I'm your AI-powered assistant using Perplexity AI.

**How to use:**
• Simply send me any message and I'll respond with AI-generated answers
• Use /help to see available commands
• Use /clear to reset our conversation
• Use /about for information about this bot

**Features:**
✔ Natural conversation with AI
✔ Context-aware responses
✔ Multiple user support
✔ Chat history per user

Ready to chat? Send me your first question! 🚀
"""
        await update.message.reply_text(welcome_message, parse_mode='Markdown')
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /help command"""
        help_message = """
🆘 **Available Commands:**

/start - Welcome message and bot introduction
/help - Show this help message
/clear - Clear your chat history with the bot
/about - Information about this bot and developer
/status - Check bot status and configuration

**Usage:**
Just send me any text message and I'll respond with AI-generated answers using Perplexity AI. No special commands needed for regular chat!

**Features:**
• Real-time AI responses
• Context-aware conversations
• Individual chat history for each user
• Professional and concise answers

Need support? Contact the developer using the /about command.
"""
        await update.message.reply_text(help_message, parse_mode='Markdown')
    
    async def clear_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /clear command"""
        user_id = update.effective_user.id
        if user_id in self.user_sessions:
            self.user_sessions[user_id].reset_conversation()
            await update.message.reply_text("✔ Your chat history has been cleared! Starting fresh conversation.")
        else:
            await update.message.reply_text("✔ Chat history cleared! Send me a message to start a new conversation.")
    
    async def about_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /about command"""
        about_message = """
🧠 **About NeuraX AI Assistant Bot**

**Bot Information:**
• Name: NeuraX AI Assistant
• Version: 1.0.0
• Developer: Alex Butler [Vritra Security Organization]
• Created: 2025

**Description:**
This bot provides access to Perplexity AI through Telegram, offering intelligent responses to your questions and engaging in meaningful conversations.

**Technologies:**
• Perplexity AI API
• Python Telegram Bot
• Async/await architecture
• Per-user session management
• Professional modular architecture

**Developer Contact:**
🐙 GitHub: https://github.com/VritraSecz
🌐 Website: https://vritrasec.com
📸 Instagram: https://instagram.com/haxorlex
▶️ YouTube: https://youtube.com/@Technolex
📢 Telegram (Central): https://t.me/LinkCentralX
⚡ Telegram (Main Channel): https://t.me/VritraSec
💬 Telegram (Community): https://t.me/VritraSecz
🤖 Support Bot: https://t.me/ethicxbot

**Support:**
If you encounter any issues or have feature requests, please contact the developer through any of the above channels.

⭐ If you find NeuraX helpful, please share it with others!
"""
        await update.message.reply_text(about_message, parse_mode='Markdown')
    
    async def status_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /status command"""
        user_id = update.effective_user.id
        user_has_session = user_id in self.user_sessions
        
        status_message = f"""
📊 **NeuraX Bot Status:**

✔ Bot is running normally
✔ Perplexity AI API is configured
✔ Telegram connection is active

**Your Session:**
• Chat History: {'Active' if user_has_session else 'No active session'}
• Messages in History: {len(self.user_sessions[user_id].chat_history) - 1 if user_has_session else 0}

**Bot Statistics:**
• Active Users: {len(self.user_sessions)}
• Uptime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

All systems operational! 🚀
"""
        await update.message.reply_text(status_message, parse_mode='Markdown')
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle regular text messages"""
        user = update.effective_user
        user_id = user.id
        message_text = update.message.text
        
        # Log the message
        logger.info(f"User {user.first_name} ({user_id}): {message_text}")
        
        try:
            # Send typing indicator
            await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
            
            # Get AI response
            ai = self.get_user_ai(user_id)
            response = ai.send_message(message_text)
            
            if response:
                # Send response to user
                await update.message.reply_text(response)
                logger.info(f"NeuraX response sent to {user.first_name} ({user_id})")
            else:
                # Handle API error
                error_message = "✘ Sorry, I encountered an error while processing your request. Please try again later."
                await update.message.reply_text(error_message)
                logger.error(f"Failed to get AI response for user {user_id}")
                
        except Exception as e:
            # Handle any unexpected errors
            logger.error(f"Error handling message from user {user_id}: {str(e)}")
            error_message = "✘ An unexpected error occurred. The developer has been notified. Please try again later."
            await update.message.reply_text(error_message)
    
    async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle errors"""
        logger.error(f"Update {update} caused error {context.error}")
    
    def run(self):
        """Start the bot"""
        print(f"{Colors.BRIGHT_GREEN}🤖 Starting NeuraX Telegram Bot...{Colors.RESET}")
        print(f"{Colors.BRIGHT_CYAN}Bot is running! Users can now interact with NeuraX.{Colors.RESET}")
        print(f"{Colors.DIM}Press Ctrl+C to stop the bot{Colors.RESET}\n")
        
        # Add error handler
        self.application.add_error_handler(self.error_handler)
        
        # Start the bot
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)

def install_telegram_dependencies():
    """Install required telegram dependencies"""
    print(f"{Colors.BRIGHT_YELLOW}📦 Installing Telegram Bot dependencies...{Colors.RESET}")
    
    try:
        import subprocess
        import sys
        
        # Install python-telegram-bot and pytz for timezone support
        packages = ["python-telegram-bot==21.5", "pytz"]
        for package in packages:
            result = subprocess.run([
                sys.executable, "-m", "pip", "install", package
            ], capture_output=True, text=True)
            
            if result.returncode != 0:
                print(f"{Colors.RED}✘ Failed to install {package}: {result.stderr}{Colors.RESET}")
                return False
        
        print(f"{Colors.BRIGHT_GREEN}✔ Telegram Bot dependencies installed successfully!{Colors.RESET}")
        print(f"{Colors.DIM}Please restart NeuraX to use the bot functionality.{Colors.RESET}")
        return True
            
    except Exception as e:
        print(f"{Colors.RED}✘ Error installing dependencies: {e}{Colors.RESET}")
        return False

def start_bot(config_manager: ConfigManager):
    """Start the Telegram bot with proper signal handling"""
    # Set timezone environment variable to UTC before anything else
    os.environ['TZ'] = 'UTC'
    try:
        time.tzset()  # Apply the timezone change
    except AttributeError:
        pass  # tzset not available on all platforms
    
    # Setup signal handler for Ctrl+C
    def signal_handler(sig, frame):
        print(f"\n{Colors.BRIGHT_YELLOW}🛑 NeuraX bot interrupted safely. Goodbye!{Colors.RESET}")
        sys.exit(0)
    
    import signal
    signal.signal(signal.SIGINT, signal_handler)
    
    try:
        if not TELEGRAM_AVAILABLE:
            print(f"{Colors.RED}✘ Telegram Bot dependencies not found!{Colors.RESET}")
            print(f"{Colors.BRIGHT_YELLOW}The python-telegram-bot library is required for bot functionality.{Colors.RESET}")
            
            try:
                choice = input(f"{Colors.BRIGHT_CYAN}Would you like to install it now? (y/n): {Colors.RESET}").lower().strip()
                if choice in ['y', 'yes']:
                    if install_telegram_dependencies():
                        print(f"{Colors.BRIGHT_GREEN}Please restart NeuraX to use the bot.{Colors.RESET}")
                    return
                else:
                    print(f"{Colors.BRIGHT_YELLOW}Bot functionality will not be available without the required dependencies.{Colors.RESET}")
                    return
            except KeyboardInterrupt:
                signal_handler(signal.SIGINT, None)
        
        # Check if bot token is configured
        bot_token = config_manager.get_telegram_token()
        if not bot_token:
            print(f"{Colors.RED}✘ No Telegram bot token configured!{Colors.RESET}")
            # Import here to avoid circular imports
            import sys
            sys.path.append(os.path.dirname(os.path.dirname(__file__)))
            from neurax import configure_telegram_token
            try:
                configure_telegram_token(config_manager)
                bot_token = config_manager.get_telegram_token()
                if not bot_token:
                    return
            except KeyboardInterrupt:
                signal_handler(signal.SIGINT, None)
        
        # Check if API key is configured
        api_key = config_manager.get_api_key()
        if not api_key:
            print(f"{Colors.RED}✘ No Perplexity API key configured!{Colors.RESET}")
            # Import here to avoid circular imports
            import sys
            sys.path.append(os.path.dirname(os.path.dirname(__file__)))
            from neurax import configure_api_key
            try:
                configure_api_key(config_manager)
                api_key = config_manager.get_api_key()
                if not api_key:
                    return
            except KeyboardInterrupt:
                signal_handler(signal.SIGINT, None)
        
        # Create and start bot
        bot = TelegramBot(config_manager)
        bot.run()
        
    except ValueError as e:
        print(f"{Colors.RED}✘ Configuration Error: {e}{Colors.RESET}")
    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)
    except Exception as e:
        print(f"{Colors.RED}✘ Error starting NeuraX bot: {e}{Colors.RESET}")
        logger.error(f"Bot startup error: {str(e)}")

if __name__ == "__main__":
    # For testing purposes
    from .config import ConfigManager
    config_manager = ConfigManager()
    start_bot(config_manager)
