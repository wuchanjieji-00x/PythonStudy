"""
演示函数的多种传参方式
"""

def user_info(name, age, gender):
    print(f'姓名是：{name}, 年龄是：{age}, 性别是：{gender}')

# 1. 位置参数（默认使用形式）：函数调用时，实参要按照函数定义的顺序，依次和形参做匹配
user_info('小明', 20, '男')



# # 2. 关键字参数： ‘键-值’形式，手动将实参直接给到形参
# user_info(name='小明', age=20, gender='男')
# # 2.1 可以不按照函数定义的顺序传参：
# user_info(gender='男', name='小明', age=20)
# # 2.2 关键字参数可以和位置参数混用，但是位置参数一定要在前面
# user_info('小明', gender='男', age=20)


# # 3. 缺省参数
# # 注意：位置参数一定要在缺省参数前面
# def user_info1(name, age, gender='男'):
#     print(f'姓名是：{name}, 年龄是：{age}, 性别是：{gender}')
#
# user_info1('小明', 20) # gender参数在函数定义时是有默认值的，函数调用时不传参就使用默认值
# user_info1('小明', 20, '女')
# user_info1('小明', 20, gender='女') # 函数调用时传实参，就使用传递的实参



# 4.不定长参数

# # 4.1 不定长 - 位置不定长， *args
# *args：数量你随意，用逗号隔开就行，我会把你传来的实参保存在一个名为args的元组里
# # 不定长定义的形参会作为元组存在，接收不定长数量的实参
# def user_info2(*args):
#     print(f'{args}, {type(args)}')
#
# user_info2(1, 2, 3, '小明', '男')  # (1, 2, 3, '小明', '男'), <class 'tuple'> # 不定长位置参数作为元组传参

# 4.2 不定长 - 关键字不定长， **kwargs
# **kwargs：数量也随意，但元素形式一定是键值对(k-v)，我会把你传来的实参都保存在名为kwargs的字典里
# 不定长定义的形参会作为字典存在，接收不定长数量的实参（key-value）
def user_info3(**kwargs):
    print(f'{kwargs}, {type(kwargs)}')

user_info3(name='小明', age=20, gender='男', addr='上海')
# {'name': '小明', 'age': 20, 'gender': '男', 'addr': '上海'}, <class 'dict'>
