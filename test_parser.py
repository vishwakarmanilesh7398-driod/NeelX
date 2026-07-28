from core.commands.parser import CommandParser

command = CommandParser.parse(
    "open settings"
)

print(command)

command = CommandParser.parse(
    "close chrome"
)

print(command)

command = CommandParser.parse(
    "home"
)

print(command)