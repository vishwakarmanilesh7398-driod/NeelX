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

        if any(word in text for word in [
            "search",
            "google",
            "find"
        ]):
            return "search"

        return "chat"