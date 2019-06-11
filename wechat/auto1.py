# -*- coding:UTF-8 -*-

from wxpy import *
import sys

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


bot = Bot(cache_path=True)
# bot = Bot()

# 定位公司群
found = bot.friends().search('六六')
print(bot.friends)
print(found)

@bot.register(found)
def message(msg):
    ret = "heelll"
    return ret


# 堵塞线程
embed()
