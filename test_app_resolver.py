from vision.app_resolver import AppResolver


tests = [
    "com.google.android.youtube",
    "com.android.settings",
    "com.instagram.android",
    "com.whatsapp",
]


for package in tests:

    name = AppResolver.resolve(package)

    print(
        f"{package} -> {name}"
    )

