from core.nlp.fuzzy import Fuzzy

apps = [
    "whatsapp",
    "youtube",
    "settings",
    "chrome"
]

tests = [
    "whats app",
    "youtubee",
    "setting",
    "chrom",
    "watsapp"
]

for text in tests:

    print(text, "->", Fuzzy.match(text, apps))