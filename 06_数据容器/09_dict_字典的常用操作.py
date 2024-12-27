"""
演示dict字典的常用操作
"""



# # 定义一个字典
# # 注意这里定义字典的格式
# dict1 = {
#     '周': 99,
#     '吴': 88,
#     '郑': 77,
#     '王': 66
# }
# print(dict1)

# # 1.新增字典元素 ： 如果字典里要输入的key不存在，即为增加元素
# dict1['张'] = 33  # 注意这里用的是[]
# print(dict1)

# # 2.更新字典元素： 如果字典里要输入的key存在，因为相同的key会覆盖，即为增加元素
# dict1['周'] = 100
# print(dict1)

# # 3.删除元素：通过key删除value，同时key也会被删除
# # dict1.pop('王')  # 这里是删除一对键值对
# # print(dict1)
# # 这里还能拿到删除的'王的分数'
# score = dict1.pop('王') # 这里既是删除一对键值对，又是取要删除的key对应的value
# print(dict1, score)

# # 4.清空元素：clear方法
# dict1.clear()
# print(dict1)  # {}

# # 5.获取全部的key
# dict2 = {
#     '周': 99,
#     '吴': 88,
#     '郑': 77,
#     '王': 66
# }
# print(dict2)
# dict2_keys = dict2.keys()
# print(dict2_keys)  # dict_keys(['周', '吴', '郑', '王'])  注意这里的输出是个list，而且带有header的

# # 6.循环遍历字典
# dict2 = {
#     '周': 99,
#     '吴': 88,
#     '郑': 77,
#     '王': 66
# }
# print(dict2)
# dict2_keys = dict2.keys()
#
# # 方式1： 通过逐一获取到全部的key完成遍历
# for key in dict2_keys:
#     print(key, end='')
#     print(dict2[key])
#
# # 方式2：直接对字典进行for循环，每一次循环都是直接得到key
# # 注意这里直接循环字典，拿到的就是key
# for key in dict2:
#     print(2, key, end='')
#     print(dict2[key])
# # 字典没有下标，所以不可以通过while循环遍历！

# # 7.统计字典的元素数量：len()
# dict2 = {
#     '周': 99,
#     '吴': 88,
#     '郑': 77,
#     '王': 66
# }
# print(dict2)
# num = len(dict2)
# print(num)

