#!/usr/bin/env python3
"""
Perplexity AI Client Module for NeuraX AI Tool
Author: Alex Butler [Vritra Security Organization]
Version: 1.0.0
NeuraX is prepared with well-structured comments by Alex for future contributors.
"""

import requests
import signal
import sys
from typing import Optional
from .colors import Colors

class PerplexityAI:
    """Perplexity AI API client"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_url = "https://api.perplexity.ai/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        self.chat_history = [
            {"role": "system", "content": "Be precise and concise."}
        ]
    
    def send_message(self, message: str, use_history: bool = True) -> Optional[str]:
        """Send message to Perplexity AI and get response"""
        try:
            if use_history:
                self.chat_history.append({"role": "user", "content": message})
                messages = self.chat_history
            else:
                messages = [
                    {"role": "system", "content": "Be precise and concise."},
                    {"role": "user", "content": message}
                ]
            
            payload = {
                "model": "sonar",
                "messages": messages
            }
            
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            response.raise_for_status()
            
            data = response.json()
            ai_reply = data["choices"][0]["message"]["content"]
            
            if use_history:
                self.chat_history.append({"role": "assistant", "content": ai_reply})
            
            return ai_reply
            
        except requests.exceptions.RequestException as e:
            print(f"{Colors.RED}✘ Network Error: {e}{Colors.RESET}")
            return None
        except KeyError as e:
            print(f"{Colors.RED}✘ API Response Error: {e}{Colors.RESET}")
            return None
        except Exception as e:
            print(f"{Colors.RED}✘ Unexpected Error: {e}{Colors.RESET}")
            return None
    
    def reset_conversation(self):
        """Reset chat history"""
        self.chat_history = [
            {"role": "system", "content": "Be precise and concise."}
        ]
