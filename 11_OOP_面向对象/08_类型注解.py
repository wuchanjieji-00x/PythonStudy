"""
类型注解：
1.变量
2.函数（方法）
"""
# 通过注解，可以显而易见的知道变量的类型，不仅是开发者自己做标记，同时也相当于告诉IDE变量的类型了

# # 1.类型注解：变量
# # 方式1：在变量附近做注解,常用方式
# # 1.1 基础数据类型
# import json
# import random
#
# var1: int = 10
# var2: str = 'itheima'
# var3: bool = True
# # 1.2 类对象   没看懂。。。
# class student:
#     pass
# stu: student = student()  # 说明student是student的类对象的类型
# # print(type(student))
# # 1.3 数据容器：基础注解
# my_list: list = [1, 2, 3]  # list是注解，my_list是变量
# my_tuple: tuple = (1, 2, 3)
# my_dict: dict = {'itheima': 666}
#
# # 1.4 数据容器：详细注解
# my_list1: list[int] = [1, 2, 3]  # list是注解，my_list是变量
# my_tuple1: tuple[int, str, bool] = (1, 'itheima', True) # tuple变量的类型注解，要把所有元素都注解掉
# my_dict1: dict[str, int] = {'itheima': 666}

# # 方式2：在注释中做注解
# # alt + 回车：自动搜索并导入package,代码上方自动添加导入package的代码：import random
# var4 = random.randint(1, 10)  # type:int  # 注意：这里注释里的int变亮了，说明IDE识别到了这个类型注解
# var5 = json.loads('{"name": "zhangsan"}')  # type: dict[str, str]
#
# def func():
#     return 10
# var6 = func()  # type: int

# # 上面这样显示的类型注解一般无意义，我们主要是在不能一眼看出变量或函数返回值的类型的地方加注解
# var7: int = random.randint(1, 10)
# var8: dict = json.loads('{"name": "zhangsan"}')
# # var9: student = fun()  # 这样可以看出var9变量是student的一个实例类对象

# # 拓展：
# # 类型注解仅仅是个程序的备注，提示功能，压根不会影响到程序的运行
# var10: int = 'itheima'
# var11: str = 123


# 2.函数（方法）的形参和返回值的类型注解,同样也是提示性的
# # 1. 形参
# def add(x: int, y: int):
#     return x + y
# add(1, 2)  # ctrl + p: 查看IDE提示
# 函数/方法的返回值
# def func(data: list) -> list:
#     # print(data.count()) # 定义了形参类型注解后，比如是list，那么在使用data加'.'后，IDE就会提示list里的方法了
#     return data
# print(func(1))



# Union联合类型注解:Union里面的类型是或的关系
# 使用Union类型注解，必须先导入package
from typing import Union

my_list: list[Union[int, str, bool]] = [1, 2, 'itheima', True]

def func(data: Union[int, str]) -> Union[int, str]:
    pass
func(2)  # 提示：data:int|str