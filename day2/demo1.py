# coding = utf-8
# @Time : 2021/4/25 8:42 下午
# @Author: aoch
# @File : demo1.py
# @SoftWare : PyCharm

# word = '单词'
# sentence = "这是一个句子！"
# paragraph = '''
#     段落
#     换行
#     展示
# '''
# print(word)
# print(sentence)
# print(paragraph)

# my_str = "I'm a student"
# 用单引号的时候要转义
# my_str2 = 'I\'m a student'
# my_str3 = "you say \"I like you\""
#
# print(my_str)
# print(my_str2)
# print(my_str3)

str = "chengdu"
# [起始位置：结束位置：步进值]
print(str[0])
print(str[0:5])
print(str[1:7:2])
print(str[:5])
print(str[5:])
print(str + ",你好")
print((str + "\t") * 3)

print("chengdu\nnihao")
# r让转义字符失效
print(r"chengdu\nnihao")
