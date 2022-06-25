# import cv2
# import mediapipe as mp
# import time

# mpHands = mp.solutions.hands
# mpDraw = mp.solutions.drawing_utils
# hands = mpHands.Hands()

# cap = cv2.VideoCapture(0)

# while True:
#     flag,img = cap.read()
#     imgrgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#     res = hands.process(imgrgb)
#     # print(res.multi_hand_landmarks)

#     if res.multi_hand_landmarks:
#         for handLms in res.multi_hand_landmarks:
#             mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)


#     cv2.imshow('frame', img)
#     if cv2.waitKey(1) == ord('q'):
#         break
# # 完成所有操作后，释放捕获器
# cap.release()
# cv2.destroyAllWindows()
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
print(volume.GetVolumeRange())

