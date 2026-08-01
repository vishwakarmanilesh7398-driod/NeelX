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

    @staticmethod
    def speak(text: str):

        print(f"🤖 {text}")

        engine = pyttsx3.init()

        engine.setProperty("rate", 170)

        engine.say(text)

        engine.runAndWait()

        engine.stop()

        del engine