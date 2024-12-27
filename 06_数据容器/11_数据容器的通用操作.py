"""
演示数据容器的通用操作
"""

# # 定义五类数据容器
# my_list = [1, 2, 3, 4, 5]
# my_tuple = (1, 2, 3, 4, 5)
# my_str = 'abcdefg'
# my_set = {1, 2, 3, 4, 5}
# my_dict = {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5, }

# # 1.len(数据容器) : 统计数据容器内的元素数量
# print(len(my_list))
# print(len(my_tuple))
# print(len(my_str))
# print(len(my_set))
# print(len(my_dict))



# # 2.max(数据容器)：获取最大元素
# print(max(my_list))
# print(max(my_tuple))
# print(max(my_str))  # 字符串怎么比较大小？
# print(max(my_set))
# print(max(my_dict)) # dict找max值时，只关心key，不关心value



# # 3.min(数据容器)：获取最小元素
# print(min(my_list))
# print(min(my_tuple))
# print(min(my_str))  # 字符串怎么比较大小？
# print(min(my_set))
# print(min(my_dict)) # dict找max值时，只关心key，不关心value



# 4.容器类型转换：
# # 4.1.list(数据容器)：容器转列表
# print(list(my_list))
# print(list(my_tuple))
# print(list(my_str))   # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(list(my_set))
# print(list(my_dict))  # ['key1', 'key2', 'key3', 'key4', 'key5']

# # 4.2.tuple(数据容器)：容器转元组
# print(tuple(my_list))
# print(tuple(my_tuple))
# print(tuple(my_str))   # ('a', 'b', 'c', 'd', 'e', 'f', 'g')
# print(tuple(my_set))
# print(tuple(my_dict))  # ('key1', 'key2', 'key3', 'key4', 'key5')

# # 4.3.str(数据容器)：容器转字符串
# print(str(my_list))  # '[1, 2, 3, 4, 5]'
# print(str(my_tuple)) # '(1, 2, 3, 4, 5)'
# print(str(my_str))   # 'abcdefg'
# print(str(my_set))   # '{1, 2, 3, 4, 5}'
# print(str(my_dict))  # '{'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5}'

# # 4.4.set(数据容器)：容器转字集合
# print(set(my_list))  # {1, 2, 3, 4, 5}
# print(set(my_tuple)) # {1, 2, 3, 4, 5}
# print(set(my_str))   # {'b', 'd', 'g', 'f', 'c', 'a', 'e'}
# print(set(my_set))   # {1, 2, 3, 4, 5}
# print(set(my_dict))  # {'key1', 'key2', 'key4', 'key5', 'key3'}



# 5.数据容器的排序：将容器元素排序，然后放入list中输出
# 注意：排序之后的结果全部都是list
# 定义五类数据容器
my_list = [2, 3, 1, 4, 5]
my_tuple = (3, 1, 5, 4, 2)
my_str = 'cedfagb'
my_set = {5, 1, 4, 3, 2}
my_dict = {'key4': 1, 'key2': 2, 'key5': 3, 'key1': 4, 'key3': 5, }
# 正序排序/升序排序，reverse默认参数为False
print(sorted(my_list), type(sorted(my_list)))   # [1, 2, 3, 4, 5] <class 'list'>
print(sorted(my_tuple), type(sorted(my_tuple))) # [1, 2, 3, 4, 5] <class 'list'>
print(sorted(my_str), type(sorted(my_str)))     # ['a', 'b', 'c', 'd', 'e', 'f', 'g'] <class 'list'>
print(sorted(my_set), type(sorted(my_set)))     # [1, 2, 3, 4, 5] <class 'list'>
print(sorted(my_dict), type(sorted(my_dict)))   # ['key1', 'key2', 'key3', 'key4', 'key5'] <class 'list'>
# 倒序排序/降序排序
print(sorted(my_list, reverse=True), type(sorted(my_list)))   # [5, 4, 3, 2, 1] <class 'list'>
print(sorted(my_tuple, reverse=True), type(sorted(my_tuple))) # [5, 4, 3, 2, 1] <class 'list'>
print(sorted(my_str, reverse=True), type(sorted(my_str)))     # ['g', 'f', 'e', 'd', 'c', 'b', 'a'] <class 'list'>
print(sorted(my_set, reverse=True), type(sorted(my_set)))     # [5, 4, 3, 2, 1] <class 'list'>
print(sorted(my_dict, reverse=True), type(sorted(my_dict)))   # ['key5', 'key4', 'key3', 'key2', 'key1'] <class 'list'>

