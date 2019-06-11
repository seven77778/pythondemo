# -*- coding: utf-8 -*-
import json
import requests
from wxpy import *


# 调用图灵机器人API，发送消息并获得机器人的回复
from wxpy.api.chats import mp


def auto_reply(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "你的api key"
    payload = {
        "key": api_key,
        "info": text,
        "userid": "123456"
    }
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    return "[tuling] " + result["text"]


bot = Bot(console_qr=True, cache_path=True)


@bot.register(mp)
def forward_message(msg):
    return auto_reply(msg.text)


embed()