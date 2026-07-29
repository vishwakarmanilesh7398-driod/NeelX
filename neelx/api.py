"""
=========================================
Project : NeelX
Module  : Public API
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from core.intent.nlp import NLP
from core.commands.executor import CommandExecutor
from core.commands.command import Command


class NeelX:

    @staticmethod
    def execute(text: str):

        intent = NLP.understand(text)

        command = Command(
            action=intent.action,
            target=intent.target
        )

        return CommandExecutor.execute(command)