"""
演示数据容器：dict 字典 的定义
"""

# # 定义字典
# dict1 = {'周': 99, '吴': 88, '郑': 77, '王': 66}
# print(dict1, type(dict1))
# # 定义空字典
# dict2 = {}
# dict3 = dict() # 这里用的是小括号，因为dict是类，这里是创建一个实例，所以用小括号
# print(dict2, type(dict2))
# print(dict3, type(dict3))

# # 定义重复的key
# dict4 = {'周': 99, '吴': 88, '郑': 77, '周': 66}
# print(dict4) # {'周': 66, '吴': 88, '郑': 77}
# # 字典里不允许有重复的key出现，如果出现，则后面的key会覆盖掉前面的key

# # 从字典中基于key获取value（类似于查字典）
# dict5 = {'周': 99, '吴': 88, '郑': 77, '王': 66}
#
# score = dict5['周']
# print(score)  # 99
#
# score = dict5['王']
# print(score)  # 66

# 定义嵌套字典   # list/uple/dict/set 中回车符完全没有影响，元素之间的分割完全看逗号
stu_score_dict = {
    '王': {
        '语文': 77,
        '数学': 66,
        '英语': 33
    },
    '周': {
        '语文': 88,
        '数学': 86,
        '英语': 55
    },
    '林': {
        '语文': 88,
        '数学': 86,
        '英语': 55
    }
}  # 注意这种嵌套字典的格式
print(stu_score_dict)

# 从嵌套字典中获取信息
score = stu_score_dict['周']['语文']
print(f'周的语文成绩是：{score}')

score = stu_score_dict['林']['英语']
print(f'林的英语成绩是：{score}')
