from vision.image import VisionImage

image = VisionImage.load(
    "temp/screenshots/latest.png"
)

print("Width :", VisionImage.width(image))

print("Height :", VisionImage.height(image))

print("Size :", VisionImage.size(image))