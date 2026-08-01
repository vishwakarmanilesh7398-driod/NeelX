"""
=========================================
Project : NeelX
Module  : Date Engine
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from datetime import datetime


class DateEngine:

    @staticmethod
    def today():

        return datetime.now().strftime("%d %B %Y")