

# ctrl+左键 查看模块内部函数

# # 1.使用import关键字导入time模块，使用其中的sleep功能（函数）。 # 使用功能时要带上模块名
# import time  # 导入python内置的time模块（time.py这个代码文件）
# print('hello')
# time.sleep(5)  # 通过'time.'就可以使用模块内部的所有功能（类，函数，变量）
# print('world')

# # 2.使用from关键字导入模块的具体某个功能， # 后面的代码可以直接用，不用写模块名
# # 使用from关键字导入time模块的sleep方法
# from time import sleep
# print('hello')
# sleep(5)
# print('world')

# # 3.使用* 导入模块内的所有功能。 # 后面的代码可以直接用，不用写模块名
# from time import *
# print('hello')
# sleep(5)
# print('world')

# # 4.使用as 给模块或模块内的某个功能起个别名
# import time as tt
# print('hello')
# tt.sleep(3)
# print('world')

from time import sleep as sl
print('hello')
sl(3)
print('world')