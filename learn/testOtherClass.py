# 引用其他py的类 todo
# ValueError: attempted relative import beyond top-level package
import sys,os
sys.path.append(os.path.dirname(__file__) + os.sep + '../')

from . myfile import get

get()

