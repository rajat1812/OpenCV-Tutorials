import cv2
import matplotlib.pyplot as plt

def main():

    imgpath = "/Users/rajatbhalla/Downloads/standard_test_images/lena_color_256.tif"
    outpath = ""

    # Reads the image path
    img = cv2.imread(imgpath)
    img2 =  cv2.imread(imgpath,0)

    # save the image at other path
    # cv2.imwrite(outpath,img)

    # it will show image in python console
    # we can change the image color / coloured maps using cmap
    plt.imshow(img, cmap='Accent')
    plt.show()
    plt.imshow(img, cmap='gray')
    plt.show()


    # show the data on that path
    cv2.imshow('Lena',img)
    cv2.imshow('Lena 2', img2)
    # Binds the keyboard event with cv2.imshow method
    cv2.waitKey(0)

    # it will destroy the window on keyboard event
    cv2.destroyAllWindows('Lena','Lena 2')


main()