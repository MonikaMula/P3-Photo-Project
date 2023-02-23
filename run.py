from PIL import Image

# First Step - Insert Picture or will be done automatically 
a = input("Insert Photo, photo path You wish to Edit \n Isert/Paste Here:  ")
try:
    image = Image.open(a)
except:
    image = Image.open('Maxi.jpg')
print("Picture wasn't insert, automatic upload pictire as an example")

# 180 Image 🙃
image = Image.open('Maxi.jpg')
image_rotate = image.rotate(180)
image_rotate.show()

image_transpose = image.transpose
image_transpose.show()

image_rotate = image.rotate(90)
image_rotate.show()