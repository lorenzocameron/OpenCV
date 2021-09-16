import cv2 as cv 

img = cv.imread('Photos/park.jpg')
cv.imshow('Cat', img)

#Converting to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)


#Blur

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

#Edge Cascade

canny = cv.Canny(img, 125, 175)
cv.imshow('canny', canny)

#Dilate image with structuring element

dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('Dilated', dilated)

#Eroding

eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('Eroded', eroded) 

#Resize

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC) #Area for reduced
cv.imshow('Resized',resized)

#Cropping

cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)