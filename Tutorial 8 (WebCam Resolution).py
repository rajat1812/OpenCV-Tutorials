import cv2


def main():
    windowName = "Live Streaming"
    cv2.namedWindow(windowName)
    cam = cv2.VideoCapture(0)

    print('width :'+str(cam.get(3)))
    print('height :'+str(cam.get(4)))

    cam.set(3,400)
    cam.set(4,300)

    print('width :'+str(cam.get(3)))
    print('height :'+str(cam.get(4)))

    if cam.isOpened():
        ret, frame = cam.read()
        print(ret)
        print(frame)
    else:
        ret = False

    while ret:

        ret, frame = cam.read()

        output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow(windowName, output)

        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows(windowName)
    cam.release()


main()
