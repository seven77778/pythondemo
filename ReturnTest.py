# coding=utf-8
# 通过java Runtime.getRuntime().exec() 执行脚本，返回给java 为 print()中内容
print('return test ?? wh')

# python方法 声明类需要两空行


class Py(object):
    def _test_(self):
        return 'test1'

    def my_method(self, x):
        return x


a = Py()
print(a._test_())
print(a.my_method(44))  # 带参数方法


def add(c, b):
    return c+b


print(add(2, 3))

# java调用add是可以的，在类中的不行，方法还不对
