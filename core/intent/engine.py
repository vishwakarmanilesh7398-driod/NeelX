"""
=========================================
Project : NeelX
Module  : Intent Engine
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from core.intent.matcher import IntentMatcher


class IntentEngine:

    @staticmethod
    def understand(text: str):
        return IntentMatcher.match(text)