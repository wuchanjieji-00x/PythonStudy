"""
演示面向对象：继承
"""

# 1.继承的基础语法

# # 1.1.单继承
# class Phone:  # 定义一个父类
#     IMEI = None  # 序列号
#     producer = 'HTC' # 厂商
#
#     def call_by_4g(self):
#         print('4g通话')
#
# class Phone2024(Phone): # 定义一个子类，从Phone这个父类继承其所有的成员（不含私有成员）
#     face_id = '1000101' # 面部识别ID
#
#     def call_by_5g(self):
#         print('2024新功能：5g通话')

# Phone = Phone2024()  # 定义一个子类的对象/实例，它包含了子类和被继承的父类的所有成员（不含私有成员）
#
# print(Phone.producer)
# Phone.call_by_4g()
# Phone.call_by_5g()


# # 1.2.多继承
# # 多继承中，一个子类可以继承很多个父类，可以继承所有被继承的父类的成员（不含私有成员）
#
# class NFCReader: # 定义第二个父类
#     nfc_type = '第五代'
#     producer = 'HM'
#
#     def read_card(self):
#         print('NFC读卡')
#
#     def write_card(self):
#         print('NFC写卡')
#
# class RemoteControl: # 定义第三个父类
#     rc_type = '红外遥控'
#
#     def Control(self):
#         print('开启红外遥控')
#
# class MyPhone(Phone, NFCReader, RemoteControl):
#     pass  # 占位语句，表示空的意思
#
# phone = MyPhone()
# phone.call_by_4g()
# phone.read_card()
# phone.write_card()
# phone.Control()
# print(phone.producer) # HTC 这里输出的是HTC，而非HM，说明我们继承的成员是Phone父类的，因为它靠左（靠前）,首先被继承，优先级最高



# 2.复写（复写父类的成员）
# 子类虽然继承了父类所有的成员，但是，当子类里有和父类同名的成员，那么子类的对象使用的是子类的成员（覆盖父类里同名的成员）

# 我们在子类里面复写了父类的同名成员之后，就相当于将父类的同名成员替换掉了。此时，对于同名成员，我们相当于获得了两套逻辑，都可以用
# 那为什么我在子类里复写之后，还需要调用父类的同名成员呢？是因为父类里的同名成员是原始平台，子类只想在原始平台核心上，拓展其他的功能而已
# 这一点，对于成员变量来说不太明显，但是对于成员方法来说，比较普遍
# 映射到现实生活中，父类的同名成员变量（平台）和子类的同名变量（车型），不一样很正常，因为对于具体的车型会和平台不一样
# 但是在平台的成员方法中，比如轴距，三大件可能都是一样的，不同的车型完全没必要把这些核心的东西再做一遍，只需要调用平台的就可以了
# 不同的车型只需要以这个为核心基础，进行拓展变更优化
class phone:  # 定义父类
    IMEI = None
    producer = 'ITCAST'

    def call_by_5g(self):
        print('父类的方法')

class myphone(phone):  # 定义一个子类
    producer = 'ITHEIMA'  # 复写父类的成员属性

    def call_by_5g(self):
        print('子类复写的方法')

        # 子类复写父类的成员后，仍想调用父类成员的方式：
        # 方式1：
        print(f'父类的producer是{phone.producer}')
        phone.call_by_5g(self)
        # # 方式2：
        # print(f'父类的producer是：{super().producer}')
        # super().call_by_5g()

phone1 = myphone()
phone1.call_by_5g()  # 子类实体类对象默认是调用子类的成员，父类的同名成员只能子类中进行调用
print(phone1.producer)



