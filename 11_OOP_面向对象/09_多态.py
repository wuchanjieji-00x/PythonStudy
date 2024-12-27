

# # 多态
# class Animal: # 定义一个父类
#     def speak(self):
#         pass
#
# class Dog(Animal): # 定义一个子类
#     def speak(self):
#         print('汪汪汪')
#
# class Cat(Animal): # 再定义一个子类
#     def speak(self):
#         print('喵喵喵')
#
#
# def make_noise(animal: Animal):  # 定义一个函数（行为）
#     # 制造点噪音，需要传入animal对象
#     animal.speak()
#
# # 演示多态，使用两个子类对象来调用函数
# dog = Dog()
# cat = Cat()
#
# make_noise(dog)  # 提示要传入一个Animal的父类的对象,但我们传入的是子类的对象
# make_noise(cat)
# # 同样的行为，使用不同的对象，获得不同的运行状态


# 抽象类/顶层抽象/顶层设计
class AC:

    def cool_wind(self):
        pass

    def hot_wind(self):
        pass

    def swing_L_R(self):
        pass
# 由于父类提供的三种方法都是空实现，没有办法直接使用，
# 所以要在子类中必须复写这三种方法，才能实现动作
class Midea_AC(AC):  # 定义美的空调子类
    def cool_wind(self):
        print('美的空调制冷方法')

    def hot_wind(self):
        print('美的空调制热方法')

    def swing_L_R(self):
        print('美的空调左右摆风方法')


class GREE_AC(AC):  # 定义格力空调子类
    def cool_wind(self):
        print('格力空调制冷方法')

    def hot_wind(self):
        print('格力空调制热方法')

    def swing_L_R(self):
        print('格力空调左右摆风方法')

def make_cool(ac: AC):
    ac.cool_wind()


midea_ac = Midea_AC()
gree_ac = GREE_AC()

make_cool(midea_ac)
make_cool(gree_ac)

# 注解：
# 定义父类：相当于制定制造空调的标准，或者说是顶层设计（空调要实现的功能）/顶层抽象（父类的方法都是空实现，只列出了方法，由厂家具体实现）
# 定义子类：相当于美的空调和格力空调都要按照标准，自行去设计，生产自己的空调
# 定义子类对象：相当于，A买了一台美的空调，B买了一台格力空调
# 定义函数：相当于，太热了我想开空调制冷，或者说，要实现空调制冷这个动作
# 定义函数形参：相当于，你想制冷，那么就开空调，这里的形参（空调）是泛指，指代空调这个家电产品，应该用父类对象
# 调用函数，传入子类对象：相当于，A用美的空调制冷，B用格力空调制冷。两者的制冷效果肯定不一样，因为两个不同品牌的空调肯定性能不一样
# 子类对象：A和B想要打开空调制冷，那么这里的空调肯定是A和B家里的实体对象，是具体的空调家电
#


