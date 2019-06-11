# coding=utf8
import itchat

itchat.auto_login(hotReload=True)

# 想给谁发信息，先查找到这个朋友,name后填微信备注即可,deepin测试成功
users = itchat.search_friends(name='')
# 获取好友全部信息,返回一个列表,列表内是一个字典
print(users)

#coding=utf8
import itchat
itchat.auto_login(hotReload=True)
#获取所有好友信息
account=itchat.get_friends()
print(account)
# #获取自己的UserName
userName = account[0]['UserName']

print('myname '+userName)