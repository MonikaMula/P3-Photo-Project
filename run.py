from PIL import Image, ImageColor

# First Step - Insert Picture or will be done automatically 
a = input("Insert Photo, photo path You wish to Edit \n Insert/Paste Here:  ")
try:
    image = Image.open(a)
except:
    image = Image.open('Maxi.jpg')
    print("Picture wasn't insert, automatic upload picture as an example")


#Image Rotation
    rotation = input("Would You Like Rotate An Image \n Yes/No: ")
if  rotation.lower().startswith("y"):
    rotation_number = input("What degree You wish picture to rotate? \n Place degree number: ")
try:
    image_rotate = image.rotate(int(rotation_number))
    image_rotate.show()
except:
    print("Go forward if You do not wish rotate an Image")
    
    
#Image_Cropping 
    cropping = input("Crop image? \n Yes/No: ")
if  cropping.lower().startswith("y"):
try:   
    image_crop = image_crop((left_x,top_y,right_x,bottom_y))
    image_crop.show()
except:
    print("Skip")
    
    