"""
演示JSON数据 和 Python字典的相互转换
"""
# 导入json模块
import json

# # 1.准备列表，其元素都是字典，将其转换为JSON
# data = [{'name': '张大山', 'age': 11}, {'name': '王大锤', 'age': 13}, {'name': '赵小虎', 'age': 16}]
# json_str = json.dumps(data, ensure_ascii=False) # 这里手动添加参数，不允许程序将中文翻译成ASCII码
# print(type(json_str))  # <class 'str'>  # 我有一个问题，这里明明输出的是一个列表，为什么类型是str???
# print(json_str)  # '[{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 13}, {"name": "赵小虎", "age": 16}]'

# # 2.准备字典，将字典转换为JSON
# d = {'name': '周杰伦', 'addr': '台北'}
# json_str1 = json.dumps(d, ensure_ascii=False)
# print(json_str1)  # '{"name": "周杰伦", "addr": "台北"}'
# print(type(json_str1))  # <class 'str'> # 这里明明输出的是一个字典，为什么类型是str？


# # 3.将JSO字符串转换为python数据类型[{k: v, k: v}, {k: v, k: v}]
# str11 = "[{'name': '张大山', 'age': 11}, {'name': '王大锤', 'age': 13}, {'name': '赵小虎', 'age': 16}]"
# list1 = json.loads(str11)
# print(list1)
# print(type(list1))
# # 这里为什么会报错？？

# # 4.将json字符串转换为python数据类型{k: v, k: v}
# s = "{'name': '周杰伦', 'addr': '台北'}"
# l1 = json.loads(s)
# print(l1)
# print(type(l1))


