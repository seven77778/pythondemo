# coding=utf8
import itchat
import requests
import re


# 抓取网页
def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


# 自动回复
@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing', 'Picture'])
def text_reply(msg):
    # 当消息不是由自己发出的时候 if not msg['FromUserName'] == Name["自己微信号"]:
    # 或者指定微信好友
    # qiqi is 3ef274a977034ae7a31c788660ffc510de88fe966a53082279d7bccb78425ce7
    if (msg['FromUserName'] == '@ca0b30667e9497e1ca26c2a82b68ebba' or
            msg['FromUserName'] == '@ff8aebeeae0244d863e395a13418989ce48316eafc5db349e54adcc9b11e8194'or
            msg['FromUserName'] == '@59485a1fa65fd24d1d24e62c28f6785736a972854f9c08af00f0c235a93a78e2'or
            msg['FromUserName'] == '@3ef274a977034ae7a31c788660ffc510de88fe966a53082279d7bccb78425ce7'):
        print(msg['FromUserName'])
        # 回复给好友
        tulingkey = "155dc2e0996d494fb33aa4d805e562a5"  # 注册图灵官网，申请自己的机器人
        url = "http://www.tuling123.com/openapi/api?key=%s&info=" % (tulingkey)
        url = url + msg['Text']
        html = getHtmlText(url)
        message = re.findall(r'\"text\"\:\".*?\"', html)
        reply = eval(message[0].split(':')[1])
        return reply


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    # 获取自己的UserName
    friends = itchat.get_friends(update=True)[0:]
    Name = {}
    Nic = []
    User = []
    for i in range(len(friends)):
        Nic.append(friends[i]["NickName"])
        User.append(friends[i]["UserName"])
    for i in range(len(friends)):
        Name[Nic[i]] = User[i]
    itchat.run()
