import cv2 as cv
import numpy as np


x = np.uint8([250])## ndarray  类型
y = np.uint8([10])
print( cv.add(x,y) ) # 250+10 = 260 => 255  饱和运算
# [[255]]

print( x+y )  # # 250+10 = 260 % 256 = 4  # 模运算  uint8  最大256
# [4]


## 图像融合   本质就是将图像赋予不同的权重
## cv.addWeighted()  需要图像大小一样哎
img1 = cv.imread('pics/lena.png')
img1 = np.resize(img1,(300,300,3))
print(img1.shape)
img2 = cv.imread('pics/touxiang.jpg')
print(img2.shape)
dst = cv.addWeighted(img1,0.7,img2,0.3,0)
cv.imshow('dst',dst)
cv.waitKey(0)

cv.bitwise_and()
