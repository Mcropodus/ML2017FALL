import cv2

img = cv2.imread('002.jpg',0)  # open file ;  0 to tell the computer that image is  Gray Scale

Pixel = img.shape  #get the size of image
x = Pixel[0] #x of image
y = Pixel[1] #y for image
for i in range(x):
    for j in range(y):
        if img[i][j] < 128:    #if the pixel in range 0 to 127, change to 0 for black
            img[i][j] = 0
        else:                  #if the pixel in range 128 to 255, change to 255 for white
            img[i][j] = 255

cv2.imshow('img',img) #show the result
cv2.waitKey()

cv2.imwrite('result.jpg',img) #save the file







