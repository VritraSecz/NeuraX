#!/usr/bin/env python3
"""
NeuraX AI Tool - A powerful CLI and Telegram bot interface for Perplexity AI
Author: Alex Butler [Vritra Security Organization]
Version: 1.0.0
NeuraX is prepared with well-structured comments by Alex for future contributors.
"""

import argparse
import signal
import sys
from modules import (
    Colors, print_banner, ConfigManager, PerplexityAI,
    clear_screen, get_input_with_prompt, print_about, 
    print_connect, print_help
)

def configure_api_key(config_manager: ConfigManager):
    """Configure Perplexity API key"""
    print(f"\n{Colors.BRIGHT_CYAN}🔑 Configure Perplexity AI API Key{Colors.RESET}")
    print(f"{Colors.DIM}Get your API key from: https://www.perplexity.ai/settings/api{Colors.RESET}\n")
    
    api_key = get_input_with_prompt("Enter your Perplexity API key: ", is_password=True)
    if api_key.strip():
        config_manager.set_api_key(api_key.strip())
        print(f"{Colors.GREEN}✔ API key configured successfully!{Colors.RESET}")
    else:
        print(f"{Colors.RED}✘ No API key provided{Colors.RESET}")

def configure_telegram_token(config_manager: ConfigManager):
    """Configure Telegram bot token"""
    print(f"\n{Colors.BRIGHT_CYAN}🤖 Configure Telegram Bot Token{Colors.RESET}")
    print(f"{Colors.DIM}Get your bot token from: @BotFather on Telegram{Colors.RESET}\n")
    
    token = get_input_with_prompt("Enter your Telegram bot token: ", is_password=True)
    if token.strip():
        config_manager.set_telegram_token(token.strip())
        print(f"{Colors.GREEN}✔ Telegram bot token configured successfully!{Colors.RESET}")
    else:
        print(f"{Colors.RED}✘ No token provided{Colors.RESET}")

def cli_chat_mode(config_manager: ConfigManager):
    """Start CLI chat mode"""
    api_key = config_manager.get_api_key()
    
    if not api_key:
        print(f"{Colors.RED}✘ No API key configured!{Colors.RESET}")
        configure_api_key(config_manager)
        api_key = config_manager.get_api_key()
        if not api_key:
            return
    
    ai = PerplexityAI(api_key)
    
    print(f"\n{Colors.BRIGHT_GREEN}🚀 Starting NeuraX CLI Chat Mode{Colors.RESET}")
    print(f"{Colors.DIM}Type 'exit', 'quit', or 'bye' to stop{Colors.RESET}")
    print(f"{Colors.DIM}Type 'clear' to clear chat history{Colors.RESET}")
    print(f"{Colors.DIM}Type 'help' for commands{Colors.RESET}\n")
    
    while True:
        try:
            user_input = get_input_with_prompt("💬 You: ")
            
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print(f"{Colors.BRIGHT_YELLOW}👋 Goodbye! NeuraX chat session ended.{Colors.RESET}")
                break
            
            if user_input.lower() == 'clear':
                ai.reset_conversation()
                print(f"{Colors.BRIGHT_GREEN}✔ Chat history cleared{Colors.RESET}")
                continue
            
            if user_input.lower() == 'help':
                print(f"""
{Colors.BRIGHT_CYAN}Available Commands:{Colors.RESET}
{Colors.BRIGHT_WHITE}• exit/quit/bye{Colors.RESET} - Exit chat mode
{Colors.BRIGHT_WHITE}• clear{Colors.RESET} - Clear chat history
{Colors.BRIGHT_WHITE}• help{Colors.RESET} - Show this help message
""")
                continue
            
            if not user_input.strip():
                continue
            
            print(f"{Colors.BRIGHT_BLUE}🧠 NeuraX: {Colors.RESET}", end="", flush=True)
            
            response = ai.send_message(user_input)
            if response:
                print(f"{Colors.BRIGHT_WHITE}{response}{Colors.RESET}\n")
            else:
                print(f"{Colors.RED}✘ Failed to get response from AI{Colors.RESET}\n")
                
        except KeyboardInterrupt:
            print(f"\n{Colors.BRIGHT_YELLOW}👋 NeuraX chat interrupted. Goodbye!{Colors.RESET}")
            break
        except Exception as e:
            print(f"{Colors.RED}✘ Error: {e}{Colors.RESET}")

def signal_handler(sig, frame):
    """Handle Ctrl+C signal for safe exit"""
    print(f"\n{Colors.BRIGHT_YELLOW}🛑 NeuraX interrupted safely. Goodbye!{Colors.RESET}")
    sys.exit(0)

