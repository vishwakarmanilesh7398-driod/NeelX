"""
=========================================
Project : NeelX
Module  : Intent Matcher
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from core.intent.intent import Intent


class IntentMatcher:

    ACTIONS = {
        "open": ["open", "launch", "start", "run"],
        "close": ["close", "exit", "quit", "stop"],
        "home": ["home", "homepage"],
        "back": ["back", "return"],
        "screenshot": ["screenshot", "capture"],
    }

    @classmethod
    def match(cls, text: str) -> Intent:

        text = text.lower().strip()

        # Special phrases
        if text == "go home":
            return Intent("home")

        if text == "go back":
            return Intent("back")

        if text == "take screenshot":
            return Intent("screenshot")

        words = text.split()

        if not words:
            return Intent("", "")

        action = words[0]
        target = " ".join(words[1:])

        for intent, keywords in cls.ACTIONS.items():
            if action in keywords:
                return Intent(intent, target)

        return Intent(action, target)