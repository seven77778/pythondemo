"""
"""

from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
import datetime


# linux执行登陆请调用下面的这句
 #bot = Bot(console_qr=2,cache_path="botoo.pkl")
#获取金山词霸每日一句，英文和翻译
def get_news():
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content, note

def send_news():

   try:
     # contents = get_news()

   # 你朋友的微信备注，请注意最好你的好友备注只有1个

     # file_helper.send_msg(123)
     #my_friend = bot.file_helper

     my_friend = bot.friends().search(u'七七')[0]
     # my_friend.send(contents[0])
     # my_friend.send(contents[1])
     nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
     my_friend.send("现在是"+nowTime+u" 亲爱的，喝口水吧！!           咕嘟咕嘟咕嘟 吨吨吨~~~  enjoy 喝水的快乐 哟喂")
     # 每86400秒（1天），发送1次
     t = Timer(3600, send_news)
     t.start()

   except:

       # 你的微信名称，不是微信帐号。

        my_friend = bot.file_helper
        my_friend.send_msg(u"消息发送失败")

if __name__ == "__main__":
    bot = Bot()
    send_news()


    # print(nowTime)