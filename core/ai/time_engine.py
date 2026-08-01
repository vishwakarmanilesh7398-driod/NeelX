"""
=========================================
Project : NeelX
Module  : Time Engine
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from datetime import datetime


class TimeEngine:

    @staticmethod
    def now():

        return datetime.now().strftime("%I:%M %p")