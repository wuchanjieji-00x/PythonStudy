"""
演示数据容器之：list 列表
语法：[元素1， 元素2，...]
"""

# 定义一个列表 list
# my_list = ['itheima', 'itcast', 'python']
# print(my_list)
# print(type(my_list))

# 定义一个列表，元素类型不同
# my_list = ['itheima', 666, True]
# print(my_list)
# print(type(my_list))

# 定义一个嵌套的列表
# my_list = [[1, 2, 3], [4, 5, 6]]
# print(my_list)
# print(type(my_list))

# 通过下标索引取出对应位置的数据
# my_list = ['Tom', 'Lily', 'Rose']
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])  # IndexError: list index out of range


# 通过下表索引取出数据（倒序）
# my_list = ['Tom', 'Lily', 'Rose']
# print(my_list[-1])
# print(my_list[-2])
# print(my_list[-3])

# 取出嵌套列表的元素
my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list[0][0])
print(my_list[0][1])
print(my_list[0][2])
print(my_list[1][0])
print(my_list[1][1])
print(my_list[1][2])

print(my_list[-1][-1])
print(my_list[-1][-2])
print(my_list[-1][-3])
print(my_list[-2][-1])
print(my_list[-2][-2])
print(my_list[-2][-3])
