"""
=========================================
Project : NeelX
Module  : AI Brain
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from core.ai.chat import ChatEngine
from core.ai.search import Search
from core.ai.calculator import Calculator
from core.ai.router import AIRouter
from core.ai.time_engine import TimeEngine
from core.ai.date_engine import DateEngine

class Brain:

    @staticmethod
    def think(text: str):

        route = AIRouter.route(text)

        if route == "chat":
            return ChatEngine.reply(text)

        if route == "search":
            return Search.search(text)

        if route == "calculator":
            return Calculator.solve(text)

        if route == "time":
            return f"The time is {TimeEngine.now()}"

        if route == "date":
            return f"Today's date is {DateEngine.today()}"

        return None