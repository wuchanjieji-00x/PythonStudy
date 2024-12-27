"""
演示数据容器之：list 列表的常用操作
"""
my_list = ['itcase', 'itheima', 'python']
# 1. 查询下标索引功能
# 1.1 查找某元素在列表内的下标索引
# index = my_list.index('itheima')
# print(f'itheima在列表中的下标索引值是:{index}')
# 1.2 如果被查找的元素不存在，会报错
# index = my_list.index('hello')
# print(f'hello在列表中的下标索引值是：{index}')  # ValueError: 'hello' is not in list

# 2.修改特定下标索引的值
# my_list[0] = '中华有神功'
# print(f'修改后的列表：{my_list}')

# 3. 在指定位置插入元素
# my_list.insert(1, '中华有神功')
# print(f'插入元素后的列表{my_list}')  # ['itcase', '中华有神功', 'itheima', 'python']

# 4.在列表的尾部追加’单个‘新元素
# my_list.append('中华有神功')
# print(f'列表追加元素后：{my_list}')

# 5.在列表的尾部追加’多个‘新元素，即添加容器
# my_list2 = [1, 2, 3]
# my_list.extend(my_list2)
# print(f'列表追加多个元素后：{my_list}')

# 6. 删除指定下标索引的元素（两种方式）
# 6.1 方式1：del 列表[元素下标]  使用关键字del
# del my_list[1]
# print(f'列表删除指定下标索引的元素后: {my_list}')
# 6.2 方式2：列表.pop(下标)   使用pop方法
# delelement = my_list.pop(1)  # 获取pop的返回值，即删掉的元素
# print(f'列表删除指定下标索引的元素后: {my_list}')
# print(delelement)

# 7. 删除某元素在列表中的第一个匹配项
# my_list3 = [1, 2, 3, 1, 2, 3]
# my_list3.remove(2)
# print(f'通过remove方法删除元素后的列表：{my_list3}')# 通过remove方法删除元素后的列表：[1, 3, 1, 2, 3]
# # 结果只删除了第一个2，即所谓的只删除元素在列表中的第一个匹配项，方法结束

# 8. 清空列表
# my_list.clear()
# print(f'clear后的列表：{my_list}')  # clear后的列表：[]

# 9. 统计列表内某元素的数量
# my_list4 = [1, 2, 3, 1, 2, 3, 1]
# count = my_list4.count(1)
# print(f'列表中，1 的数量：{count}')  # 列表中，1 的数量：3

# 10. 同级列表中全部元素的数量，即列表的长度
# my_list5 = [1, 2, 3, 1, 2, 3, 1, 2, 3]
# count = len(my_list5)
# print(f'列表中，全部元素的数量是：{count}')  # 列表中，全部元素的数量是：9


# 练习
# 定义一个列表，并用变量接收
age = [21, 25, 21, 23, 22, 20]
print(age)
# 追加一个元素31到列表的尾部
age.append(31)
print(age)
# 追加一个新列表[29， 33， 30] 到列表的尾部
age.extend([29, 33, 30])  # 追加多个元素，记得要将元素作为一个嵌套列表追加进去
print(age)
# 取出第一个元素
element1 = age[0]
print(element1)
# 取出最后一个元素
element_last = age[-1]
print(element_last)
# 元素31在列表中的下标索引
index_31 = age.index(31)
print(index_31)


