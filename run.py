from PIL import Image, ImageColor, ImageOps
from urllib import request

# First Step - Insert Picture or will be done automatically
url = input("Insert Photo, photo path You wish to Edit \n Insert/Paste Here: ")
try:
    request.urlretrieve(url, "Rework.png")
    image = Image.open("Rework.png")
    print("Picture was insert")
    image_uploaded = True
except:
    url_test = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/"\
               "Python_logo_and_wordmark.svg/"\
               "2560px-Python_logo_and_wordmark.svg.png"
    request.urlretrieve(url_test, "Rework.png")
    image = Image.open("Rework.png")
    print("Picture was insert")
    image_uploaded = True
    print("Picture wasn't insert, automatic upload picture as an example")

# Image Rotation
rotation = input('Would You Like Rotate An Image \n Yes/No: ')
if rotation.lower().startswith("y"):
  rotation_number = input(
      'What degree You wish picture to rotate? \n Place degree number: ')
  try:
      image_rotate = image.rotate(int(rotation_number))
      image_rotate.show()
      image = image_rotate
  except:
      print("Go forward if You do not wish rotate an Image")

# Grey Color
grayscale = input("Would You like change picture to grey: \n Yes/No: ")
if grayscale.lower().startswith("y"):
  image = ImageOps.grayscale(image)
  image.show()

# Image_Cropping 
cropping = input('Crop image? \n Yes/No: ')
if cropping.lower().startswith("y"):
    print(f"image size is: {image.size} ")
    left_x = input("left: ")
    top_y = input("top: ")
    right_x = input("right: ")
    bottom_y = input("bottom: ")
    
try:
    width, height = image.size
    left = int(left_x)
    top = int(top_y)
    right = width - int(right_x)
    bottom = height - int(bottom_y)
    image_crop = image.crop((left, top, right, bottom))
    image_crop.show()
    image = image_crop
except:
    print("Wrong Input")
    
# Saving Image
saving_mode = input("Would You like to save Your picture? \n Yes/No: ")
if saving_mode.lower().startswith("y"):
    save_path = input("Insert path where You wish to save picture: \n ")
    if save_path:
          image.save(f"{save_path}")    