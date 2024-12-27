"""
补充知识
"""
# # print语句不换行
# print('hello', end='')
# print('world')

# # 制表符：\t
# # 让多行字符串整齐的对齐
# print('hello world')
# print('itheima best')
#
# print('hello\tworld')
# print('itheima\tbest')
"""
演示使用while嵌套循环
印打九九乘法表
"""
# 定义外层循环的控制变量
i = 1
while i <= 9:

    # 定义内层循环的控制变量
    j = 1
    while j <= i:
        # 内层循环的print语句，不要换行.通过\t制表符进行对齐
        print(f'{j} * {i} = {j * i}\t', end='')   # 内层循环控制变量 * 外层循环控制变量
        j += 1  # 定义内层循环的退出条件
    i += 1 # 定义内层循环的退出条件
    print()  # print空内容，就是输出一个换行