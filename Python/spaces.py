import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/park.jpg')
cv.imshow('Cats', img)

# BGR to Grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# BGR to HSV

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# BGR to L*a*b

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)  

plt.imshow(img)
plt.show()

# Grayscale to BGR (cant convert from gs to hsv -> gotta pass trough BGR)

hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv to BGR', hsv_bgr)




cv.waitKey(0)