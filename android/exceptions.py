"""
=========================================
Project : NeelX
Module  : Android Exceptions
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""


class AndroidError(Exception):
    """Base Android Exception."""
    pass


class ADBNotFoundError(AndroidError):
    """ADB executable not found."""
    pass


class DeviceNotFoundError(AndroidError):
    """No Android device connected."""
    pass


class CommandExecutionError(AndroidError):
    """ADB command execution failed."""
    pass