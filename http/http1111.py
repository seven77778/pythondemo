# # -.- coding:utf-8 -.-
#
# import socket
# import time
# from ctypes import *
#
# import os
# path1=os.path.abspath('.\\dll')   # 表示当前所处的文件夹的绝对路径
# print(path1)
# # 初始化socket
# s = socket.socket()
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(("", 8000))
# server_socket.listen(120)
# # 获取主机名, 也可以使用localhost
# #host = socket.gethostname()
# host = "localhost"
# # 默认的http协议端口号
# port = 81
#
# # 绑定服务器socket的ip和端口号
# s.bind((host, port))
#
# # 服务器名字/版本号
# server_name = "Python-DLL"
#
# #f = open("index.html")
# #content = f.read()
# #print content
#
# # 可同时连接五个客户端
# s.listen(5)
#
# # 提示信息
# print ("You can see a HelloWorld from this server in ur browser, type in", host, "\r\n")
# # dll = cdll.LoadLibrary('ProjectForJava.dll')
# # print( dll.add(1, 2))
#
#
# # 服务器循环
# while True:
#     # 等待客户端连接
#     client_socket, client_address = server_socket.accept()
#     # 显示请求信息
#     print ("--Request Header:")
#     # 接收浏览器的请求, 不作处理
#     request_data = client_socket.recv(1024)
#     print("request data:", request_data)
#     # 获得请求的时间
#     # 相应头文件和内容
#     response ="123"
#     # 发送回应
#     # c.send(response)
#     client_socket.send(bytes(response, "utf-8"))
#
#     # 关闭客户端连接
#     client_socket.close()
#
#     print ("success")
#     print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
#
