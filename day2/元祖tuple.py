# coding = utf-8
# @Time : 2021/4/25 10:27 下午
# @Author: aoch
# @File : 元祖tuple.py
# @SoftWare : PyCharm


tup = (50)
print(type(tup))

tup1 = (50, )
print(type(tup1))

tup3 = (10, 20, 30, 40)
print(tup3[0])
print(tup3[-1])
print(tup3[1:3])

# 可以增加
tup4 = (50, 60)
tup5 = tup3 + tup3
print(tup5)

# 不可以改
# tup3[0] = "a"

# 删除
# 直接删除了tup3这个变量 报错
# del tup3
# print(tup3)