import cv2 as cv
import numpy as np
'''
鼠标做画笔
创建一个简单的应用程序，无论我们在哪里双击它，都可以在图像上绘制一个圆
'''

## dir 就是将这个对象中的所有属性显示出来
## 查看鼠标事件  它为我们提供了每个鼠标事件的坐标(x，y)
events = [i for i in dir(cv) if 'EVENT' in i]
print( events )

# print("***************")
# print([i for i in dir(cv)])



def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:## 双击左键
        cv.circle(img,(x,y),100,(255,0,0),-1)

# 创建一个黑色的图像，一个窗口，并绑定到窗口的功能
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')

# 鼠标回调函数
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()


'''
CV_EVENT_MOUSEMOVE ：鼠标移动

CV_EVENT_LBUTTONDOWN : 鼠标左键按下

CV_EVENT_RBUTTONDOWN : 鼠标右键按下

CV_EVENT_MBUTTONDOWN ： 鼠标中键按下

CV_EVENT_LBUTTONUP ： 鼠标左键放开

CV_EVENT_RBUTTONUP ： 右键放开

CV_EVENT_MBUTTONUP ： 中键放开

CV_EVENT_LBUTTONDBLCLK ： 左键双击

CV_EVENT_RBUTTONDBLCLK ： 右键双击

CV_EVENT_MBUTTONDBLCLK ： 中键双击

CV_EVENT_MOUSEWHEEL ： 鼠标向前（+）或向后（-）滑动

CV_EVENT_MOUSEHWHEEL ： 鼠标向右（+）或向左（-）滑动



Flags主要有一下几种：

CV_EVENT_FLAG_LBUTTON ：左键拖拽

CV_EVENT_FLAG_RBUTTON ： 右键拖拽

CV_EVENT_FLAG_MBUTTON ： 中键拖拽

CV_EVENT_FLAG_CTRLKEY ： Ctrl按下不放

CV_EVENT_FLAG_SHIFTKEY ： shift按下不放

CV_EVENT_FLAG_ALTKEY ： alt按下不放
'''