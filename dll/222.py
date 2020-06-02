# -*- encoding: utf-8 -*-
# 调试成功版本
import time
# import os
# import sys

import ctypes
from ctypes import *


dll = ctypes.windll.LoadLibrary('C:\\futurehotel\\es200601.dll')
print("dll版本号为 ： "+ str(dll.GetVersion()) )
print("数据库open:"+str(dll.OpenDatabase("","") ))
name=ctypes.c_char_p(b"gc")
roomno=ctypes.c_char_p(b"0105230")
begintime=ctypes.c_char_p(b"1912091200")
endtime=ctypes.c_char_p(b"1912101400")
cardno=ctypes.c_void_p(0)


print(roomno.value);
print(dll.WriteGuestCard2(name,bytes(1),bytes(),begintime,endtime,byref(cardno)))


print("数据库0close:"+str(dll.CloseDatabase() ))

