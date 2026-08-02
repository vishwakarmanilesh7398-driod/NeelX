"""
=========================================
Project : NeelX
Module  : Launcher Scanner
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from android.adb import ADB


class Launcher:

    @staticmethod
    def list():

        output = ADB.shell(
            "cmd package query-activities "
            "-a android.intent.action.MAIN "
            "-c android.intent.category.LAUNCHER"
        )

        return output