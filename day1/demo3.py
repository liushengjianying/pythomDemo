# coding = utf-8
# @Time : 2021/4/24 1:22 下午
# @Author: aoch
# @File : demo3.py
# @SoftWare : PyCharm

import random
x = random.randint(0, 2)
print(x)
# if True:
if 0:
    print('true')
else:
    print('false')


score = int(input("请输入成绩:"))

if 90 <= score <= 100:
    print("优秀")
elif 80 <= score < 90:
    print("B")
else:
    print("c")

