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

        with microphone as source:

            print("🎤 Listening...")

            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(source)

        print("🧠 Recognizing...")

        try:

            text = recognizer.recognize_google(audio)

            print(f"You said: {text}")

            return text

        except sr.UnknownValueError:

            print("❌ Could not understand audio")

            return ""

        except sr.RequestError as e:

            print(f"❌ Speech Recognition Error: {e}")

            return ""