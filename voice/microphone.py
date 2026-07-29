"""
=========================================
Project : NeelX
Module  : Microphone
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

import speech_recognition as sr


class Microphone:

    @staticmethod
    def create():

        recognizer = sr.Recognizer()

        microphone = sr.Microphone()

        return recognizer, microphone