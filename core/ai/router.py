"""
=========================================
Project : NeelX
Module  : AI Router
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""


class AIRouter:

    @staticmethod
    def route(text: str):

        text = text.lower().strip()

        # -------------------------
        # Calculator
        # -------------------------

        if any(word in text for word in [
            "calculate",
            "plus",
            "minus",
            "multiply",
            "divide",
            "+",
            "-",
            "*",
            "/"
        ]):
            return "calculator"

        # -------------------------
        # Search
        # -------------------------

        if any(word in text for word in [
            "search",
            "google",
            "find"
        ]):
            return "search"

        # -------------------------
        # Time
        # -------------------------

        if any(word in text for word in [
            "time",
            "what time",
            "current time"
        ]):
            return "time"

        # -------------------------
        # Date
        # -------------------------

        if any(word in text for word in [
            "date",
            "today",
            "today's date",
            "what is today's date"
        ]):
            return "date"

        # -------------------------
        # Default
        # -------------------------

        return "chat"