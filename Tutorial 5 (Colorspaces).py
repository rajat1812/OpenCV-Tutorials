import cv2
import matplotlib.pyplot as plt



def main():

    imgpath = "/Users/rajatbhalla/Downloads/standard_test_images/lena_color_256.tif"


    # Reads the image path
    img = cv2.imread(imgpath)

    # convert BGR Colorspace to RGB Colorspace
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


    plt.imshow(img)
    plt.title('Color image BGR')
    plt.xticks([])
    plt.yticks([])
    plt.show()


    plt.imshow(img)
    plt.title('Color image RGB')
    plt.xticks([])
    plt.yticks([])
    plt.show()


    # show the data on that path
    cv2.imshow('Lena',img)

    # Binds the keyboard event with cv2.imshow method
    cv2.waitKey(0)

    # it will destroy the window on keyboard event
    cv2.destroyAllWindows('Lena')


main()