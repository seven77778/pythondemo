# -*- encoding: utf-8 -*-
# 测试 C++ dll

import os
import sys
from ctypes import *

dll = cdll.LoadLibrary('ProjectForJava.dll')
print dll.add(1, 2)

# C++代码中 要有 extern "C"  __declspec(dllexport)   int add(int x,int y);
# DllForJava.dll 运行失败

dll2 = cdll.LoadLibrary('DllForJava.dll')
print(dll2.add(1, 2))
# AttributeError: function 'add' not found
