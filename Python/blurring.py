import cv2 as cv 

img = cv.imread('Photos/cats.jpg')
cv.imshow('cats', img)

# Averaging

avg = cv.blur(img, (7,7))
cv.imshow('avg', avg)

# Gaussian (less 'blurring' but more natural)

blur = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('blur', blur)

# Median blur (useful for remove noises)

median = cv.medianBlur(img, 7)
cv.imshow('median', median)

# Bilateral (reteains edges)

bi = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bi', bi)



cv.waitKey(0)