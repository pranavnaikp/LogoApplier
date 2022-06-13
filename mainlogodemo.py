'''required libraries are pillow'''
from tkinter import *
import os
from PIL import Image, ExifTags
from tkinter import filedialog

logo_file = 'logo.png'
logoIm = Image.open(logo_file)
size_100 = (100,100)

os.makedirs('withlogodemo', exist_ok = True)
print("creating images with logo!....")
	

try:
    files = filedialog.askopenfilenames(initialdir = "/",title = "Select a File",filetypes = (("Image files","*.jpg*"),("all files","*.*")))

    for filename in files:

        if not (filename.endswith('.png') or filename.endswith('.JPG') or filename.endswith('.PNG') or filename.endswith('.jpg')) or filename.endswith('.png') or filename == logo_file:
            continue
        im = Image.open(filename)
        exif = im._getexif()

        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation]=='Orientation':
                break
        
        exif = im.getexif()
        print(type(exif))
       
        if exif == None:
            pass
        elif exif[orientation] == 3:
            im=im.rotate(180, expand=True)
        elif exif[orientation] == 6:
            im=im.rotate(270, expand=True)
        elif exif[orientation] == 8:
            im=im.rotate(90, expand=True)
        width, height = im.size
        print(height, width, height/width)
        ratio = int(height/width)
        min_dim = min(height,width)
        dim=int(min_dim/3)
        logo_size=(dim,dim)
        print(ratio)
        logoIm = logoIm.resize(logo_size)
    

    



        logoWidth, logoHeight = logoIm.size
        #print(logoHeight,logoWidth)
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
        im.save(os.path.join('withlogodemo', filename))
        #im.show()
except Exception as e:
    print ("Exif data spinning errored (might have no exif data). Delete {} to remove error".format(filename))
    print (e)
print("done!!!")
