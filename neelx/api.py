"""
=========================================
Project : NeelX
Module  : Public API
Author  : Nilesh Vishwakarma
Version : 1.1.0
=========================================
"""

from core.intent.nlp import NLP
from core.commands.executor import CommandExecutor
from core.commands.command import Command


class NeelX:

    @staticmethod
    def execute(text: str):

        print(f"\n📝 Input : {text}")

        intent = NLP.understand(text)

        print(f"🧠 Intent : {intent}")

        command = Command(
            action=intent.action,
            target=intent.target
        )

        print(f"⚙️ Command : {command}")

        result = CommandExecutor.execute(command)

        print("✅ Command Executed")

        return result