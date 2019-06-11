# -*- coding:UTF-8 -*-
import smtplib
from email.mime.text import MIMEText

mail_host = 'smtp.163.com'
mail_user = 'lisuheng345@163.com' #发送邮件的邮箱
mail_pw = 'lisuheng' #你的密码
to_addr = '522097606@qq.com'#收邮件的邮箱

message = MIMEText('阿里云-飞猪-汽车票业务线-订单预定报警','plain','utf-8')#参数1 邮件内容
message['From'] = mail_user
message['To'] = to_addr

message['Subject'] = 'test' #邮件标题

try:
    server = smtplib.SMTP(mail_host,25)
    server.starttls()
    server.set_debuglevel(1)#打印详细日志
    server.login(mail_user,mail_pw)
    server.sendmail(mail_user,[to_addr],message.as_string())
    print('success')
except smtplib.SMTPException as e:
    print('error')
    print(e)