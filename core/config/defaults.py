"""
=========================================
Project : NeelX
Module  : Default Configuration
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

DEFAULT_SETTINGS = {
    "application": {
        "name": "NeelX",
        "version": "1.0.0",
        "developer_mode": False
    },

    "appearance": {
        "theme": "dark",
        "language": "en"
    },

    "logging": {
        "level": "INFO"
    },

    "window": {
        "width": 1280,
        "height": 720,
        "fullscreen": False
    },

    "android": {
        "adb_path": "",
        "auto_connect": True
    },

    "vision": {
        "camera_index": 0,
        "ocr_enabled": True
    },

    "voice": {
        "wake_word": "Neel",
        "microphone": 0
    },

    "automation": {
        "enabled": True,
        "delay": 0.5
    }
}