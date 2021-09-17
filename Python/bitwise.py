import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rect = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(),(200,200), 200, 255, -1)

cv.imshow('rect', rect)
cv.imshow('circle', circle)

# bitwise and

bit_and = cv.bitwise_and(rect,circle)
cv.imshow('image', bit_and)


# bitwise or

bit_or = cv.bitwise_or(rect,circle)
cv.imshow('image2', bit_or)

# bitwise XOR

bit_xor = cv.bitwise_xor(rect,circle)
cv.imshow('image3', bit_xor)

# bitwise not

bit_not = cv.bitwise_not(rect)
cv.imshow('image4', bit_not)



cv.waitKey(0)