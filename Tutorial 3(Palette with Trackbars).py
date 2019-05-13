import cv2
import numpy as np

def emptyFunc():
    pass

def main():

    img1 = np.zeros((512,512,3), np.uint8)
    windowName = 'Opencv BGR color palette'
    cv2.namedWindow(windowName)

    cv2.createTrackbar('B', windowName, 0, 255, emptyFunc)
    cv2.createTrackbar('G', windowName, 0, 255, emptyFunc)
    cv2.createTrackbar('R', windowName, 0, 255, emptyFunc)

    # 'B'  - Name of the color/ name of the trackbar
    # windowName - name of the window associated with trackbar
    # 0 - min value associated with trackbar
    # 255 - max value associated with trackbar
    # emptyFunc() - func will call when we move the slider

    while(True):
        cv2.imshow(windowName,img1)

        # window will be close only on esc
        if cv2.waitKey(1) == 27:
            break
        blue = cv2.getTrackbarPos('B', windowName)
        green = cv2.getTrackbarPos('G', windowName)
        red = cv2.getTrackbarPos('R', windowName)

        # Create a composite image
        img1[:] = [blue,green,red]
        print(blue , green,red)
    cv2.destroyAllWindows()


main()