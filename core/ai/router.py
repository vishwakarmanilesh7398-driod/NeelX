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

        if (
            "time" in text
              or "what time" in text
              or "current time" in text
         ):
        return "time"

        if (
            "date" in text
              or "today" in text
              or "what is today's date" in text
         ):
         return "date"