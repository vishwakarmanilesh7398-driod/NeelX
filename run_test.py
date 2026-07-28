"""
=========================================
Project : NeelX
Module  : Test Runner
Author  : Nilesh Vishwakarma
Version : 1.1.0
=========================================
"""

import os
import sys


ROOT = os.path.dirname(os.path.abspath(__file__))

# Project root ko PYTHONPATH me add karo
os.environ["PYTHONPATH"] = ROOT


def run(test_file):
    os.system(f'"{sys.executable}" "{test_file}"')


def main():

    while True:

        print("\n========== NeelX Test Runner ==========")
        print("1. Android Tests")
        print("2. Vision Tests")
        print("3. Command Tests")
        print("4. Exit")

        choice = input("\nSelect Option : ")

        if choice == "1":
            run("tests/android/test_api.py")

        elif choice == "2":
            run("tests/vision/test_matcher.py")

        elif choice == "3":
            run("tests/commands/test_executor.py")

        elif choice == "4":
            print("\nBye Bro ❤️")
            break

        else:
            print("\nInvalid Option")


if __name__ == "__main__":
    main()