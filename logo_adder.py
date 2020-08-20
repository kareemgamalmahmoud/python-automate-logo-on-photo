import os
from PIL import Image


# first we will take the name of the logo
# that the user want to add .
# then , take the name of the folder the we
# will add the photos after adding the logo .

LOGO_NAME = 'face.png' #input('enter the logo name with extention : ')
FOLDER_NAME = 'with logo image' #input('enter the folder name : ')

# get the informations of the logo ==>(width , height)

logo_image = Image.open(LOGO_NAME)
logo_width , logo_height = logo_image.size

# create the folder if it does not exist

if not( os.path.exists(FOLDER_NAME) ):
    os.mkdir(FOLDER_NAME)

# loop over the images

# counter
count = 0

for filename in os.listdir('.'):
    # check that the file is not logo
    if not(filename.endswith('.png') or filename.endswith('.jpg') or filename == logo_image):
        continue
    img = Image.open(filename)
    width, height = img.size

    # add logo to the image
    # there is a method called (paste) in pillow
    # that make us to add the photo
    img.paste(logo_image, (width - logo_width, height - logo_height))

    # know let's save the image
    img.save(os.path.join(FOLDER_NAME, filename))
    count += 1
    print(f'done image : {filename}')


print(f'  {count} photos has been DONE')