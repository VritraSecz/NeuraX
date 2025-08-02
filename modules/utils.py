#!/usr/bin/env python3
"""
Utilities Module for NeuraX AI Tool
Author: Alex Butler [Vritra Security Organization]
Version: 1.0.0
NeuraX is prepared with well-structured comments by Alex for future contributors.
"""

import os
import getpass
import signal
import sys
from .colors import Colors, print_banner

def setup_signal_handler():
    """Setup signal handler for Ctrl+C"""
    def signal_handler(sig, frame):
        print(f"\n{Colors.BRIGHT_YELLOW}🛑 NeuraX interrupted safely. Goodbye!{Colors.RESET}")
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_input_with_prompt(prompt: str, is_password: bool = False) -> str:
    """Get input with colorful prompt"""
    if is_password:
        return getpass.getpass(f"{Colors.BRIGHT_YELLOW}{prompt}{Colors.RESET}")
    else:
        return input(f"{Colors.BRIGHT_YELLOW}{prompt}{Colors.RESET}")

def print_about():
    """Print about information with banner"""
    print_banner()
    about_text = f"""
{Colors.BRIGHT_CYAN}╔═════════════════════════════════════════════════════════════════════╗
║                           {Colors.BRIGHT_YELLOW}ABOUT NEURAX{Colors.BRIGHT_CYAN}                              ║
╠═════════════════════════════════════════════════════════════════════╣
║                                                                     ║
║  {Colors.BRIGHT_WHITE}Tool Name:{Colors.RESET} {Colors.BRIGHT_GREEN}NeuraX AI Assistant{Colors.BRIGHT_CYAN}                                     ║
║  {Colors.BRIGHT_WHITE}Version:{Colors.RESET} {Colors.BRIGHT_GREEN}1.0.0{Colors.BRIGHT_CYAN}                                                    ╔╝
║  {Colors.BRIGHT_WHITE}Developer:{Colors.RESET} {Colors.BRIGHT_GREEN}Alex Butler [Vritra Security Organization]{Colors.BRIGHT_CYAN}             ║
║  {Colors.BRIGHT_WHITE}Created:{Colors.RESET} {Colors.BRIGHT_GREEN}2025{Colors.BRIGHT_CYAN}                                                     ║
║                                                                    ║
║  {Colors.BRIGHT_WHITE}Description:{Colors.BRIGHT_CYAN}                                                      ║
║  A powerful dual-mode AI assistant that integrates with            ║
║  Perplexity AI. Features both CLI chat interface and               ║
║  Telegram bot functionality for seamless AI interactions.          ║
║                                                                    ║
║  {Colors.BRIGHT_WHITE}Features:{Colors.BRIGHT_CYAN}                                                         ║
║  • Interactive CLI chat with colorful output                       ║
║  • Telegram bot integration                                        ║
║  • Persistent configuration management                             ║
║  • Easy API and bot token configuration                            ║
║  • Chat history support                                            ║
║  • Cross-platform compatibility                                    ║
║  • Professional modular architecture                               ║
║                                                                    ║
║  {Colors.BRIGHT_WHITE}Technologies Used:{Colors.BRIGHT_CYAN}                                                ╚╗
║  • Python 3.x                                                       ║
║  • Perplexity AI API                                                ║
║  • Telegram Bot API                                                 ║
║  • Asyncio for async operations                                     ║
║  • JSON for configuration storage                                   ║
║  • Modular architecture for maintainability                         ║
║                                                                     ║
╚═════════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(about_text)

def print_connect():
    """Print connect/contact information with banner"""
    print_banner()
    connect_text = f"""
{Colors.BRIGHT_CYAN}╔═════════════════════════════════════════════════════════════════════╗
║                         {Colors.BRIGHT_YELLOW}CONNECT WITH US{Colors.BRIGHT_CYAN}                             ║
╠═════════════════════════════════════════════════════════════════════╣
║                                                                     ║
║  {Colors.BRIGHT_WHITE}Developer:{Colors.RESET} {Colors.BRIGHT_GREEN}Alex Butler [Vritra Security Organization]{Colors.BRIGHT_CYAN}             ╔╝
║                                                                    ║
║  {Colors.BRIGHT_WHITE}🐙 GitHub:{Colors.RESET} {Colors.BRIGHT_BLUE}https://github.com/VritraSecz{Colors.BRIGHT_CYAN}                          ║
║                                                                    ║
║  {Colors.BRIGHT_WHITE}🌐 Website:{Colors.RESET} {Colors.BRIGHT_BLUE}https://vritrasec.com{Colors.BRIGHT_CYAN}                                 ║
║                                                                    ║
║  {Colors.BRIGHT_WHITE}📸 Instagram:{Colors.RESET} {Colors.BRIGHT_BLUE}https://instagram.com/haxorlex{Colors.BRIGHT_CYAN}                      ║
║                                                                    ║
║  {Colors.BRIGHT_WHITE}▶️ YouTube:{Colors.RESET} {Colors.BRIGHT_BLUE}https://youtube.com/@Technolex{Colors.BRIGHT_CYAN}                        ║
║                                                                    ║
║  {Colors.BRIGHT_WHITE}📢 Telegram (Central):{Colors.RESET} {Colors.BRIGHT_BLUE}https://t.me/LinkCentralX{Colors.BRIGHT_CYAN}                  ║
║                                                                    ║
║  {Colors.BRIGHT_WHITE}📢 Telegram (Main Channel):{Colors.RESET} {Colors.BRIGHT_BLUE}https://t.me/VritraSec{Colors.BRIGHT_CYAN}                ║
║                                                                    ║
║  {Colors.BRIGHT_WHITE}📢 Telegram (Community):{Colors.RESET} {Colors.BRIGHT_BLUE}https://t.me/VritraSecz{Colors.BRIGHT_CYAN}                  ║
║                                                                    ║
║  {Colors.BRIGHT_WHITE}💡 Support & Issues:{Colors.BRIGHT_CYAN}                                              ║
║  For bug reports, feature requests, or general support,            ║
║  please reach out through any of the above channels.               ╚╗
║                                                                     ║
║  {Colors.BRIGHT_GREEN}⭐ If you find NeuraX helpful, please consider starring           {Colors.BRIGHT_CYAN} ║
║     the repository and sharing it with others!{Colors.BRIGHT_CYAN}                      ║
║                                                                     ║
║  {Colors.BRIGHT_WHITE}🤝 Contributions Welcome:{Colors.BRIGHT_CYAN}                                          ║
║  We welcome contributions, suggestions, and feedback from           ║
║  the community to make NeuraX even better!                          ║
║                                                                     ║
╚═════════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(connect_text)

