import cv2 as cv
import numpy as np
img = cv.imread( "messi5.jpg")
kernel = np.ones( (15,15),np.float32)/255
cv.imwrite( "smooth.png", cv.filter2D( img, -1, kernel))
cv.imwrite( "smooth_gblur.png", cv.GaussianBlur( img, (15,15),0))
cv.imwrite( "smooth_med.png", cv.medianBlur( img, 15))
# while True:
#     _,frame = cap.read()
#     # hsv = cv.cvtColor( frame, cv.COLOR_BGR2HSV)
#     kernel = np.ones( ( 15,15), np.float32)/225
#     smoothed = cv.filter2D( frame, -1, kernel)
#     blur = cv.GaussianBlur( frame, (15,15), 0)
#     med = cv.medianBlur( frame, 15)
#     cv.imshow( "frame", frame)
#     cv.imshow( "smmoth", smoothed)
#     cv.imshow( "gblur", blur)
#     cv.imshow( "med", med)
#     # cv.imshow( "hsv", hsv)
#     if cv.waitKey(1) == ord("q"): break
# cap.release()
cv.destroyAllWindows()