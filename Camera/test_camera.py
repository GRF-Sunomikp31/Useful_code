#测试免驱摄像头帧率和分辨率
import cv2
import time

capture = cv2.VideoCapture(3)
while True:
    start = time.time()
    ret, frame = capture.read()
    frame = cv2.flip(frame,1)   #镜像操作
    cv2.imshow("video", frame)
    sp = frame.shape
    print(sp)
    key = cv2.waitKey(15)#这个必须写，否则会因为刷新的问题显示不上
    end = time.time()
    seconds = end - start
    print(1/seconds)

cv2.destroyAllWindows()
