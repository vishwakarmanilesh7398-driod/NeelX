from vision.matcher import TemplateMatcher

match = TemplateMatcher.find(
    "temp/screenshots/latest.png",
    "vision/templates/settings_icon.png"
)

if match:

    print("✅ Match Found")

    print("X :", match["x"])
    print("Y :", match["y"])

    print("Width :", match["width"])
    print("Height :", match["height"])

    print("Confidence :", match["confidence"])

else:

    print("❌ Match Not Found")