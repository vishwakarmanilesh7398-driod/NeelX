from core.automation.router import AutomationRouter


tests = [
    "open youtube",
    "open settings",
    "go home",
    "go back",
    "take screenshot",
    "calculate 25 plus 75",
    "search free fire",
    "how are you"
]


for text in tests:

    result = AutomationRouter.route(text)

    print(f"{text} -> {result}")