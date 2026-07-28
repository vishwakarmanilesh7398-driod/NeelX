"""
=========================================
Project : NeelX
Module  : Command Executor
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from core.commands.command import Command
from core.apps.manager import Apps
from android.api import Android


class CommandExecutor:

    @staticmethod
    def execute(command: Command):

        action = command.action
        target = command.target

        # -------------------------
        # Apps
        # -------------------------

        if action == "open":
            Apps.open(target)
            return True

        if action == "close":
            Apps.close(target)
            return True

        # -------------------------
        # Navigation
        # -------------------------

        if action == "home":
            Android.home()
            return True

        if action == "back":
            Android.back()
            return True

        if action == "recent":
            Android.recent()
            return True

        raise ValueError(f"Unknown command: {action}")