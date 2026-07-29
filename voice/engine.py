"""
=========================================
Project : NeelX
Module  : Voice Engine
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from voice.listener import VoiceListener
from voice.speaker import Speaker

from neelx.api import NeelX
from core.intent.nlp import NLP


class VoiceEngine:

    @staticmethod
    def run():

        Speaker.speak("Listening")

        text = VoiceListener.listen()

        if not text:
            Speaker.speak("I did not hear anything.")
            return

        print(f"\n📝 Recognized : {text}")

        intent = NLP.understand(text)

        if intent.action == "open":
            Speaker.speak(f"Opening {intent.target}")

        elif intent.action == "close":
            Speaker.speak(f"Closing {intent.target}")

        elif intent.action == "home":
            Speaker.speak("Going Home")

        elif intent.action == "back":
            Speaker.speak("Going Back")

        elif intent.action == "screenshot":
            Speaker.speak("Capturing Screenshot")

        NeelX.execute(text)

        Speaker.speak("Command Executed")