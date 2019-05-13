import cv2

imgpath = "/Users/rajatbhalla/Downloads/chessboard.jpeg"
image = cv2.imread(imgpath)
resize_image = cv2.resize(image,(1000,1000))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# We specific the top 50 corners

# 100 = max_corners -> maximum no. of corners to return
# 0.01 = quality level of image corners max(1500) , min(0.01)
#15 = minimum distance (euclidean distance) between the returned corners
corners = cv2.goodFeaturesToTrack(gray,100,0.01,20)

for corner in corners:
    x,y = corner[0]
    x = int(x)
    y = int(y)
    cv2.rectangle(image,(x-10,y-10),(x+10,y+10),(0,255,0),2)

cv2.imshow('Corner found',image)
cv2.waitKey(0)
cv2.destroyAllWindows()