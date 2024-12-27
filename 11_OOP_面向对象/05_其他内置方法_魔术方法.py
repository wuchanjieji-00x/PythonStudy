


class student:

    # 魔术方法：__init__ ：设置初始化行为
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 魔术方法：__str__：定义输出内容
    def __str__(self):
        return f'student类对象，name:{self.name},年龄：{self.age}'  # 定义输出内容

    # 魔术方法：__lt__ ： < 和 >
    def __lt__(self, other):
        return self.age < other.age  # 定义判断逻辑

    # 魔术方法：__le__ ： <= 和 >=
    def __le__(self, other):
        return self.age <= other.age  # 定义判断逻辑

    # 魔术方法：__eq__ ： ==
    def __eq__(self, other):
        return self.age == other.age  # 定义判断逻辑




# # 魔术方法：__init__ ：设置初始化行为
# stu1 = student('周杰伦', 31)
# print(stu1) # <__main__.student object at 0x0000022A52A65390>
# print(str(stu1)) # <__main__.student object at 0x0000022A52A65390>
# 得到的是内存地址

# # 魔术方法：__str__：定义输出内容
# stu1 = student('周杰伦', 31)
# print(stu1) # student类对象，name:周杰伦,年龄：31
# print(str(stu1)) # student类对象，name:周杰伦,年龄：31

# # 魔术方法：__lt__ ： < 和 >
# stu1 = student('周杰伦', 31)
# stu2 = student('林俊杰', 35)
# print(stu1 < stu2)  # True,实际上，根据魔术方法的返回值，比较的是不同类对象的年龄
# print(stu1 > stu2)  # False

# # 魔术方法：__le__ ： <= 和 >=
# stu1 = student('周杰伦', 35)
# stu2 = student('林俊杰', 35)
# print(stu1 <= stu2)  # True
# print(stu1 >= stu2)  # True

# 魔术方法：__eq__ ： ==
# # 1.不定义__eq__方法时，'==' 默认比较的是两个类对象的内存地址，结果肯定是False
# stu1 = student('周杰伦', 35)
# stu2 = student('林俊杰', 35)
# print(stu1 == stu2)  # False
# # 2.定义__eq__方法时，'==' 比较的逻辑是魔术方法中定义的判断逻辑
# stu1 = student('周杰伦', 35)
# stu2 = student('林俊杰', 35)
# print(stu1 == stu2)  # True