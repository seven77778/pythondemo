# -*-coding:utf-8-*
# make a big fortune hhahaa
import random

list_red = [x for x in range(1,36)]        #1~35红色球序列
list_blue = [x for x in range(1,13)]       #1~12蓝色球序列

res_red = random.sample(list_red, 5)       #随机选取5个红球
res_blue = random.sample(list_blue, 2)     #随机选取2个红球

res_red.sort()                             #对选取的5个红球排序
res_blue.sort()                            #对选取的2个蓝球排序

res = res_red + res_blue
print(res)
