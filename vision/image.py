"""
=========================================
Project : NeelX
Module  : Vision Image
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from pathlib import Path
import cv2


class VisionImage:

    @staticmethod
    def load(path: str):

        image = cv2.imread(str(path))

        if image is None:
            raise FileNotFoundError(
                f"Image not found: {path}"
            )

        return image

    @staticmethod
    def save(image, path: str):

        output = Path(path)

        output.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        cv2.imwrite(
            str(output),
            image
        )

    @staticmethod
    def width(image):

        return image.shape[1]

    @staticmethod
    def height(image):

        return image.shape[0]

    @staticmethod
    def size(image):

        return (
            image.shape[1],
            image.shape[0]
        )