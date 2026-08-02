"""
=========================================
Project : NeelX
Module  : Package Manager
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from android.adb import ADB


class PackageManager:

    @staticmethod
    def list_packages():

        output = ADB.shell(
            "pm list packages"
        )

        packages = []

        for line in output.splitlines():

            line = line.strip()

            if line.startswith("package:"):

                packages.append(
                    line.replace("package:", "")
                )

        return packages