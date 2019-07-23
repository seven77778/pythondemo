import itchat
import os
import cv2

# pip install opencv-python

# 注册消息响应事件，消息类型为itchat.content.TEXT，即文本消息
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
   print(msg)
   global flag
   cap = cv2.VideoCapture(0)
   ret, img = cap.read()
   cv2.imwrite("pic.jpg", img)
   # 将图片发送至文件传输助手
   itchat.send('@img@%s' % u'pic.jpg', 'filehelper')
   # 释放摄像头
   cap.release()
   print('end')

if __name__ == '__main__':
   itchat.auto_login(True)
   # itchat.send(message, "filehelper")
   itchat.run()