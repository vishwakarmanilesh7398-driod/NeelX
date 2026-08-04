
"""
=========================================
Project : NeelX
Module  : App Manager
Author  : Nilesh Vishwakarma
Version : 1.2.0
=========================================
"""

from urllib.parse import quote_plus

from android.adb import ADB


class AppManager:

    @staticmethod
    def open(package_name: str):

        try:

            # Fast & works with most Android apps
            output = ADB.shell(
                f"monkey -p {package_name} "
                f"-c android.intent.category.LAUNCHER 1"
            )

            print(output)

        except Exception:

            # Fallback
            output = ADB.shell(
                f"am start -n {package_name}/.Main"
            )

            print(output)

    @staticmethod
    def close(package_name: str):

        ADB.shell(
            f"am force-stop {package_name}"
        )

    @staticmethod
    def search_youtube(query: str):

        from urllib.parse import quote_plus

        encoded_query = quote_plus(query)

        print(f"🎬 YouTube Search: {query}")

        # Open YouTube search directly
        ADB.shell(
            f'am start '
            f'-a android.intent.action.SEARCH '
            f'-p com.google.android.youtube '
            f'--es query "{encoded_query}"'
        )



    @staticmethod
    def is_installed(package_name: str) -> bool:

        result = ADB.shell(
            f"pm list packages {package_name}"
        )

        return package_name in result

    @staticmethod
    def list_packages():

        result = ADB.shell(
            "pm list packages"
        )

        return result.splitlines()

