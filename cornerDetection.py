import cv2 as cv
import numpy as np


capture = cv.VideoCapture(0)


while True:
    ret, img = capture.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    corners = cv.goodFeaturesToTrack(gray, 950, 0.01, 10)
    corners = np.int0(corners)

    for corner in corners:
        x, y = corner.ravel()
        cv.circle(img, (x,y), 3, 255, -1)

    cv.imshow('Corner', img)
    k = cv.waitKey(5) & 0xff
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()