'''
def print_argument_help(arg_name: str):
    """Print help for specific argument"""
    help_messages = {
        '--api': f"""
{Colors.BRIGHT_CYAN}╔══════════════════════════════════════════════════════════════════════╗
║                        {Colors.BRIGHT_YELLOW}--api ARGUMENT HELP{Colors.BRIGHT_CYAN}                           ║
╚══════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.BRIGHT_WHITE}Description:{Colors.RESET}
Configure Perplexity AI API key for NeuraX tool.

{Colors.BRIGHT_WHITE}Usage:{Colors.RESET}
{Colors.BRIGHT_GREEN}python neurax.py --api{Colors.RESET}                    # Interactive mode
{Colors.BRIGHT_GREEN}python neurax.py --api sk-proj-yourkey{Colors.RESET}    # Direct inline input

{Colors.BRIGHT_WHITE}Examples:{Colors.RESET}
{Colors.BRIGHT_GREEN}python neurax.py --api sk-proj-1234567890abcdef{Colors.RESET}
{Colors.BRIGHT_GREEN}python neurax.py --api sk-sei-myperplexitykey{Colors.RESET}

{Colors.BRIGHT_WHITE}Get your API key from:{Colors.RESET} {Colors.BRIGHT_BLUE}https://www.perplexity.ai/settings/api{Colors.RESET}
""",
        '--token': f"""
{Colors.BRIGHT_CYAN}╔══════════════════════════════════════════════════════════════════════╗
║                       {Colors.BRIGHT_YELLOW}--token ARGUMENT HELP{Colors.BRIGHT_CYAN}                         ║
╚══════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.BRIGHT_WHITE}Description:{Colors.RESET}
Configure Telegram bot token for NeuraX bot functionality.

{Colors.BRIGHT_WHITE}Usage:{Colors.RESET}
{Colors.BRIGHT_GREEN}python neurax.py --token{Colors.RESET}                         # Interactive mode
{Colors.BRIGHT_GREEN}python neurax.py --token 92173:hd83bdksdn{Colors.RESET}        # Direct inline input

{Colors.BRIGHT_WHITE}Examples:{Colors.RESET}
{Colors.BRIGHT_GREEN}python neurax.py --token 1234567890:ABCdefGHIjklMNOpqrSTUvwxyz{Colors.RESET}
{Colors.BRIGHT_GREEN}python neurax.py --token 92173:hd83bdksdn{Colors.RESET}

{Colors.BRIGHT_WHITE}Get your bot token from:{Colors.RESET} {Colors.BRIGHT_BLUE}@BotFather on Telegram{Colors.RESET}
"""
    }
    
    if arg_name in help_messages:
        print(help_messages[arg_name])
    else:
        print(f"{Colors.RED}✘ No help available for argument: {arg_name}{Colors.RESET}")
'''
        
def configure_api_key_inline(config_manager: ConfigManager, api_key: str = None):
    """Configure Perplexity API key with optional inline value"""
    if api_key:
        # Direct inline configuration
        print(f"\n{Colors.BRIGHT_CYAN}🔑 Configuring Perplexity AI API Key{Colors.RESET}")
        config_manager.set_api_key(api_key.strip(), silent=True)
        print(f"{Colors.GREEN}✔ API key configured successfully!{Colors.RESET}")
    else:
        # Interactive configuration
        configure_api_key(config_manager)

def configure_telegram_token_inline(config_manager: ConfigManager, token: str = None):
    """Configure Telegram bot token with optional inline value"""
    if token:
        # Direct inline configuration
        print(f"\n{Colors.BRIGHT_CYAN}🤖 Configuring Telegram Bot Token{Colors.RESET}")
        config_manager.set_telegram_token(token.strip(), silent=True)
        print(f"{Colors.GREEN}✔ Telegram bot token configured successfully!{Colors.RESET}")
    else:
        # Interactive configuration
        configure_telegram_token(config_manager)

