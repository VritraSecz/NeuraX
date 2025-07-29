#!/usr/bin/env python3
"""
Colors Module for NeuraX AI Tool
Author: Alex Butler [Vritra Security Organization]
Version: 1.0.0
NeuraX is prepared with well-structured comments by Alex for future contributors.
"""

class Colors:
    """ANSI color codes for terminal output"""
    
    # Reset
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    
    # Text colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright colors
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

def print_banner():
    """Print colorful NeuraX banner"""
    banner = f"""
{Colors.BRIGHT_CYAN}╔═════════════════════════════════════════════════════════════════════╗
║                                                                    ╔╝
║         {Colors.BRIGHT_MAGENTA}███    ██ ███████ ██    ██ ██████   █████  ██   ██{Colors.BRIGHT_CYAN}         ║
║         {Colors.BRIGHT_MAGENTA}████   ██ ██      ██    ██ ██   ██ ██   ██  ██ ██{Colors.BRIGHT_CYAN}          ║
║         {Colors.BRIGHT_MAGENTA}██ ██  ██ █████   ██    ██ ██████  ███████   ███{Colors.BRIGHT_CYAN}           ║
║         {Colors.BRIGHT_MAGENTA}██  ██ ██ ██      ██    ██ ██   ██ ██   ██  ██ ██{Colors.BRIGHT_CYAN}          ║
║         {Colors.BRIGHT_MAGENTA}██   ████ ███████  ██████  ██   ██ ██   ██ ██   ██{Colors.BRIGHT_CYAN}         ║
║                                                                    ║
║                    {Colors.BRIGHT_YELLOW}🧠 AI-Powered Assistant Tool 🧠{Colors.BRIGHT_CYAN}                 ╚╗
║                                                                     ║
║            {Colors.BRIGHT_GREEN}CLI Mode & Telegram Bot Integration Available{Colors.BRIGHT_CYAN}            ║
║    {Colors.BRIGHT_WHITE}Version 1.0.0 - By Alex Butler [Vritra Security Organization]{Colors.BRIGHT_CYAN}    ║
║                                                                     ║
╚═════════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(banner)
