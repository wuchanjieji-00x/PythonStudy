"""
演示对序列进行切片操作
"""

# # 1.对list进行切片，从1开始，4结束，步长1
# L = [0, 1, 2, 3, 4, 5, 6]
# result1 = L[1:4]  # 步长默认是1，所以可以省略不写
# print(result1)

# # 2.对tuple进行切片
# T = (0, 1, 2, 3, 4, 5, 6)
# result2 = T[:]  # 起始和结束不写，表示从头到尾切片，步长为1可以省略
# print(result2)

# # 3.对str进行切片
# str1 = '0123456'
# result3 = str1[::2]  # 从头到尾切片，步长为2
# print(result3)

# # 反向切片
# # 4.对list反向切片
# L1 = [0, 1, 2, 3, 4, 5, 6]
# result4 = L1[::-1]  # -1不能省略
# print(result4)

# # 5.对tuple反向切片
# T1 = (0, 1, 2, 3, 4, 5, 6)
# result5 = T1[3:1:-1]  # 这里的序号还是正着数的
# print(result5) # (3, 2)

# # 6.对str进行反向切片
# str2 = '0123456'
# result6 = str2[4:2:-2]
# print(result6)   # 4



# 练习
# 请使用任何方式，得到'黑马程序员'
str1 = '月过万薪,员序程马黑来,nohtyP学'

# 方式1：
# # 倒序字符串，切片取出
# str2 = str1[::-1]
# print(str2)  # 学Python,来黑马程序员,薪万过月
# # print(str2.index('黑'))
# str3 = str2[9:14] # 注意是从0开始计数
# print(str3)

# 教程
print(str1[::-1][9:14])

# #或 切片取出，再倒序字符串
# str4 = str1[5:10]
# print(str4)
# str5 = str4[::-1]
# print(str5)

# 教程
print(str1[5:10][::-1])



# # 方式2：
# # slit分割’，‘，replace替换'来'为空，倒序字符串
# L6 = str1.split(',')
# print(L6)    # L6 是个列表，但是列表里的元素都是字符串，不能被更改  # ['月过万薪', '员序程马黑来', 'nohtyP学']
# # L6[1][5] = 5 # TypeError: 'str' object does not support item assignment
# str6 = L6[1]
# # print(type(str6))
# print(str6)
# str7 = str6.replace('来', '')
# print(str7)
# str8 = str7[::-1]
# print(str8)

# 教程
print(str1.split(',')[1].replace('来', '')[::-1])







