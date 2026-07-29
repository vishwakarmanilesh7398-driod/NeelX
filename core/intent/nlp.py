"""
=========================================
Project : NeelX
Module  : Natural Language Engine
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from core.intent.engine import IntentEngine


class NLP:

    IGNORE_WORDS = {

        "please",
        "can",
        "could",
        "you",
        "me",
        "the",
        "a",
        "an",
        "to",
        "my"

    }

    @classmethod
    def understand(cls, text: str):

        words = text.lower().split()

        filtered = []

        for word in words:

            if word not in cls.IGNORE_WORDS:
                filtered.append(word)

        clean_text = " ".join(filtered)

        return IntentEngine.understand(clean_text)