"""
=========================================
Project : NeelX
Module  : Public API
Author  : Nilesh Vishwakarma
Version : 1.1.0
=========================================
"""

from core.intent.intent import Intent
from core.commands.command import Command
from core.commands.executor import CommandExecutor
from core.intent.nlp import NLP


class NeelX:

    @staticmethod
    def execute(text: str):

        intent = NLP.understand(text)

        return NeelX.execute_intent(intent)

    @staticmethod
    def execute_intent(intent: Intent):

        command = Command(
            action=intent.action,
            target=intent.target
        )

        return CommandExecutor.execute(command)