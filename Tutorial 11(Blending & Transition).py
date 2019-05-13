

import cv2
import matplotlib.pyplot as plt
import numpy as np
import time

def main():


    imgpath1 = "/Users/rajatbhalla/Downloads/standard_test_images/lena_color_512.tif"
    imgpath2 = "/Users/rajatbhalla/Downloads/standard_test_images/cameraman.tif"


    img1 = cv2.imread(imgpath1)
    img2 = cv2.imread(imgpath2)

    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

    alpha = 0.5
    beta  =0.5
    gamma = 0

    # blending
    blending = cv2.addWeighted(img1,alpha,img2,beta,gamma)

    # transition
    for i in np.linspace(0,1,10):
        alpha = i
        beta = 1 - alpha
        transition = cv2.addWeighted(img1,alpha,img2,beta,gamma)
        cv2.imshow('Transition',transition)
        
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()

    images = [img1,img2,blending]

    for i in range(3) :
       plt.imshow(images[i])

    plt.show()

main()
