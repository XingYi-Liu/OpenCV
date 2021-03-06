import cv2
import numpy as np
'''
painting
'''

# 创建黑色的图像
img = np.zeros((512,512,3), np.uint8)##BGR

cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv2.circle(img,(447,63), 63, (0,0,255), -1)
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,1)
## def ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness=None, lineType=None, shift=None)
## (长轴 短轴)

## 顶点的坐标。将这些点组成形状为ROWSx1x2的数组，其中ROWS是顶点数，并且其类型应为int32
## 三个参数为False，您将获得一条连接所有点的折线
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
## (10,500)  指的是  bottom-left 位置
## putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None)
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()