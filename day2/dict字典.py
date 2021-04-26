# coding = utf-8
# @Time : 2021/4/25 10:38 下午
# @Author: aoch
# @File : dict字典.py
# @SoftWare : PyCharm

info = {"age": 18, "sex": "man"}

# 直接访问不存在的会报错
# print(info["name"])

print(info.get("name"))
# 没找到可以设定默认值
print(info.get("name", "m"))
# 找到了就不会去默认值
print(info.get("age", 20))

info['age'] = 20
print(info)

# 删除键值对
del info['age']

print(info)

# 报错
# del info
#
# print(info)

# 清空值
info.clear()
print(info)


obj = {"age": 18, "sex": "man", "id": 123}
print(obj.keys())  # 列表
print(obj.values())  # 列表
print(obj.items()) # 元祖

for key in obj.keys():
    print(key)

for value in obj.values():
    print(value)

for key, value in obj.items():
    print("key=%s, value=%s" % (key, value))


myList = ["a", "b", "c", "d", "e"]
# 转换成枚举类型
print(enumerate(myList))

for i, x in enumerate(myList):
    print("i=%s, x=%s" % (i, x))