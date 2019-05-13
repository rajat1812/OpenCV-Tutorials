import cv2


imgpath = "/Users/rajatbhalla/Downloads/squares.jpeg"
image = cv2.imread(imgpath)
cv2.imshow('Input image', image)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray,30,200)
cv2.imshow('edged image',edged)
cv2.waitKey(0)

# Finding Contours
# Use a copy of your image edge.copy(), since find contours alters the image
# contours only process grayscale images
contours , hierarchy = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)



print('no. of contours found' , str(len(contours)))


# Draw all contours
cv2.drawContours(image,contours,-1,(0,255,0),4)

cv2.imshow('contour image',image)
cv2.waitKey(0)