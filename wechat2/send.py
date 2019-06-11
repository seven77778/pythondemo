# -*- coding:UTF-8 -*-

import itchat
import sys

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

# 登录
itchat.login()
# 发送消息
itchat.send('hello', 'ZJ210314')
