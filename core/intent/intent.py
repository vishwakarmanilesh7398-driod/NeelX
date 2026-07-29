"""
=========================================
Project : NeelX
Module  : Intent Model
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""


class Intent:

    def __init__(self, action: str, target: str = ""):

        self.action = action.lower().strip()
        self.target = target.lower().strip()

    def __repr__(self):

        return f"Intent(action='{self.action}', target='{self.target}')"