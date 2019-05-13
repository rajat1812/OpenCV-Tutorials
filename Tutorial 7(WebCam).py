import cv2



windowName = "Live Streaming"
cv2.namedWindow(windowName)
cam = cv2.VideoCapture(0)

if cam.isOpened():
        ret,frame = cam.read()
        print(ret)
        print(frame)
else :
        ret = False

while ret:

    ret,frame = cam.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow(windowName,frame)

    if cv2.waitKey(1) == 27:
        break


cv2.destroyAllWindows(windowName)
cam.release()


