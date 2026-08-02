"""
=========================================
Project : NeelX
Module  : Fuzzy Matcher
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from difflib import SequenceMatcher


class Fuzzy:

    @staticmethod
    def match(text: str, choices: list[str], threshold=0.65):

        text = text.lower()

        best = None
        score = 0

        for item in choices:

            ratio = SequenceMatcher(
                None,
                text,
                item.lower()
            ).ratio()

            if ratio > score:
                score = ratio
                best = item

        if score >= threshold:
            return best

        return None