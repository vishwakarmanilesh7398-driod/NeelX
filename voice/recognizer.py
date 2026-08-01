"""
=========================================
Project : NeelX
Module  : Voice Recognizer
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

import speech_recognition as sr
from voice.microphone import Microphone


class VoiceRecognizer:

    @staticmethod
    def listen():

        recognizer, microphone = Microphone.create()

        try:

            with microphone as source:

                print("🎤 Listening...")

                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=6
                )

            print("🧠 Recognizing...")

            text = recognizer.recognize_google(audio)

            print(f"You said: {text}")

            return text.lower().strip()

        except sr.WaitTimeoutError:

            print("⌛ Timeout")
            return ""

        except sr.UnknownValueError:

            print("❌ Could not understand")
            return ""

        except Exception as e:

            print(e)
            return ""