"""
演示数据容器：set 集合的使用
"""
# 定义集合
# 集合是不允许重复，且 无序的
# S1 = {3, 2, 3, 'hello', True, 3, 'hello', True}
# S2 = set()
# print(S1, type(S1))  # {True, 2, 3, 'hello'} <class 'set'>
# print(S2, type(S2))  # set() <class 'set'>

# # 神奇之处
# S1 = {1, 2, 3, 'hello', True, 3, 'hello', True}
# print(S1, type(S1))  # {'hello', 1, 2, 3} <class 'set'>
# # 为什么字符串开头是1的时候，布尔量不能输出了？？？

# # 添加新元素
# S1 = {3, 2, 3, 'hello', True, 3, 'hello', True}
# S1.add('python')
# S1.add(3)
# print(S1)  # {True, 2, 3, 'python', 'hello'}

# # 移除元素
# S1 = {3, 2, 3, 'hello', True, 3, 'hello', True}
# S1.remove(3)
# print(S1)  # {True, 2, 'hello'}

# # 随机取一个元素
# S1 = {3, 2, 1, 'hello', True}
# element = S1.pop()
# print(element)  # 1
# print(S1) # {2, 3, 'hello'}

# # 清空集合
# S1 = {3, 2, 1, 'hello', True}
# S1.clear()
# print(S1)  # set()  # 空集合

# # 取两个set的差集
# S1 = {1, 2, 3}
# S2 = {1, 5, 6}
# S3 = S1.difference(S2)  #可理解为S1较S2而言，有什么不同之处？ 也就是说，哪些元素S1有，而S2是没有的
# print(S3)  # {2, 3}
# print(S2)  # {1, 5, 6}
# print(S1)  # {1, 2, 3}

# # 消除两个set的差集:
# S1 = {1, 2, 3}
# S2 = {1, 5, 6}
# S1.difference_update(S2) # 在S1中消除和S2的交集
# print(S1)  # {2, 3}
# print(S2)  # {1, 5, 6}

# # 合并两个set
# S1 = {1, 2, 3}
# S2 = {1, 5, 6}
# S3 = S1.union(S2) # 取两个集合的并集，不改变原集合
# print(S3)  # {1, 2, 3, 5, 6}
# print(S2)  # {1, 5, 6}
# print(S1)  # {1, 2, 3}

# # 统计集合元素数量
# S1 = {1, 2, 3}
# S2 = {1, 2, 3, 1, 2, 3}
# length1 =len(S1)
# length2 =len(S2)
# print(length1) # 3
# print(length2) # 3


# # 集合的遍历
#
# # while循环：集合不支持下标索引，所以不能用while循环遍历set
#
# # for 循环
# S1 = {1, 2, 3}
# S2 = {1, 2, 3, 1, 2, 3}
# for element in S1:
#     print(element) # 1 2 3
# for element in S2:
#     print(element) # 1 2 3



# 练习
my_list = ['黑马程序员', '传播止咳', '黑马程序员', '传播止咳', 'itheima', 'itcast', 'itheima', 'itcast', 'best']

S1 = set()

for element in my_list:
    S1.add(element)

print(S1)
