#!/usr/bin/env python3
"""
Configuration Manager Module for NeuraX AI Tool
Author: Alex Butler [Vritra Security Organization]
Version: 1.0.0
NeuraX is prepared with well-structured comments by Alex for future contributors.
"""

import json
import signal
import sys
from pathlib import Path
from typing import Optional, Dict
from .colors import Colors

class ConfigManager:
    """Manages configuration for the NeuraX AI tool"""
    
    def __init__(self, tool_name: str = "neurax"):
        self.tool_name = tool_name
        self.config_dir = Path.home() / f".config-{tool_name}"
        self.config_file = self.config_dir / "config.json"
        self.ensure_config_dir()
    
    def ensure_config_dir(self):
        """Ensure config directory exists"""
        self.config_dir.mkdir(exist_ok=True)
    
    def load_config(self) -> Dict:
        """Load configuration from file"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"{Colors.RED}✘ Error loading config: {e}{Colors.RESET}")
                return {}
        return {}
    
    def save_config(self, config: Dict, silent: bool = False):
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=2)
            if not silent:
                print(f"{Colors.GREEN}✔ Configuration saved successfully{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.RED}✘ Error saving config: {e}{Colors.RESET}")
    
    def get_api_key(self) -> Optional[str]:
        """Get Perplexity API key"""
        config = self.load_config()
        return config.get('perplexity_api_key')
    
    def set_api_key(self, api_key: str, silent: bool = False):
        """Set Perplexity API key"""
        config = self.load_config()
        config['perplexity_api_key'] = api_key
        self.save_config(config, silent)
    
    def get_telegram_token(self) -> Optional[str]:
        """Get Telegram bot token"""
        config = self.load_config()
        return config.get('telegram_bot_token')
    
    def set_telegram_token(self, token: str, silent: bool = False):
        """Set Telegram bot token"""
        config = self.load_config()
        config['telegram_bot_token'] = token
        self.save_config(config, silent)
