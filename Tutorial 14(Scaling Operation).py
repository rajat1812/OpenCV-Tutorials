import cv2

def main():
    imgpath = "/Users/rajatbhalla/Downloads/standard_test_images/lena_color_512.tif"

    img1 = cv2.imread(imgpath, 1)

    # Shrinking
    output = cv2.resize(img1,None,fx=1.5,fy=1 , interpolation=cv2.INTER_AREA)

    # Zooming , it operates on neighbourhood of  4x4(pixel area for the given point)
    output1 = cv2.resize(img1, None, fx=1.5, fy=1, interpolation=cv2.INTER_CUBIC)

    # it gives original size of image
    output2 = cv2.resize(img1, None, fx=1, fy=1, interpolation=cv2.INTER_LINEAR)

    output3 = cv2.resize(img1, None, fx=1.5, fy=1, interpolation=cv2.INTER_NEAREST)

    # it operates on neighbourhood of 8x8(pixel area for the given point)
    output4 = cv2.resize(img1, None, fx=1.5, fy=1, interpolation=cv2.INTER_LANCZOS4)

    cv2.imshow('AREA',output)
    cv2.imshow('CUBIC', output1)
    cv2.imshow('LINEAR', output2)
    cv2.imshow('NEAREST', output3)
    cv2.imshow('LANCZOS4', output4)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()