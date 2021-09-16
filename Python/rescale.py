import cv2 as cv

img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    #Images, video, live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width,height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)


def changeRes(width, height):
    #Live video
    capture.set(3, width)
    capture.set(4, height)
    

capture = cv.VideoCapture('Videos/dog.mp4') #integer parameters select i/o device
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, 0.20)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()


cv.waitKey(0)