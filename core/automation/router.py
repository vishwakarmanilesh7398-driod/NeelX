"""
=========================================
Project : NeelX
Module  : Automation Router
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""


class AutomationRouter:

    @staticmethod
    def route(action: str):

        text = action.lower().strip()

        # Android / device commands
        if any(word in text for word in [
            "open",
            "close",
            "home",
            "back",
            "screenshot"
        ]):
            return "command"

        # Calculator
        if any(word in text for word in [
            "calculate",
            "plus",
            "minus",
            "multiply",
            "divide"
        ]):
            return "brain"

        # Search
        if any(word in text for word in [
            "search",
            "google",
            "find"
        ]):
            return "brain"

        # Normal conversation
        return "brain"