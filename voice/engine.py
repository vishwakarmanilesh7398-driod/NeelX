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
from core.ai.brain import Brain


class VoiceEngine:

    @staticmethod
    def run():

        Speaker.speak("Listening")

        text = VoiceListener.listen()

        print(f"DEBUG: {text}")

        if not text:
            Speaker.speak("I did not hear anything.")
            return

        print(f"\n📝 Recognized : {text}")

        # -------------------------
        # AI Brain
        # -------------------------

        reply = Brain.think(text)

        if reply:

            Speaker.speak(reply)

            return

        # -------------------------
        # Command Processing
        # -------------------------

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

        NeelX.execute_intent(intent)

        Speaker.speak("Command Executed")