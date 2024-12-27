"""
演示类的构造方法
"""

# # 使用构造方法对成员变量进行赋值
# # __init__
# class student:
#     # name = None  # 这里可以不用声明成员变量，在构造方法里直接连变量声明和变量赋值一起做了
#     # age = None
#     # tel = None
#
#     def __init__(self, name, age, tel): # self不占用形参位置，构造方法接收对象创建时的实参
#         self.name = name  # 成员变量声明和赋值
#         self.age = age
#         self.tel = tel
#         print('student类创建了一个类对象') # 验证用。说明，当类对象工作时，首先执行构造方法
#
# stu1 = student('周杰伦', 30, '185000') # 创建类对象时，将构造方法的实参传进去，作为类的成员变量/成员属性
# print(stu1.name)
# print(stu1.age)
# print(stu1.tel)


# 练习,没有写出来

for num in [1, 11]:
    print(f'当前录入第{num}位学生信息，总共需录入10位学生信息')
    class student:
        name = input('请输入学生姓名： ')
        age = input('请输入学生年龄： ')
        addr = input('请输入学生地址： ')

        def __init__(self, name, age, addr):
            self.name = name
            self.age = age
            self.addr = addr
            print(f'学生{num}信息录入完成，信息为：【学生姓名：{self.name}，年龄：{self.age}, 地址：{self.addr}】')
    num += 1
# stu1 = student('周杰伦', 30, '北京')

