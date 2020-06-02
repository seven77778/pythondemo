    # -*- encoding: utf-8 -*-
# 测试 C++ dll

# import os
# import sys
from ctypes import *


dll = windll.LoadLibrary('xxx.dll')
print("dll版本号为 ： "+ str(dll.GetVersion()) )
print("test")
# ValueError: Procedure called with not enough arguments (8 bytes missing) or wrong calling convention
#
print(dll.OpenDatabase("","") )
print(dll.WriteGuestCard2("lsh",bytes("0".encode("utf-8")),"8505","1912021200","","0"))


def version():
    return str(dll.GetVersion());



