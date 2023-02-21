from PIL import Image

image = Image.open('Maxi.jpg')
image.show()

# 180 Image rotate Image up side down 🙃
image = Image.open('Maxi.jpg')
image_rotate = image.rotate(180)
image_rotate.show()