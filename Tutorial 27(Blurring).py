import cv2
import numpy as np
import matplotlib.pyplot as plt


def main():

    imgpath = "/Users/rajatbhalla/Downloads/standard_test_images/lena_color_256.tif"
    img = cv2.imread(imgpath)
    cv2.imshow('original image', img)


    #Creating 3x3 kernel
    kernal_3x3 = np.ones((3,3),np.float32)/9

    blurred = cv2.filter2D(img,-1,kernal_3x3)

    # Creating 3x3 kernel
    kernal_7x7= np.ones((7, 7), np.float32)/49

    blurred2 = cv2.filter2D(img, -1, kernal_7x7)

    cv2.imshow('blurred 3x3', blurred)
    cv2.imshow('blurred 7x7', blurred2)
    cv2.waitKey(0)



    cv2.destroyAllWindows()



main()