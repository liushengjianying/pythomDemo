# coding = utf-8
# @Time : 2021/4/26 10:04 下午
# @Author: aoch
# @File : 文件操作.py
# @SoftWare : PyCharm

# 打开文件，w是写入模式，文件不存在就新建
# f = open("test.txt", "w")
# f.write("I am here.")
#
# # 默认不写是r,读写模式，找不到文件就报错
# # f = open("test1.txt")
#
# # 关闭文件
# f.close()

f = open("test.txt", "r")
content = f.read(5)
print(content)
f.close()