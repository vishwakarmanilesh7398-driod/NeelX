"""
=========================================
Project : NeelX
Module  : Vision Actions
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from vision.matcher import TemplateMatcher
from android.controller import AndroidController


class VisionActions:

    @staticmethod
    def click(template_path: str, screen_path="temp/screenshots/latest.png"):

        match = TemplateMatcher.find(
            screen_path,
            template_path
        )

        if match is None:
            return False

        x = match["x"] + match["width"] // 2
        y = match["y"] + match["height"] // 2

        AndroidController.tap(x, y)

        return True