from PIL import Image

# First Step - Insert Picture or will be done automatically 
a = input("Insert Photo, photo path You wish to Edit \n Isert/Paste Here:  ")
try:
    image = Image.open(a)
except:
    image = Image.open('Maxi.jpg')
print("Picture wasn't insert, automatic upload pictire as an example")


#Image Rotation
rotation = input('Would You Like Rotate An Image \n Answer Yes/No')
if rotation.lower().startswith("y"):
   rotation_number = input('What Degree You wish picture to rotate? \n Plase Degree Number')
try:
    image_rotate = image.rotate(int(rotation_number))
    image_rotate.show()
except:
    print("Can't accept Your Answer")
    
    
    