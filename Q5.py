import cv2 as cv
import numpy as np

haar = cv.CascadeClassifier( "haarcascade_frontalface_alt.xml")
img = cv.imread( "face.jpg")
gimg = cv.cvtColor( img, cv.COLOR_BGR2GRAY)
gimg_d = gimg.copy()
img_d = img.copy()

faces = haar.detectMultiScale( gimg, scaleFactor=1.2, minNeighbors=5)

#go over list of faces and draw them as rectangles on original colored img
for (x, y, w, h) in faces:
    cv.rectangle( img_d, (x,y), (x+w,y+h), ( 0,255,0), 5)
    cv.rectangle( gimg_d, (x, y), (x+w, y+h), (0, 255, 0), 5)

# cv.imwrite( "col", img)
cv.imwrite( "face_g.jpg", gimg)
cv.imwrite( "face_d.jpg", img_d)
cv.imwrite( "face_gd.jpg", gimg_d)

cv.waitKey(0)
cv.destroyAllWindows()