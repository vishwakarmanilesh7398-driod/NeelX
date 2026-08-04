from core.automation.parser import AutomationParser


tests = [
    "open youtube and open settings",
    "open chrome then open youtube",
    "open instagram after that open youtube"
]


for text in tests:

    print(f"\nInput : {text}")

    actions = AutomationParser.parse(text)

    for index, action in enumerate(actions, start=1):

        print(f"{index}. {action}")