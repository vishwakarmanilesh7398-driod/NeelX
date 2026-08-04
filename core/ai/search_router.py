"""
=========================================
Project : NeelX
Module  : Search Router
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""


class SearchRouter:

    @staticmethod
    def route(text: str):

        text = text.lower().strip()

        if "youtube" in text:
            return "youtube"

        if "google" in text:
            return "google"

        if "chrome" in text:
            return "chrome"

        return "google"