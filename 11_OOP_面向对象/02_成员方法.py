"""
演示面向对象中的成员方法定义和使用
"""

# 定义一个带有成员方法的类：
class student:  # 定义一个类
    name = None # 定义类的成员变量 或者叫做 成员属性

    def say_hi(self): # 定义类的成员方法 注意，在定义成员方法中，self形参必须写
        print(f'大家好，我是{self.name}，希望大家多多关照') # 在成员方法的方法体中，访问成员变量，一定要通过self去访问

    def say_hi2(self, msg):  # 定义成员方法时，可以接受对象的实参传递，可以让对象更加个性化
        # self不占用形参位置
        print(f'大家好，我是{self.name}, {msg}') # 在成员方法的方法体中，调用外部形参，直接调用，不需要通过self访问

stu_1 = student() # 创建一个对象，  或者叫做:创建一个实例
stu_1.name = '周杰伦' # 给对象的成员变量赋值
stu_1.say_hi()  # 调用对象的成员方法。（注意：self是自带的，在传参的时候，可忽略self形式参数）

# 可以多次创建对象，每个对象之间相互独立，互不干扰
stu_2 = student()
stu_2.name = '林俊杰'
stu_2.say_hi()

stu_3 = student()
stu_3.name = '张学友'
stu_3.say_hi2('nice to meet you')  # 在调用成员方法，传实参的时候，忽略self