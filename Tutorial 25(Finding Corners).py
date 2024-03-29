import cv2
import numpy as np


imgpath = "/Users/rajatbhalla/Downloads/chessboard.jpeg"
image = cv2.imread(imgpath)
resize_image = cv2.resize(image,(1000,1000))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# The Corner Harris function requires the array datatype to be float32
gray = np.float32(gray)

# input_image,block_size,kernel_size,k
harris_corners = cv2.cornerHarris(gray,3,3,0.05)

# We use dilation of the corner points to enlarge them
#kernel = np.ones((3,3),np.uint8)
#harris_corners = cv2.dilate(harris_corners,kernel,iterations=2)

# Threshold for an optimal value , it may vary depending on the image.
image[harris_corners > 0.025* harris_corners.max()] = [255,127,127]

cv2.imshow('Harris_Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
