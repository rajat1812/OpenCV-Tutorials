import cv2
import matplotlib.pyplot as plt
import numpy as np
import random


def main():
    imgpath = "/Users/rajatbhalla/Downloads/standard_test_images/mandril_color.tif"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    rows,columns,channels = img.shape

    # probability factor of noise in the image
    p=0.05

    output = np.zeros(img.shape,np.uint8)

    for i in range(rows):
        for j in range(columns):
            r = random.random()
            if r < p/2 :
                # pepper sprinkled
                output[i][j]= [0,0,0]
            elif r< p:
                # salt sprinkled
                output[i][j] = [255,255,255]
            else:
                output[i][j] = img[i][j]



    plt.imshow(output)
    plt.title('Image with Salt and Pepper Noise')
    plt.show()


if __name__ == "__main__":
    main()