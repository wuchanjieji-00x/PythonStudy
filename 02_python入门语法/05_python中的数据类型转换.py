# 将数字类型转换为字符串
num_str = str(11)
print(type(num_str), num_str)  # <class 'str'> 11

float_str = str(11.345)
print(type(float_str), float_str)  # <class 'str'> 11.345
# 我们只转换数据的类型，而不破坏数据的内容


# 将字符串转换成数字
num1 = int('11.345')
print(type(num1), num1)   # <class 'int'> 11

num2 = float('11.345')
print(type(num2), num2)  # <class 'float'> 11.345

# 这是一个错误示例，想要将字符串转换为int类型，那么字符串的内容必须是整数
num3 = int('11.345')
print(type(num3), num3)

# 错误示例，想要将字符串转换成数字，必须要求字符串内的内容都是数字
# num3 = int('黑马程序员')
# print(type(num3), num3)


# 整数转浮点数
float_num = float(11)
print(type(float_num), float_num)  # <class 'float'> 11.0

# 浮点数转整数
int_num = int(11.345)
int_num1 = int(11.999)
print(type(int_num), int_num)  # <class 'int'> 11
print(type(int_num1), int_num1)  # <class 'int'> 11

# 浮点数转整数会丢失精度，会把小数点后的数字全部丢掉