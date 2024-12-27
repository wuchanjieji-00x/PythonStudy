"""
演示tuple元组的定义和操作
"""

# 定义元组
# t1 = (1, 'hello', True)
# t2 = ()
# t3 = tuple() # 通过关键字定义，这实际定义了一个类对象
# print(f't1的类型是：{type(t1)}，内容是{t1}')
# print(f't2的类型是：{type(t2)}，内容是{t2}')
# print(f't3的类型是：{type(t3)}，内容是{t3}')

# 定义单个元素的元组，末尾要记得加个逗号
# t4 = ('hello')
# print(f't4的类型是：{type(t4)}，内容是{t4}')  # t4的类型是：<class 'str'>，内容是hello
# t5 = ('hello', )
# print(f't5的类型是：{type(t5)}，内容是{t5}')  # t5的类型是：<class 'tuple'>，内容是('hello',)

# 元组的嵌套
# t6 = ((1, 2, 3), (4, 5, 6))
# print(f't6的类型是：{type(t6)}，内容是{t6}')
# # 下标索引取数据
# print(t6[1][2])  # 注意，这里用的是中括号。写法和list一致



# 1.tuple的操作：index查找方法：查询元素下标
# t7 = ('中华有神功', '宫廷玉液酒', '一百八一杯')
# index = t7.index('宫廷玉液酒')
# print(f't7元组中，"宫廷玉液酒"的index是：{index}')

# 2.tuple的操作：count统计方法：统计某个元素的数量
# t8 = ('中华有神功', '宫廷玉液酒', '宫廷玉液酒', '宫廷玉液酒', '一百八一杯')
# count = t8.count('宫廷玉液酒')
# print(f't7元组中，"宫廷玉液酒"的count是：{count}个')

# 3.tuple的操作：len函数：统计元组的元素数量或者是统计元组的长度   # 注意，这里叫做len函数，而不是len方法，因为len函数不属于tuple类
# t8 = ('中华有神功', '宫廷玉液酒', '宫廷玉液酒', '宫廷玉液酒', '一百八一杯')
# length = len(t8)
# print(f't8元组中的元素数量是：{length}')


# 4.tuple的循环遍历
# t9 = ('中华有神功', '宫廷玉液酒', '一百八一杯')

# # while循环遍历
# index = 0
# while index < len(t9):
#     element = t9[index]  # 注意这里用的是中括号，和list一致
#     print(f't9中，第{index}个元素：{element}')
#
#     index += 1

# # for循环遍历
# index = 1
# for element in t9:
#     print(f't9中，第{index}个元素：{element}')
#     index += 1



# 5.元组的内容是不可修改的，否则报错！！！
# t9 = ('中华有神功', '宫廷玉液酒', '一百八一杯')
# t9[1] = '你竟然不知道价格'
# print(t9)  # TypeError: 'tuple' object does not support item assignment

# 但是，如果tuple里面有list的话，list是可以被修改的
# t10 = (1, 2, 3, [4, 5, 6])
# t10[3][1] = 100
# print(t10)  # (1, 2, 3, [4, 100, 6])



# 练习
jay_zhou = ('周杰伦', 11, ['football', 'music'])

index = jay_zhou.index(11)
print(index)
name = jay_zhou[0]
print(name)
del jay_zhou[2][0]
print(jay_zhou)

