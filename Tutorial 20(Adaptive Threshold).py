# Adaptive threshold is useful in bimodel images where we have diffrent lightning conditions

import cv2
import matplotlib.pyplot as plt


def main():


    imgpath = "/Users/rajatbhalla/Downloads/standard_test_images/lena_color_512.tif"
    imgpath1 = "/Users/rajatbhalla/Downloads/th2.jpeg"

    img = cv2.imread(imgpath1, 0)


    # it not works with the coloured images
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    # it is the neighbourhood pixels on which the adavtive algo supposed to work
    # more is the block size more the image is clear(vivid)
    block_size = 513

    constant = 2
    th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, constant)
    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, constant)

    output = [img, th1, th2]

    titles = ['Original', 'Mean Adaptive', 'Gaussian Adaptive']

    for i in range(3):
        plt.subplot(1, 3, i + 1)
        plt.imshow(output[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()


if __name__ == "__main__":
    main()