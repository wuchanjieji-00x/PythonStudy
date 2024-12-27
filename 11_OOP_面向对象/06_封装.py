"""
演示面向对象封装思想中私有成员的使用
"""

# # 定义一个类，内含私有成员变量和私有成员方法
# class phone:
#
#     __current_volatge = 0.5   # 定义私有成员变量
#
#     def __keep_single_core(self): # 定义私有成员方法
#         print('让cpu以单核模式运行')   
#
#     def call_by_5g(self):  # 定义公开成员方法
#         if self.__current_volatge >= 1: # 类的公开成员方法可以访问类的私有成员变量
#             print('5g通话已开启')
#         else:
#             self.__keep_single_core() # 类的公开成员方法可以调用类的私有成员方法
#             print('电量不足，无法使用5g通话，已设置为单核运行进行省电')
#     # 也就是说，如果这个公开方法变成私有的，那么这个方法仍然可以访问和调用类的私有成员，（也就是说，类内部是可以访问和调用的）
#     # 但是，类对象就永远不能访问和调用类的私有成员。
#     # 这也是苹果的越狱和安卓的root，刷机，目的是访问和调用私有成员
#     # 或者说，将类的私有成员变成公开的；或者，定义公开方法去访问和调用类的私有成员，
#     # 目的是使用手机中被限制的功能
#
# phone = phone()
# # phone.__keep_single_core  # 报错，对象不能直接调用私有成员方法
# # print(phone.__current_volatge) # 报错，对象不能直接访问私有成员变量
# # phone.call_by_5g() # 类对象可以通过公开成员方法：访问类的私有成员变量，调用类的私有成员方法

# 拓展：类对象如何直接访问和调用类的私有成员呢？
# 根据错误内容：AttributeError: 'phone' object has no attribute '__keep_single_core'. Did you mean: '_phone__keep_single_core'?
# 感觉应该是可以的，但是调用方式暂时不知道



# 练习
class Phone:

    __is_5g_enable = True

    def __check_5g(self):
        if self.__is_5g_enable == True:
        # 这个判断条件可以写为：if self.__is_5g_enable：
        # 不要记，要feel
            print('5g开启')
        else:
            print('5g关闭，使用4g网络')

    def call_by_5g(self):
        self.__check_5g()  # 在方法中，调用和访问类的成员，都要通过self
        # if self.__is_5g_enable == True:
        print('正在通话中')

    # 思想：用户不需要知晓5g的状态，5g是否要开启，
    # 你只需要打电话，我会告诉你5g开没有开启，我会告诉你当前的信号强度支不支持5g，需不需要切换到4g去
    # 但是，用户又需要实现打电话的功能，所有我必要要设计一个公开方法供用户使用。
    # 但是打电话又需要检查5g的状态，所以我会把这个接口做在公开方法中，在公开方法内部中去检查，同时用户又不能直接感受到

phone = Phone()

phone.call_by_5g()


