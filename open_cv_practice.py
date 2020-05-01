import cv2 as cv
import numpy as np
img1 = cv.imread('test1.jpg',1)
img2 = cv.imread('test2.jpg',1)
cv.imshow('img1',img1)
cv.imshow('img2',img2)
k = cv.waitKey(0)
if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('test11.jpg',img1)
    cv.imwrite('test22.jpg',img2)
    cv.destroyAllWindows()