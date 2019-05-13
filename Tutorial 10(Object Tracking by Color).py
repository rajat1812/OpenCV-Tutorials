import cv2
import numpy as np

def main():


    windowName = "Live Streaming"
    cv2.namedWindow(windowName)
    cam = cv2.VideoCapture(0)

    if cam.isOpened():
        ret,frame = cam.read()

    else :
        ret = False

    while ret:

        ret,frame = cam.read()

        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        # Blue Color
        low = np.array([100,50,50])
        high = np.array([140,255,255])

        #  # it will show only that coloured objects in black & white form
        image_mask = cv2.inRange(hsv,low,high)

        # it will show only that coloured objects in coloured form
        output = cv2.bitwise_and(frame,frame,mask=image_mask)

        cv2.imshow(windowName, frame)
        cv2.imshow("Image_mask", image_mask)
        #cv2.imshow("Color Tacking",output)

        if cv2.waitKey(1) == 27:
            break


    cv2.destroyAllWindows(windowName)
    cam.release()



main()
