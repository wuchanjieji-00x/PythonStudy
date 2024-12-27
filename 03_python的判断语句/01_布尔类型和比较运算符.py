"""
演示布尔类型的定义
以及比较运算符的应用
"""
# # 定义变量存储布尔类型的数据
# bool_1 = True
# bool_2 = False
# print(f'bool_1变量的内容是：{bool_1}, 类型是：{type(bool_1)}')
# print(f'bool_2变量的内容是：{bool_2}, 类型是：{type(bool_2)}')

# 比较运算符的使用
# ==, !=, >, <, >=, <=

# 演示进行内容的 ==, !=比较
# 数字的比较
num1 = 10
num2 = 10
print(f'10 == 10 的结果是：{num1 == num2}')

num1 = 10
num2 = 15
print(f'10 != 15的结果是：{num1 != num2}')

# 字符串的比较
name1 = 'itcast'
name2 = 'ITcast'
print(f'\'itcast\' == \'ITcast\' 的结果是：{name1 == name2}')

# 演示>, <, >=, <=
num1 = 10
num2 = 5
print(f'10 > 5 的结果是：{10 > 5}')
print(f'10 < 5 的结果是：{10 < 5}')

num1 = 10
num2 = 10
print(f'10 >= 10 的结果是：{num1 >= num2}')
print(f'10 <= 10 的结果是：{num1 <= num2}')