import cv2
import numpy as np

imgpath = "/Users/rajatbhalla/Downloads/sunflower.jpeg"
img = cv2.imread(imgpath)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('original image', img)


# set the detector
detector = cv2.SimpleBlobDetector_create()

# Detect keypoints
keypoints = detector.detect(img)

# Draw detected blobs as red circles.
# cv2.DRAW**** ensures the size of the circle corresponds to the size of blob

blank= np.zeros((1,1))
blobs = cv2.drawKeypoints(img,keypoints,blank,(0,0,255),cv2.DRAW_MATCHES_FLAGS_DEFAULT)

cv2.imshow("Blobs",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


