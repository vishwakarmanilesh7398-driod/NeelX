"""
=========================================
Project : NeelX
Module  : App Resolver
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""


class AppResolver:

    APPS = {

        "com.google.android.youtube": "YouTube",
        "com.android.settings": "Settings",
        "com.instagram.android": "Instagram",
        "com.whatsapp": "WhatsApp",
        "com.google.android.apps.chrome": "Chrome",
        "com.android.chrome": "Chrome",
        "com.facebook.katana": "Facebook",
        "com.google.android.gm": "Gmail",
        "com.google.android.apps.maps": "Google Maps",
        "com.google.android.googlequicksearchbox": "Google",
    }

    @classmethod
    def resolve(cls, package: str):

        if not package:
            return "Unknown"

        return cls.APPS.get(
            package,
            package
        )

