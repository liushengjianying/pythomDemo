# coding = utf-8
# @Time : 2021/4/26 9:37 下午
# @Author: aoch
# @File : def函数.py
# @SoftWare : PyCharm


def divide(a, b):
    shang = a // b
    yushu = a % b
    return shang, yushu


sh, yu = divide(5, 2)
print(sh, yu)

a = 100


#
#
# def test1():
#     a = 200
#     print(a)
#     a = 300
#     print(a)
#
#
# def test2():
#     print(a)
#
#
# test1()
# test2()


def test1():
    global a
    print(a)
    a = 300
    print(a)


def test2():
    print(a)


test1()
test2()
