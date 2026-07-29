"""
=========================================
Project : NeelX
Module  : Wake Word
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from voice.listener import VoiceListener


class WakeWord:

    WORDS = [
        "hey bro",
        "hi bro",
        "hello bro",
        "bro"
    ]

    @classmethod
    def detect(cls):

        print("\n💤 Waiting for Wake Word...")

        text = VoiceListener.listen()

        if not text:
            return False

        text = text.lower().strip()

        return text in cls.WORDS