"""
=========================================
Project : NeelX
Module  : Command Executor
Author  : Nilesh Vishwakarma
Version : 1.1.0
=========================================
"""

from core.commands.command import Command
from core.apps.manager import Apps
from android.api import Android
from android.screenshot import Screenshot


class CommandExecutor:

    @staticmethod
    def execute(command: Command):

        action = command.action
        target = command.target

        # Debug
        print(f"🚀 Executing : {action} {target}")

        # -------------------------
        # Apps
        # -------------------------

        if action == "open":
            print(f"📱 Opening : {target}")
            Apps.open(target)
            return True

        if action == "close":
            print(f"📱 Closing : {target}")
            Apps.close(target)
            return True

        # -------------------------
        # Navigation
        # -------------------------

        if action == "home":
            print("🏠 Going Home")
            Android.home()
            return True

        if action == "back":
            print("⬅️ Going Back")
            Android.back()
            return True

        if action == "recent":
            print("📋 Opening Recent Apps")
            Android.recent()
            return True

        # -------------------------
        # Screenshot
        # -------------------------

        if action == "screenshot":

            image = Screenshot.capture()

            print(f"📸 Screenshot Saved : {image}")

            return image

        raise ValueError(f"Unknown command: {action}")