import cv2
import numpy as np
import matplotlib.pyplot as plt


def main():
    imgpath = "/Users/rajatbhalla/Downloads/standard_test_images/lena_color_512.tif"

    img1 = cv2.imread(imgpath, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

    rows, columns, channels = img1.shape

    # set of points of input image
    point1  = np.float32([[100,100], [300,100],[100,300]])

    # set of points of output image
    point2 = np.float32([[100,100], [400,150],[400,300]])

    # Affine transformation
    A = cv2.getAffineTransform(point1,point1)

    print("a",A)

    output = cv2.warpAffine(img1,A,(columns,rows))


    plt.imshow(output)
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()