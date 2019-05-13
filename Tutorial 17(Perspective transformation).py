import cv2
import matplotlib.pyplot as plt
import numpy as np


def main():
   imgpath = "/Users/rajatbhalla/Downloads/standard_test_images/lena_color_512.tif"

    img1 = cv2.imread(imgpath, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

    rows, columns, channels = img1.shape
    print(rows,columns)

    point1 = np.float32([[0, 0], [400, 0], [0, 400], [400, 400]])
    point2 = np.float32([[0, 0], [100, 0], [0, 100], [100, 100]])

    P = cv2.getPerspectiveTransform(point1, point2)

    print(P)

    output = cv2.warpPerspective(img1, P, (100,100))

    plt.imshow(output)
    plt.title('Changed Perspective')
    plt.show()


if __name__ == "__main__":
    main()