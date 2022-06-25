import numpy as np
import cv2

img = cv2.imread('pics/touxiang.jpg', 1)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()