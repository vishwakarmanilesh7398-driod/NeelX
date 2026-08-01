"""
=========================================
Project : NeelX
Module  : Chat Engine
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from core.ai.responses import RESPONSES


class ChatEngine:

    @staticmethod
    def reply(text: str):

        text = text.lower().strip()

        return RESPONSES.get(text)