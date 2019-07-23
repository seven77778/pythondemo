import cv2
import smtplib
import sys
import os
import time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtpserver  = 'smtp.163.com'         # smtp服务器
username    = 'lisuheng345@163.com'    # 发件邮箱账号
password    = 'lisuheng'            # 邮箱登录密码
sender      = 'lisuheng345@163.com'    # 发件人
addressee   = '522097606@qq.com'     # 收件人
exit_count  = 5                      # 尝试联网次数
path        = os.getcwd()            #获取图片保存路径

# photo
def getPicture():
    cap = cv2.VideoCapture(0)
    ret, img = cap.read()
    cv2.imwrite('person.jpg', img)
    if img is None:
        print("camera error")
    else:
        print("camera success")
    # 关闭摄像头
    cap.release()


def setMsg():
    # 下面依次为邮件类型，主题，发件人和收件人。
    msg = MIMEMultipart('mixed')
    msg['Subject'] = '电脑已经启动'
    msg['From'] = '88888888888@163.com <88888888888@163.com>'
    msg['To'] = addressee

    # 下面为邮件的正文
    text = "你的电脑已经开机！照片如下！"
    text_plain = MIMEText(text, 'plain', 'utf-8')
    msg.attach(text_plain)

    # 构造图片链接
    sendimagefile = open(path+'/person.jpg', 'rb').read()
    image = MIMEImage(sendimagefile)
    # 下面一句将收件人看到的附件照片名称改为people.png。
    image["Content-Disposition"] = 'attachment; filename="people.png"'
    msg.attach(image)
    return msg.as_string()

def sendEmail(msg):
    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(username, password)
    smtp.sendmail(sender, addressee, msg)
    smtp.quit()

# 判断网络是否联通,成功返回0，不成功返回1
# linux中ping命令不会自动停止，需要加入参数 -c 4，表示在发送指定数目的包后停止。
def isLink():
    return os.system('ping -c 4 www.baidu.com')
    # return os.system('ping www.baidu.com')

def main():
    print("123")
    getPicture()
    msg = setMsg()
    sendEmail(msg)
    print("end")
    # reconnect_times = 0
    # while isLink():
    #     time.sleep(10)
    #     reconnect_times += 1
    #     if reconnect_times == exit_count:
    #         sys.exit()

if __name__ == '__main__':
    main()