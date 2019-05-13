import cv2


def main():
    windowName = "Live Streaming Record"
    cv2.namedWindow(windowName)
    cam = cv2.VideoCapture(0)

    filepath = "/Users/rajatbhalla/PycharmProjects/Output.avi"
    codec =  cv2.VideoWriter_fourcc('X','V','I','D')
    frames = 30
    resolution = (1280,760)

    videoFileOutput = cv2.VideoWriter(filepath,codec,frames,resolution)


    if cam.isOpened():
        ret, frame = cam.read()
        print(ret)
        print(frame)
    else:
        ret = False

    while ret:

        ret, frame = cam.read()

        videoFileOutput.write(frame)

        cv2.imshow(windowName,frame)

        if cv2.waitKey(1) == 27:
            break

    videoFileOutput.release()
    cam.release()
    cv2.destroyAllWindows(windowName,frame)



main()
