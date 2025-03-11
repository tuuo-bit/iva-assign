import cv2 as cv
import numpy as np
img = cv.imread( "image.png")
gimg = cv.cvtColor( img, cv.COLOR_BGR2GRAY)
bimg = cv.GaussianBlur( gimg, (7,7), sigmaX=2, sigmaY = 2)

sobelx = cv.Sobel(  bimg, cv.CV_16S, 1, 0, ksize = 1)

sobely = cv.Sobel(  bimg, cv.CV_16S, 0, 1, ksize = 1)

sobelxy = np.sqrt( sobelx**2 + sobely**2)

canny = cv.Canny( bimg, 10, 20)

cv.imshow( "xy", sobelxy)
cv.imshow( "c", canny)
cv.imwrite( "edge_b.png", bimg)
cv.imwrite( "edge_s.png", sobelxy)
cv.imwrite( "edge_c.png", canny)
cv.waitKey(0)
cv.destroyAllWindows()