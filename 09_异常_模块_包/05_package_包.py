


# 创建一个自定义包

# 在包里面创建两个自定义模块

# 导入自定义包中的自定义模块
# 方式1：有问题
# import my_package.my_module4
# import my_package.my_module3
#
# my_package.my_module3.info_print3()
# my_package.my_module4.info_print4()

# 方式2：
# from my_package import my_module3
# from my_package import my_module4
# my_module3.info_print3()
# my_module4.info_print4()

# # 方式3：
# from my_package.my_module3 import info_print3
# from my_package.my_module4 import info_print4
#
# info_print3()
# info_print4()

# 通过__all__ = []控制import*
# 这里的 __all__ = [] 代码要写在package文件夹下的__init__.py里面