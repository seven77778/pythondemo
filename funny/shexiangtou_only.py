import cv2
cap = cv2.VideoCapture(0)
f, frame = cap.read()#此刻拍照
cv2.imwrite("example.jpg", frame)# 将拍摄内容保存为png图片
cap.release()# 关闭调用的摄像头