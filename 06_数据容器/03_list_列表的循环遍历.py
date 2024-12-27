"""
演示对list循环遍历
使用while和for循环两种方式
"""
# my_list = ['中华有神功', '宫廷玉液酒', '一百八一杯']
#
# def list_while_func():
#
#     """
#     使用while循环遍历列表的演示函数
#     :return:None
#     """
#     # 循环控制变量通过下标索引来控制，默认为0
#     # 每一次循环将下标索引变量+1
#     # 循环条件：下标索引变量 < 列表的元素数量
#
#     # 定义一个变量用来标记列表的下标
#     index = 0   # 初始值为0
#     while index < len(my_list):
#         # 通过index变量取出对应下标的元素
#         element = my_list[index]
#         print(f'列表第{index}个元素：{element}')
#
#         # 循环退出条件，至关重要，否则会进入死循环
#         index += 1
# list_while_func()

# def list_for_func():
#     """
#     使用for循环，遍历列表的演示函数
#     :return: None
#     """
#     index = 0
#     # for 临时变量 in 数据容器
#     for element in my_list:
#         index += 1
#         print(f'列表第{index}个元素：{element}')
#
# list_for_func()


# 练习
# 取出列表中的偶数
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []

# # while 循环遍历
# index = 0
# while index < len(my_list):
#     element = my_list[index]
#     if element % 2 == 0:
#         new_list.append(element)
#     index += 1
# print(new_list)

# for循环遍历

for element in my_list:
    if element % 2 == 0:
        new_list.append(element)
print(new_list)
