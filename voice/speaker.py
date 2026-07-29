"""
=========================================
Project : NeelX
Module  : Speaker
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

import pyttsx3


class Speaker:

    _engine = pyttsx3.init()

    @classmethod
    def speak(cls, text: str):

        print(f"🤖 {text}")

        cls._engine.say(text)
        cls._engine.runAndWait()