import cv2 as cv

""" 
img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)
cv.waitKey(0) #Keyboard binding (wait to be pressed)

"""

#Reading videos

capture = cv.VideoCapture('Videos/dog.mp4') #integer parameters select i/o device
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)

