"""
=========================================
Project : NeelX
Module  : Calculator
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""


class Calculator:

    @staticmethod
    def solve(text: str):

        try:

            expression = (
                text.lower()
                .replace("calculate", "")
                .replace("plus", "+")
                .replace("minus", "-")
                .replace("multiply", "*")
                .replace("into", "*")
                .replace("divide", "/")
            )

            answer = eval(expression)

            return f"The answer is {answer}"

        except Exception:

            return None