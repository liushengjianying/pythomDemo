# coding = utf-8
# @Time : 2021/4/24 1:46 下午
# @Author: aoch
# @File : demo4.py
# @SoftWare : PyCharm

'''
for i in range(5):
    print(i)

# 类似JS for(let i = 0; i < 10; i = i+3)
for i in range(0, 10, 3):
    print(i)

for i in range(-10, -100, -30):
    print(i)

name = "chengdu"
for i in name:
    print(i, end="\t")

arr = ["aa", "bb", "cc", "dd"]
for i in range(len(arr)):
    print(i, arr[i])
'''

# i = 0
# while i < 5:
#     print("第%d次" % (i+1))
#     i += 1
#
#
# sum = 0
# x = 0
# while x < 100:
#     x += 1
#     sum += x
#
# print(sum)

# count = 0
# while count < 5:
#     print(count, "小于5")
#     count += 1
# else:
#     print(count, "大于等于5")

i = 0
while i < 10:
    i += 1
    print("-"*30)
    if i == 5:
        continue
        # break
    print(i)