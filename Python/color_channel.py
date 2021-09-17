import cv2 as cv 
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('boston0',img)

b,g,r = cv.split(img) #split color channel


blank = np.zeros(img.shape[:2], dtype='uint8')

# displaying color channel not in grayscale

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r]) #merge color channel
cv.imshow('merged',merged)

blank = np.zeros(img.shape[:2], dtype='uint8')

cv.waitKey(0)