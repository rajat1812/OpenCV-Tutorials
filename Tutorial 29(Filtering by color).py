import cv2
import numpy as np
def main():


    cam = cv2.VideoCapture(0)

    if cam.isOpened():
        ret,frame = cam.read()
        print(ret)
        print(frame)
    else :
        ret = False

    while ret:

        # define range of PURPLE color in HSV
        lower_purple = np.array([125, 0, 0])
        upper_purple = np.array([175, 255, 255])

        ret,frame = cam.read()



        # Convert image from RGB/BGR to HSV so we easily filter
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Use inRange to capture only the values between lower & upper_purple
        mask = cv2.inRange(hsv_img, lower_purple, upper_purple)

        # Perform Bitwise AND on mask & our original frame
        res = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('Original', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('Filtered color only', res)




        if cv2.waitKey(1) == 27:
            break


    cv2.destroyAllWindows()
    cam.release()


main()
