import cv2 as cv
import numpy as np
img = cv.imread( "image.png")
# img = cv.imread( "C:\\Users\\DELL\\Documents\\SEM 6\\image.png")
cv.imshow( "Original", img)
cv.destroyAllWindows()
hsv = cv.cvtColor( img, cv.COLOR_BGR2HSV)
arr = [ [(0,50,50),(10,255,255),"q1_red"], [(45,50,50),(75,255,255),"q1_green"], [(110,50,50),(130,255,255),"q1_blue"]]
for arr1,arr2,name in arr:
    mask = cv.inRange( hsv, np.array( arr1), np.array( arr2))
    res = cv.bitwise_and( img, img, mask = mask)
    cv.imshow( name, res)
    cv.waitKey(0)
    cv.destroyAllWindows()  
    cv.imwrite( name+".png", res)   