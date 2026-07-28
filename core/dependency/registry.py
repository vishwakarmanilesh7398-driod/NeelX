"""
=========================================
Project : NeelX
Module  : Dependency Registry
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from core.dependency.dependency import Dependency


DEPENDENCIES = [

    Dependency(
        name="NumPy",
        package="numpy"
    ),

    Dependency(
        name="OpenCV",
        package="cv2"
    ),

    Dependency(
        name="ADB",
        package="adb"
    ),

    Dependency(
        name="Pillow",
        package="PIL"
    ),

    Dependency(
        name="Requests",
        package="requests"
    )

]