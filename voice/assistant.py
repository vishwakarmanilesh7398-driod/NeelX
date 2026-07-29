"""
=========================================
Project : NeelX
Module  : Voice Assistant
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from voice.wakeword import WakeWord
from voice.engine import VoiceEngine
from voice.speaker import Speaker


class Assistant:

    @staticmethod
    def start():

        print("\n🤖 NeelX Assistant Started")
        Speaker.speak("I'm ready, bro.")

        while True:

            detected = WakeWord.detect()

            if detected:

                Speaker.speak("Yes bro.")

                try:
                    VoiceEngine.run()

                except Exception as error:

                    print(f"❌ {error}")

                    Speaker.speak("Sorry bro. Something went wrong.")