def main():
    """Main function with improved argument handling"""
    # Setup signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    
    try:
        config_manager = ConfigManager()
        
        # Custom argument parser to handle inline values
        parser = argparse.ArgumentParser(description='NeuraX AI Tool', add_help=False)
        parser.add_argument('--about', action='store_true', help='Show about information')
        parser.add_argument('--connect', action='store_true', help='Show contact information')
        parser.add_argument('--api', nargs='?', const=True, help='Configure Perplexity API key')
        parser.add_argument('--token', nargs='?', const=True, help='Configure Telegram bot token')
        parser.add_argument('--bot', action='store_true', help='Start Telegram bot')
        parser.add_argument('--help', action='store_true', help='Show help message')
        parser.add_argument('--config', action='store_true', help='Show current configuration')
        
        args = parser.parse_args()
        
        # Count number of arguments provided
        active_args = sum([
            bool(args.about),
            bool(args.connect),
            bool(args.api is not None),
            bool(args.token is not None),
            bool(args.bot),
            bool(args.help),
            bool(args.config)
        ])
        
        # Check if multiple arguments are used
        if active_args > 1:
            print(f"{Colors.RED}✘ Error: Only one argument should be used at a time!{Colors.RESET}\n")
            print(f"{Colors.BRIGHT_YELLOW}Examples of correct usage:{Colors.RESET}")
            print(f"{Colors.BRIGHT_GREEN}python neurax.py --about{Colors.RESET}")
            print(f"{Colors.BRIGHT_GREEN}python neurax.py --api sk-proj-yourkey{Colors.RESET}")
            print(f"{Colors.BRIGHT_GREEN}python neurax.py --token 12345:abcdef{Colors.RESET}")
            print(f"{Colors.BRIGHT_GREEN}python neurax.py --config{Colors.RESET}")
            print(f"{Colors.BRIGHT_GREEN}python neurax.py --bot{Colors.RESET}\n")
            print_help()
            return
        
        # Handle arguments
        if args.about:
            print_about()
            return
        
        if args.connect:
            print_connect()
            return
        
        if args.help:
            print_help()
            return
        
        if args.api is not None:
            if args.api is True:
                # No value provided, enter interactive mode
                configure_api_key(config_manager)
            else:
                # Value provided, configure directly
                configure_api_key_inline(config_manager, args.api)
            return
        
        if args.token is not None:
            if args.token is True:
                # No value provided, enter interactive mode
                configure_telegram_token(config_manager)
            else:
                # Value provided, configure directly
                configure_telegram_token_inline(config_manager, args.token)
            return
        
        if args.config:
            # Display current configuration with enhanced formatting
            print(f"\n{Colors.BRIGHT_CYAN}╔══════════════════════════════════════════════════════════════════════╗")
            print(f"║                         {Colors.BRIGHT_YELLOW}NEURAX CONFIGURATION{Colors.BRIGHT_CYAN}                         ║")
            print(f"╚══════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
            
            # Get configuration values
            api_key = config_manager.get_api_key()
            token = config_manager.get_telegram_token()
            
            # Display API Key
            if api_key:
                # Mask API key for security (show first 8 and last 4 chars)
                if len(api_key) > 12:
                    masked_api = api_key[:8] + "*" * (len(api_key) - 12) + api_key[-4:]
                else:
                    masked_api = api_key[:4] + "*" * (len(api_key) - 4)
                print(f"{Colors.BRIGHT_WHITE}📡 Perplexity API Key:{Colors.RESET} {Colors.GREEN}{masked_api}{Colors.RESET} {Colors.GREEN}✔ Configured{Colors.RESET}")
            else:
                print(f"{Colors.BRIGHT_WHITE}📡 Perplexity API Key:{Colors.RESET} {Colors.RED}✘ Not configured{Colors.RESET}")
            
            # Display Telegram Token
            if token:
                # Mask token for security (show first 6 chars and indicate configured)
                masked_token = token[:6] + "*" * (len(token) - 6) if len(token) > 6 else "*" * len(token)
                print(f"{Colors.BRIGHT_WHITE}🤖 Telegram Bot Token:{Colors.RESET} {Colors.GREEN}{masked_token}{Colors.RESET} {Colors.GREEN}✔ Configured{Colors.RESET}")
            else:
                print(f"{Colors.BRIGHT_WHITE}🤖 Telegram Bot Token:{Colors.RESET} {Colors.RED}✘ Not configured{Colors.RESET}")
            
            # Display configuration file location
            print(f"\n{Colors.DIM}Configuration stored in: {config_manager.config_file}{Colors.RESET}")
            return
        
        if args.bot:
            # Import and start telegram bot
            try:
                from modules.telegram_bot import start_bot
                start_bot(config_manager)
            except ImportError:
                print(f"{Colors.RED}✘ Telegram bot module not found. Please ensure modules/telegram_bot.py exists.{Colors.RESET}")
            return
        
        # If no arguments, start CLI chat mode
        clear_screen()
        print_banner()
        cli_chat_mode(config_manager)
        
    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)
    except Exception as e:
        print(f"{Colors.RED}✘ Unexpected error: {e}{Colors.RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()
