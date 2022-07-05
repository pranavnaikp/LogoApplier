from tkinter import filedialog
import cv2 as cv
import cvzone,os
import numpy as np
from tkinter import *
import random

os.makedirs("added-logo",exist_ok=True)
logo = cv.imread(os.getcwd() + "\logo.png",cv.IMREAD_UNCHANGED)
data = os.getcwd() + "\input-photos"
man = 0
global fileobject 
fileobject = tuple()

def openfiles():
    global fileobject 
    fileobject = filedialog.askopenfilenames(initialdir = "/",title = "Select a File",filetypes = (("Image files","*.jpg*"),("Image files","*.png* "),("all files","*.*")))
    
def manual(button_name):
    for filename in fileobject:
        print(filename)
        if not (filename.endswith('.png') or filename.endswith('.JPG') or filename.endswith('.PNG') or filename.endswith('.jpg'))or filename == "logo.png":
            continue
        img = cv.imread(filename)
        im_height,im_width , im_channel = img.shape
        min_dim = min(im_height,im_width)
        dim = int(min_dim/4)
        logo_im = cv.resize(logo,(dim,dim))
        logo_width,logo_height, logo_channel = logo_im.shape
        if button_name =="top-right":
            im_final = cvzone.overlayPNG(img,logo_im,[im_width-logo_width,0])
        if button_name == "top-left":
            im_final = cvzone.overlayPNG(img,logo_im,[0,0])
        if button_name == "bottom-right":
            im_final = cvzone.overlayPNG(img,logo_im,[im_width-logo_width,im_height-logo_height])
        if button_name == "bottom-left":
            im_final = cvzone.overlayPNG(img,logo_im,[0,im_height-logo_height])
        filename1 = os.path.basename(filename)
        os.chdir(".\\added-logo")
        cv.imwrite("{}".format(filename1),im_final)
        os.chdir( os.path.dirname(os.getcwd()))

def auto():
    for filename in fileobject:
        print(filename)
        if not (filename.endswith('.png') or filename.endswith('.JPG') or filename.endswith('.PNG') or filename.endswith('.jpg'))or filename == "logo.png":
            continue
        img = cv.imread(filename)
        im_height,im_width , im_channel = img.shape
        min_dim = min(im_height,im_width)
        dim = int(min_dim/4)

        
        cropimg1 = img[0:dim,0:dim]
        cropimg2 = img[0:dim,im_width-dim:im_width]
        cropimg3 = img[im_height-dim:im_height,0:dim]
        cropimg4 = img[im_height-dim:im_height,im_width-dim:im_width]

        blur1 = cv.GaussianBlur(cropimg1,(13,13),cv.BORDER_DEFAULT)
        blur2 = cv.GaussianBlur(cropimg2,(13,13),cv.BORDER_DEFAULT)
        blur3 = cv.GaussianBlur(cropimg3,(13,13),cv.BORDER_DEFAULT)
        blur4 = cv.GaussianBlur(cropimg4,(13,13),cv.BORDER_DEFAULT)

        canny1 = cv.Canny(blur1,125,175)
        canny2 = cv.Canny(blur2,125,175)
        canny3 = cv.Canny(blur3,125,175)
        canny4 = cv.Canny(blur4,125,175)

        contours1,he1= cv.findContours(canny1,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
        contours2,he2= cv.findContours(canny2,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
        contours3,he3= cv.findContours(canny3,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
        contours4,he4= cv.findContours(canny4,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

        len1 = len(contours1)
        len2 = len(contours2)
        len3 = len(contours3)
        len4 = len(contours4)

        listx = (len1,len2,len3,len4)

        indx = listx.index(min(listx))

        if len1 == len2 == len3 == len4:
            dim1 = [0,0]

        elif indx == 0:
            dim1 = [0,0]

        elif indx == 1:
            dim1 = [im_width-dim,0]

        elif indx == 2:
            dim1 = [0,im_height-dim]

        else:
            dim1 = [im_width-dim,im_height-dim]
        

        logo_im = cv.resize(logo,(dim,dim))

        
        filename1 = os.path.basename(filename)
        
        logo_width,logo_height, logo_channel = logo_im.shape
        im_final = cvzone.overlayPNG(img,logo_im,dim1)
        os.chdir(".\\added-logo")
        cv.imwrite("{}".format(filename1),im_final)
        os.chdir( os.path.dirname(os.getcwd()))




# Create the root window
window = Tk()

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("530x500")

#Set window background color
window.config(background = "lavender")
border_color = Frame(window, background="red")

desc1 = Label(window,highlightbackground = "black", 
                         highlightthickness = 3,bd = 0,text = "Choose photos to add logos",fg = "black",bg="lightblue")

desc2 = Label(window,highlightbackground = "black", 
                         highlightthickness = 3,bd = 5,text = "How would you like the logo to be placed?",fg = "black",bg="skyblue")


button_file_explorer = Button(window,highlightbackground = "black", 
                         highlightthickness = 5,bd = 5,text = "Select photos",bg = "lightgrey",width = 30, height = 3,fg = "blue",activebackground  = "lightgreen",command = openfiles)
button_auto = Button(window,highlightbackground = "black", 
                         highlightthickness = 5,bd = 10,text = "Place logo\nautomatically",bg = "lightyellow",activebackground  = "lightgreen",width=15,height=3,command = auto)
button_manual_tr = Button(window,highlightbackground = "black", 
                         highlightthickness = 5,bd = 10,text = "top-right\ncorner",bg = "#FFE0FF",activebackground  = "lightgreen",width=15,height=3,command = lambda: manual("top-right"),)
button_manual_tl = Button(window,highlightbackground = "black", 
                         highlightthickness = 5,bd = 10,text = "top-left\ncorner",bg = "#FFE0FF",activebackground  = "lightgreen",width=15,height=3,command = lambda: manual("top-left"),)
button_manual_br = Button(window,highlightbackground = "black", 
                         highlightthickness = 5,bd = 10,text = "bottom-right\ncorner",bg = "#FFE0FF",activebackground  = "lightgreen",width=15,height=3,command = lambda: manual("bottom-right"),)
button_manual_bl = Button(window,highlightbackground = "black", 
                         highlightthickness = 5,bd = 10,text = "bottom-left\ncorner",bg = "#FFE0FF",activebackground  = "lightgreen",width=15,height=3,command = lambda: manual("bottom-left"),)
button_exit = Button(window,highlightbackground = "black", 
                         highlightthickness = 5,bd = 5,text = "Exit",fg = "white",bg = "grey",activebackground  = "red",activeforeground  = "white",command = exit,width=30,height=3)

desc1.grid(column = 3, row = 0)

button_file_explorer.grid(column = 3, row = 1,pady = 5)
desc2.grid(column = 3, row = 6)

button_auto.grid(column = 3, row = 12)
button_manual_tr.grid(column=9,row=11)
button_manual_tl.grid(column=0,row=11)
button_manual_br.grid(column=9,row=14)
button_manual_bl.grid(column=0,row=14)
button_exit.grid(column = 3,row = 40)

# Let the window wait for any events
window.mainloop()
