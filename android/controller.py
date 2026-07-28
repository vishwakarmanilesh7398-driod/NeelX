"""
=========================================
Project : NeelX
Module  : Android Controller
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from android.adb import ADB


class AndroidController:

    @staticmethod
    def tap(x: int, y: int):

        ADB.shell(
            f"input tap {x} {y}"
        )

    @staticmethod
    def swipe(
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        duration: int = 300
    ):

        ADB.shell(
            f"input swipe {x1} {y1} {x2} {y2} {duration}"
        )

    @staticmethod
    def input_text(text: str):

        text = text.replace(" ", "%s")

        ADB.shell(
            f'input text "{text}"'
        )

    @staticmethod
    def home():

        ADB.shell(
            "input keyevent 3"
        )

    @staticmethod
    def back():

        ADB.shell(
            "input keyevent 4"
        )

    @staticmethod
    def recent():

        ADB.shell(
            "input keyevent 187"
        )

    @staticmethod
    def power():

        ADB.shell(
            "input keyevent 26"
        )

    @staticmethod
    def volume_up():

        ADB.shell(
            "input keyevent 24"
        )

    @staticmethod
    def volume_down():

        ADB.shell(
            "input keyevent 25"
        )