# -*- coding: UTF-8 -*-

try:
    fh = open("testfile.txt", "w")
    fh.write("test!")
except IOError:
    print ("Error: ")
else:
    print ("else")
    fh.close()