import cv2
import numpy as np
import matplotlib.pyplot as plt


def main():
    imgpath = "/Users/rajatbhalla/Downloads/standard_test_images/lena_color_512.tif"

    img1 = cv2.imread(imgpath, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

    # get the shape of the image & 3 params(channels) to collect the shape of the image bcz its a coloured image
    rows,columns,channels = img1.shape

    # Translation
    T = np.float32([[1,0,50],[0,1,50]])
    print(T, rows, columns, channels)

   # Rotation
   #scaling takes place on both axis
    R = cv2.getRotationMatrix2D((columns/2,rows/2), 0,0.5)

    # 0.5 = scaling factor of image
    # 0 = angle
    print(R)


    # Transformation
    translation = cv2.warpAffine(img1, T, (columns, rows))
    rotation = cv2.warpAffine(img1,R,(columns,rows))


    plt.imshow(rotation)
    plt.imshow(translation)
    plt.show()
    

    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()