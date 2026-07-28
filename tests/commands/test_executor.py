"""
=========================================
Project : NeelX
Module  : Command Executor Test
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

import time

from core.commands.parser import CommandParser
from core.commands.executor import CommandExecutor


def run(command_text):

    print(f"\n> {command_text}")

    command = CommandParser.parse(command_text)

    CommandExecutor.execute(command)


run("open settings")

time.sleep(4)

run("home")

time.sleep(2)

run("open chrome")

time.sleep(4)

run("back")

print("\n✅ All Commands Executed")