def print_help():
    """Print help information"""
    help_text = f"""
{Colors.BRIGHT_CYAN}╔═════════════════════════════════════════════════════════════════════╗
║                             {Colors.BRIGHT_YELLOW}HELP{Colors.BRIGHT_CYAN}                                    ║
╠═════════════════════════════════════════════════════════════════════╣
║                                                                     ║
║  {Colors.BRIGHT_WHITE}Usage:{Colors.RESET} {Colors.BRIGHT_GREEN}python neurax.py [OPTIONS]{Colors.BRIGHT_CYAN}                                 ╔╝
║                                                                    ║
║  {Colors.BRIGHT_WHITE}Available Options:{Colors.BRIGHT_CYAN}                                                ║
║                                                                    ║
║  {Colors.BRIGHT_GREEN}--about{Colors.BRIGHT_CYAN}       Show information about NeuraX and developer         ║
║                                                                    ║
║  {Colors.BRIGHT_GREEN}--connect{Colors.BRIGHT_CYAN}     Show developer contact and social media profiles    ║
║                                                                    ║
║  {Colors.BRIGHT_GREEN}--api{Colors.BRIGHT_CYAN}         Configure Perplexity API key (interactive/inline)   ║
║                                                                    ║
║  {Colors.BRIGHT_GREEN}--token{Colors.BRIGHT_CYAN}       Configure Telegram bot token (interactive/inline)   ║
║                                                                    ║
║  {Colors.BRIGHT_GREEN}--bot{Colors.BRIGHT_CYAN}         Start Telegram bot (requires configured token)      ║
║                                                                    ║
║  {Colors.BRIGHT_GREEN}--config{Colors.BRIGHT_CYAN}      Show current configuration status                   ║
║                                                                    ║
║  {Colors.BRIGHT_GREEN}--help{Colors.BRIGHT_CYAN}        Show this help message                              ║
║                                                                    ║
║  {Colors.BRIGHT_WHITE}No arguments:{Colors.BRIGHT_CYAN} Start interactive CLI chat mode                     ║
║                                                                    ║
║  {Colors.BRIGHT_WHITE}Configuration:{Colors.BRIGHT_CYAN}                                                    ║
║  All settings are saved in ~/.config-vritrasecz/neurax-config.json ╚╗
║  and can be used globally across sessions.                          ║
║                                                                     ║
║  {Colors.BRIGHT_WHITE}Examples:{Colors.BRIGHT_CYAN}                                                          ║
║  {Colors.BRIGHT_GREEN}python neurax.py{Colors.BRIGHT_CYAN}                         # Start CLI chat          ║
║  {Colors.BRIGHT_GREEN}python neurax.py --api{Colors.BRIGHT_CYAN}                    # Configure API key      ║
║  {Colors.BRIGHT_GREEN}python neurax.py --api sk-proj-mykey{Colors.BRIGHT_CYAN}      # Direct API config      ║
║  {Colors.BRIGHT_GREEN}python neurax.py --token 123:abc{Colors.BRIGHT_CYAN}          # Direct token config    ║
║  {Colors.BRIGHT_GREEN}python neurax.py --config{Colors.BRIGHT_CYAN}                # View configuration      ║
║  {Colors.BRIGHT_GREEN}python neurax.py --bot{Colors.BRIGHT_CYAN}                    # Start Telegram bot     ║
║  {Colors.BRIGHT_GREEN}python neurax.py --about{Colors.BRIGHT_CYAN}                  # Show about info        ║
║                                                                     ║
╚═════════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(help_text)
