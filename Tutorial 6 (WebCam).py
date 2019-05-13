import cv2
import matplotlib.pyplot as plt

def main():


    cam = cv2.VideoCapture(0)

    if cam.isOpened():
        ret,frame = cam.read()
        print(ret)
        print(frame)
    else :
        ret = False

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    plt.imshow(img)
    plt.title('Color image RGB')
    plt.xticks([])
    plt.yticks([])
    plt.show()

    cam.release()


main()
