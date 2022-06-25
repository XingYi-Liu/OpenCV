import numpy as np
import cv2 as cv

img = cv.imread('pics/touxiang.jpg')
print(img.shape)##(300,300,3)
#如果图像是灰度的，则返回的元组仅包含行数和列数

## 像素总数
print(img.size)# 270000

print(img.dtype)# uint8

px = img[100,100]
print(px)## [184 187 192] BGR

## 仅仅访问蓝色 通道
print(img[100,100,0])## 184

## numpy 是快速数组计算的优化裤  对于访问 很慢

## 更好的像素访问
## 编辑方法
readpx = img.item(100,100,2)
print(readpx)## 192

## 修改read 值
img.itemset((100,100,2),100)
print(img.item(100,100,2))## 100


# img2 = cv.imread('pics/roi.jpg')
# print(img2.shape)# (280, 450, 3)
# ball = img2[220:280, 330:390]
# img2[273:333, 100:160] = ball
# cv.imshow('img2',img2)
# cv.waitKey(0)

## 拆分
# b, g, r = cv.split(img)  基本不用
## 合并
img = cv.merge((b,g,r))

b = img [:, :, 0]

img [:, :, 2] = 0