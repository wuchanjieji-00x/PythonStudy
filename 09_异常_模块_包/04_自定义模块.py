

# 首先在当前文件目录下创建一个自定义模块，my_module1

# # 1.导入自定义模块
# # import my_module1
# # my_module1.calculate(1, 2)  # 3
#
# from my_module1 import calculate
# calculate(1, 2)  # 3

# # 2. 导入不同模块的同名功能
# from my_module1 import calculate  # 这个变灰了，说明没有被使用
# from my_module2 import calculate
# calculate(1, 1) # 0  # 使用的是最后导入的模块的方法

# 3. main+回车
from my_module1 import calculate
# 这里运行就打印出3了，说明把自定义模块文件中的测试代码也运行了，需要在自定义模块文件里做处理

# 4.__all__ = [函数名]
# # 当自定义模块文件中，没有__all__ = [函数名]，则默认自定义模块中的所有函数都能够调用
# from my_module1 import *
# calculate(1, 1)
# calculate1(1, 1)

# # 当自定义模块文件中，有__all__ = [函数名]，则你只能调用__all__() 括号中的函数
# from my_module1 import *
# calculate(1, 1)
# calculate1(1, 1)  # NameError: name 'calculate1' is not defined. Did you mean: 'calculate'?

# # 但是你不采用'*'这个字符的话， 手动导入自定义模块的函数是允许的
# from my_module1 import calculate1
# calculate1(1, 1)  # 0
