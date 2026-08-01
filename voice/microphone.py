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

    _recognizer = sr.Recognizer()
    _microphone = sr.Microphone()

    @classmethod
    def create(cls):

        cls._recognizer.pause_threshold = 0.8
        cls._recognizer.energy_threshold = 300
        cls._recognizer.dynamic_energy_threshold = True

        return cls._recognizer, cls._microphone