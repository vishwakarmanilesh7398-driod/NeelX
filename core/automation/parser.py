"""
=========================================
Project : NeelX
Module  : Automation Parser
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""


class AutomationParser:

    SEPARATORS = [
        " and ",
        " then ",
        " after that ",
    ]

    @classmethod
    def parse(cls, text: str):

        text = text.lower().strip()

        actions = [text]

        for separator in cls.SEPARATORS:

            new_actions = []

            for action in actions:

                parts = action.split(separator)

                for part in parts:

                    part = part.strip()

                    if part:
                        new_actions.append(part)

            actions = new_actions

        return actions