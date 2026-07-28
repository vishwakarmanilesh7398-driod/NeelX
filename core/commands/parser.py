"""
=========================================
Project : NeelX
Module  : Command Parser
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from core.commands.command import Command


class CommandParser:

    @staticmethod
    def parse(text: str) -> Command:

        text = text.lower().strip()

        parts = text.split(maxsplit=1)

        if len(parts) == 1:
            return Command(parts[0])

        return Command(
            action=parts[0],
            target=parts[1]
        )