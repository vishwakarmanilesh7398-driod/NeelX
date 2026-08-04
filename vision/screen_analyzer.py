"""
=========================================
Project : NeelX
Module  : Screen Analyzer
Author  : Nilesh Vishwakarma
Version : 1.1.0
=========================================
"""

import re

from android.adb import ADB
from android.screen import Screen


class ScreenAnalyzer:

    @staticmethod
    def capture():

        print("👁️ Capturing current screen...")

        return Screen.screenshot(
            "data/screen_analysis.png"
        )

    @staticmethod
    def current_app():

        print("🔍 Detecting current Android app...")

        output = ADB.shell(
            "dumpsys activity activities"
        )

        package = None

        # Android foreground/resumed activity
        patterns = [
            r"mResumedActivity:.*?\s([a-zA-Z0-9._]+)/(?:[a-zA-Z0-9._$]+)",
            r"mFocusedApp:.*?\s([a-zA-Z0-9._]+)/(?:[a-zA-Z0-9._$]+)",
            r"ResumedActivity:.*?\s([a-zA-Z0-9._]+)/(?:[a-zA-Z0-9._$]+)",
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                output,
                re.MULTILINE
            )

            if match:

                package = match.group(1)
                break

        if package:

            print(f"📱 Foreground Package: {package}")

            return package

        print("❌ Could not detect foreground app")

        return None

    @staticmethod
    def analyze():

        screenshot = ScreenAnalyzer.capture()

        package = ScreenAnalyzer.current_app()

        result = {
            "screenshot": screenshot,
            "package": package
        }

        print()
        print("🧠 Screen Analysis")
        print(f"📸 Screenshot : {screenshot}")
        print(f"📱 Package    : {package}")

        return result

