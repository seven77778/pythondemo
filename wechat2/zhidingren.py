# -*- coding: utf-8 -*-

import itchat
import http.client
import json

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 监听人的微信id
touserNameId = '@28ac47c220c4e48eb42194dd842606c1af16155d6c47bcc9d68d7526864cea70'
fromuserId = '123b12a0e8a88eebf0a307298fba5155e6aabb629162889cce53b0c277cb77b7'
tulingDomain = 'openapi.tuling123.com'
tulingOpenapiUrl = 'http://' + tulingDomain + '/openapi/api/v2'
# 聊天计数
count = 0


# 监听接收到的文件信息
@itchat.msg_register(itchat.content.TEXT)
def reply_msg(msg):
    print(msg)
    # 指定好友回复特定消息
    if msg['FromUserName'] == touserNameId and msg['ToUserName'] == touserNameId:
        global count

        # 图灵机器人
        robbot0 = '155dc2e0996d494fb33aa4d805e562a5'
        # 图灵机器人1
        robbot1 = 'appkey1'
        # 图灵机器人2
        robbot2 = 'appkey2'
        # 图灵机器人3
        robbot3 = 'appkey3'
        # 图灵机器人4
        robbot4 = 'appkey4'

        count += 1
        temp = 'robbot' + str(count // 98)
        usedRobbot = robbot0
        print("收到：", msg.text)
        info = msg.text

        headers = {
            # heard部分直接通过chrome部分request header部分
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '14',  # get方式提交的数据长度，如果是post方式，转成get方式：【id=wdb&pwd=wdb】
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'http://10.1.2.151/',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36'
        }
        data = {
            "reqType": 0,
            "perception": {
                "inputText": {
                    "text": info
                },
                "selfInfo": {
                    "location": {
                        "city": "北京",
                        "province": "北京",
                        "street": "信息路"
                    }
                }
            },
            "userInfo": {
                "apiKey": usedRobbot,
                "userId": "me"
            }
        }
        # 这里是为了找到 id 包含 FromUserName 和 ToUserName
        print(data)
        conn = http.client.HTTPConnection(tulingDomain)
        header = {"Content-type": "application/json"}
        conn.request(method="POST", url=tulingOpenapiUrl, headers=header, body=json.dumps(data))
        response = conn.getresponse()
        # print(response.status)
        # print(response.reason)
        res = response.read()
        # print(res)
        resp = json.loads(res)
        # print(resp)
        # print(type(resp))

        reponseType = resp['results'][0]['values']
        print(reponseType)
        print(type(reponseType))

        # str = input("回复：")
        itchat.send(reponseType['text'], toUserName=touserNameId)


if __name__ == '__main__':
    # 退出程序以后还暂存登录状态
    itchat.auto_login(hotReload=True)

    # 给文件助手发消息
    itchat.send("文件助手你好哦", toUserName="filehelper")
    itchat.run()