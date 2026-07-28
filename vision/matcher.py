"""
=========================================
Project : NeelX
Module  : Template Matcher
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from pathlib import Path
import cv2

from vision.image import VisionImage


class TemplateMatcher:

    @staticmethod
    def find(screen_path: str, template_path: str, threshold: float = 0.90):

        screen = VisionImage.load(screen_path)
        template = VisionImage.load(template_path)

        result = cv2.matchTemplate(
            screen,
            template,
            cv2.TM_CCOEFF_NORMED
        )

        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val < threshold:
            return None

        h, w = template.shape[:2]

        return {
            "x": max_loc[0],
            "y": max_loc[1],
            "width": w,
            "height": h,
            "confidence": round(max_val, 3)
        }