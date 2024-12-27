"""
演示使用for嵌套循环
打印九九乘法表
"""
# 通过外层循环控制行数
# 通过内层循环控制每一行的输出项

# for循环
# for i in range(1, 10):
#     for j in range(1, i+1):
          # 在内层循环中输出每一行的内容
#         print(f'{j} * {i} = {j * i}\t', end='')  # 让每个行与行的输出项都对齐，行内的每个输出都不换行
#
#     print() # 外层循环可以通过print()输出一个回车符
#

# while 循环
# i = 1
# while i < 10:#
#     j = 1
#     while j <= i:
#         print(f'{j} * {i} = {j * i}\t', end='')
#         j += 1
#     i += 1
#     print()

# for 和 while 嵌套
# for i in range(1, 10):
#
#     j = 1
#     while j <= i:
#         print(f'{j} * {i} = {j * i}\t', end='')
#         j += 1
#
#     print()

# while和for嵌套：
# i = 1
# while i < 10:
#     for j in range(1, i+1):
#         print(f'{j} * {i} = {j * i}\t', end='')
#     i += 1
#     print()
