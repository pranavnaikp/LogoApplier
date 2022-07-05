import cv2 as cv

img  =  cv.imread('IMG_20220522_090907.jpg')

cv.imshow("img",img)

blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)

dim = img.shape
im_height,im_width , im_channel = img.shape
ratio = int(im_width/im_height)
min_dim = min(im_height,im_width)
dim = int(min_dim/3)

    
cropimg1 = img[0:dim,0:dim]
cropimg2 = img[0:dim,im_width-dim:im_width]
cropimg3 = img[im_height-dim:im_height,0:dim]
cropimg4 = img[im_height-dim:im_height,im_width-dim:im_width]

blur1 = cv.GaussianBlur(blur,(5,5),cv.BORDER_DEFAULT)
blur1 = cv.GaussianBlur(cropimg1,(5,5),cv.BORDER_DEFAULT)
blur2 = cv.GaussianBlur(cropimg2,(5,5),cv.BORDER_DEFAULT)
blur3 = cv.GaussianBlur(cropimg3,(5,5),cv.BORDER_DEFAULT)
blur4 = cv.GaussianBlur(cropimg4,(5,5),cv.BORDER_DEFAULT)

canny  = cv.Canny(blur, 125,175)
canny1 = cv.Canny(blur1,125,175)
canny2 = cv.Canny(blur2,125,175)
canny3 = cv.Canny(blur3,125,175)
canny4 = cv.Canny(blur4,125,175)

contours, he = cv.findContours(canny,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
contours1,he1= cv.findContours(canny1,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
contours2,he2= cv.findContours(canny2,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
contours3,he3= cv.findContours(canny3,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
contours4,he4= cv.findContours(canny4,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

len1 = len(contours1)
len2 = len(contours2)
len3 = len(contours3)
len4 = len(contours4)
lenx = len(contours)

cv.imshow("img1",canny1)
cv.imshow("img2",canny2)
cv.imshow("img3",canny3)
cv.imshow("img4",canny4)

listx = (len1,len2,len3,len4)

indx = listx.index(min(listx))

print(lenx)
print(len1)
print(len2)
print(len3)
print(len4)


canny = cv.Canny(blur,125,175)

cv.imshow("edges",canny)


