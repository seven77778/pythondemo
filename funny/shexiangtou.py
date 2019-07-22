import itchat
import os
import cv2

# pip install opencv-python

# 注册消息响应事件，消息类型为itchat.content.TEXT，即文本消息
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
   print(msg)
   global flag
   # 发送内容
   message = msg['Text']
   # 接收者
   toName = msg['ToUserName']
   if toName == "filehelper":
       if message == "pic":
           # 0代表内置摄像头 1、2...为外界是
           cap = cv2.VideoCapture(0)
           ret, img = cap.read()
           cv2.imwrite("pic.jpg", img)
           # 将图片发送至文件传输助手
           itchat.send('@img@%s' % u'pic.jpg', 'filehelper')
           # 释放摄像头
           cap.release()
       if message[0:3] == "cmd":
           # 执行输入的命令
           os.system(message.strip(message[0:4]))


if __name__ == '__main__':
   message ="使用说明： 1.输入[cmd xxx] 执行命令。 2 .输入pic 打开摄像头"
   """
   在auto_login()里面提供一个True，即hotReload=True
   即可保留登陆状态
   即使程序关闭，一定时间内重新开启也可以不用重新扫码
   """
   itchat.auto_login(True)
   itchat.send(message, "filehelper")
   itchat.run()