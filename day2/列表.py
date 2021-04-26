# coding = utf-8
# @Time : 2021/4/25 9:32 下午
# @Author: aoch
# @File : 列表.py
# @SoftWare : PyCharm

# a = [1, 3]
# b = [2, 4]
# a.append(b)
# print(a)
# a.extend(b)
# print(a)
#
# c = [1, 2, "ring", 3, "ring", 4]
# c.insert(1, 3)
# del c[0]
# c.pop()
# c.remove("ring")  # 直接删除指定内容的元素,只删除第一个匹配的
# c[1] = "gold"
# print(c)

# nameList = ["小张", "小王", "小李"]
# nameTemp = input("请输入")
# nameList.append(nameTemp)
#
# for name in nameList:
#     print(name)


# find_name = input("输入")
# list = [1, "小张", 4]
# if find_name in list:
#     print("找到了")
# else:
#     print("没找到")

# abc = ["a", "b", "c", "d", "e"]
# # 范围区间左闭右开，不包含4
# print(abc.index("b", 1, 4))
# # 计数
# print(abc.count("B"))
# abc.reverse()
# print(abc)
# abc.sort()  # 默认升序
# print(abc)
# abc.sort(reverse=True)  # 降序
# print(abc)

import random
offices = [[], [], []]
names = ["a", "b", "c", "d", "e", "f", "g", "h"]

for name in names:
    index = random.randint(0, 2)
    offices[index].append(name)

i = 1
for office in offices:
    print("办公室%d的人数为%d" % (i, len(office)))
    i += 1
    for name in office:
        print(name, end="\t")
    print("\n")
    print("-" * 20)