# -*- encoding: utf-8 -*-
import clr

# 测试 C# dll
# clr not clr ,install pythonnet

# CSharpClassLibraryForJava 是 namespace
from CSharpClassLibraryForJava import *
# Class1 是 public class
instance = Class1()
print("start")
print(instance.getstr())
print(instance.add(12,15))
print("end")