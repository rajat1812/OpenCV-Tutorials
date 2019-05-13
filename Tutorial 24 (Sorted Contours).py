
import cv2


imgpath = "/Users/rajatbhalla/Downloads/shapes.jpeg"
image = cv2.imread(imgpath)
cv2.imshow('Input image', image)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray,30,200)
cv2.imshow('edged image',edged)
cv2.waitKey(0)

# Finding Contours
# Use a copy of your image edge.copy(), since find contours alters the image

contours , hierarchy = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('countour image', edged)
cv2.waitKey(0)


print('no. of contours found' , str(len(contours)))


# Function we'll use to draw contour area
def get_contour_areas(contours):

    # return the araes of all contours as list
    all_areas = []
    for cnt in contours:
        area =  cv2.contourArea(cnt)
        all_areas.append(area)
    return all_areas


cont = get_contour_areas(contours)
print("Contour area before sorting",cont)

sorted_contours = sorted(contours, key= cv2.contourArea,reverse=True)

cont2 = get_contour_areas(sorted_contours)
print("Contour area after sorting",cont2)


# Iterate over our contours and draw one by one


for c in sorted_contours:

    cv2.drawContours(image,[c], -1, (0, 255, 0), 4)
    cv2.imshow('contour image', image)
    cv2.waitKey(0)

cv2.destroyAllWindows()


