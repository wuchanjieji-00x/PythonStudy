"""
演示以数据容器的角度，学习字符串的操作
"""

# 1.定义一个字符串
# str1 = 'abcdefg hijk lmn'

# 2.通过下标索引取元素
# value1 = str1[8]
# value2 = str1[-8]
# print(value1, value2)

# 3.字符串也是一个无法修改的数据容器
# str1[8] = 'H'   # TypeError: 'str' object does not support item assignment

# # 4.字符串的操作
# # 4.1 index方法
# str2 = 'Bulid Your Dream'
# value3 = str2.index('Your')
# print(value3)  # 6  # 输出的是字符起始下标

# # 4.2 replace方法
# str3 = 'Bulid Your Dream'
# str4 = str3.replace('u', '比亚迪')
# print(str4)  # B比亚迪lid Yo比亚迪r Dream
# # 注意，str3是只读的，不能修改，我们实际上得到的是一个新的字符串，str4

# # 4.3 split方法
# str5 = 'Bulid Your Dream'
# str6 = str5.split(' ')
# print(f'将字符串{str5}按照"空格"进行split分割后得到：{str6}，其类型是：{type(str6)}')
# # 将字符串Bulid Your Dream按照"空格"进行split分割后得到：['Bulid', 'Your', 'Dream']，其类型是：<class 'list'>
# str7 = str5.split('u')
# print(f'将字符串{str5}按照"u"进行split分割后得到：{str7}，其类型是：{type(str7)}')
# # 将字符串Bulid Your Dream按照"u"进行split分割后得到：['B', 'lid Yo', 'r Dream']，其类型是：<class 'list'>

# # 4.4 strip方法：删除字符串的首尾空格和换行符
# str8 = '   Bulid Your Dream   '
# str9 = str8.strip() # 不传入参数，默认值是空格。即删除字符串的首尾空格和换行符
# print(f'字符串{str8}被strip()后，结果是：{str9}')  # strip函数默认值是删除字符串首尾的空格
# # 字符串   Bulid Your Dream   被strip()后，结果是：Bulid Your Dream

# str10 = '123Bulid Your Dream321'
# str11 = str10.strip('123')  # 注意，这里删除的”123“其实是”1“”2“”3“三个子字符串，遇到就删掉
# print(f'字符串{str10}被strip("123")后，结果是：{str11}')
# # 字符串123Bulid Your Dream321被strip("123")后，结果是：Bulid Your Dream

# # 那为什么字符串前面有空格就不能删除呢???
# str10 = '   123Bulid Your Dream321    '
# str11 = str10.strip('123')
# print(f'字符串{str10}被strip("123")后，结果是：{str11}')
# # 字符串   123Bulid Your Dream321   被strip("123")后，结果是：   123Bulid Your Dream321


# # 4.5 count方法：统计字符串中某字符串的出现次数
# str2 = 'Bulid Your Dream'
# count = str2.count('u')
# print(count)  # 2


# # 4.6 len()函数：统计字符串的长度（包括空格）
# str2 = 'Bulid Your Dream'
# length = len(str2)
# print(length)  # 16


# # 练习
# str_n = 'itheima itcast boxuegu'
#
# count = str_n.count('it')
# print(f'字符串{str_n}中有{count}个"it"字符')
#
# str_n1 = str_n.replace(' ', '|')
# print(f'字符串{str_n},空格被替换后，结果：{str_n1}')
#
# str_n2 = str_n1.split('|')
# print(f'字符串{str_n1},按照"|"分割后，结果：{str_n2}')


