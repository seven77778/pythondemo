print("this my first python demo on github")

import clr

# the sample method invoke C# dll
# clr not clr ,it is pythonnet

from HotelLockDll import *
clr.FindAssembly("HotelLockDll.dll")
instance = HotelLockDll()
print("start")
print(instance.Initialize())
print(instance.Read_Card("316091"))
print(instance.Write_Card("316091", "Li", "10301", "0100", "2019-03-26 22:34:00", "2019-03-27 15:34:00"))
print("end")