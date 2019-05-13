import cv2
import numpy as np

windowName = 'Drawing'

img = np.zeros((512,512,3),np.uint8)

cv2.namedWindow(windowName)

# mouse callback function

def draw_shape(event,cordinate1,cordinate2,flags,params):
    if event == cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img,(cordinate1,cordinate2),40,(0,255,0),-1)

    elif event == cv2.EVENT_MOUSEMOVE:
        cv2.line(img, (cordinate1,cordinate2), (cordinate1,cordinate2), (255, 0, 0), 2)


# bind the callback function to window
cv2.setMouseCallback(windowName,draw_shape)


def main():
    while (True):
        cv2.imshow(windowName, img)

        # window will be close only on esc
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()


main()