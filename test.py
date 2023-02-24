from PIL import Image, ImageColor, ImageOps

# First Step - Insert Picture or will be done automatically
a = input("Insert Photo, photo path You wish to Edit \n Insert/Paste Here:  ")
try:
    image = Image.open(a)
except:
    image = Image.open('Maxi.jpg')
    print("Picture wasn't insert, automatic upload picture as an example")

#Image_Cropping
cropping = input('Crop image? \n Yes/No: ')
if cropping.lower().startswith("y"):
  left_x = input("left: ")
  top_y = input("top: ")
  right_x = input("right: ")
  bottom_y = input("bottom: ")
  
#width, height = image.size
  try:
    left_x = int(left_x)
    top_y = int(top_y)
    right_x = int(right_x)
    bottom_y = int(bottom_y)
    image_crop= image.crop((left_x, top_y, right_x, bottom_y))
    image_crop.show()
    image = image_crop
  except:
      print("Wrong Input")


#Image Rotation
rotation = input('Would You Like Rotate An Image \n Yes/No: ')
if rotation.lower().startswith("y"):
  rotation_number = input('What degree You wish picture to rotate? \n Place degree number: ')
  try:
      image_rotate = image.rotate(int(rotation_number))
      image_rotate.show()
      image = image_rotate
  except:
      print("Go forward if You do not wish rotate an Image")

#Zamiana na szare
grayscale = input("Would You like change picture to grey: \n Yes/No: ")
if grayscale.lower().startswith("y"):
  image = ImageOps.grayscale(image)
  image.show()

savin_mode = input("Would You like to save Your picture? \n Yes/No: ")

if savin_mode.lower().startswith("y"):
  save_path=input("Insert path where You wish to save picture: \n ")
  if save_path:
    image.save(f"{save_path}")
