from vision.matcher import TemplateMatcher
from android.controller import AndroidController

match = TemplateMatcher.find(
    "temp/screenshots/latest.png",
    "vision/templates/settings_icon.png"
)

if match:

    x = match["x"] + match["width"] // 2
    y = match["y"] + match["height"] // 2

    print("Found :", x, y)

    AndroidController.tap(x, y)

    print("✅ Settings Opened")

else:

    print("❌ Settings Icon Not Found")