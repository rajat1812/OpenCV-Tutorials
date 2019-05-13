import cv2
import numpy as np

cam = cv2.VideoCapture('/Users/rajatbhalla/Downloads/Befikra Tiger Shroff Disha Patani - HDYaar.Com.mp4')

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.createBackgroundSubtractorMOG2()

if cam.isOpened():
    ret, frame = cam.read()
    print(ret)
    print(frame)
else:
    ret = False

while True:
    ret, frame = cam.read()

    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask,cv2.MORPH_OPEN,kernel)

    cv2.imshow('frame',fgmask)
    cv2.imshow('web',frame)


cv2.waitKey(0)
cam.release()
cv2.destroyAllWindows()
