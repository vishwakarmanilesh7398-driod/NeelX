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

            print("DEBUG: Waiting...")

            detected = WakeWord.detect()

            print(f"DEBUG: detected = {detected}")

            if detected:

                print("DEBUG: Wake Word Found")

                Speaker.speak("Yes bro.")

                print("DEBUG: Starting VoiceEngine")

                try:

                    VoiceEngine.run()

                    print("DEBUG: VoiceEngine Finished")

                except Exception as error:

                    print(error)

                    Speaker.speak("Sorry bro.")