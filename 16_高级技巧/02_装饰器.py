"""
装饰器
"""

# # 装饰器的一般写法（闭包）
# def outer(func):
#     def inner():
#         print('我睡觉了')
#         func()
#         print('我起床了')
#
#     return inner
#
# def sleep():
#     import random
#     import time
#     print("睡眠中...")
#     time.sleep(random.randint(1, 3))
#
#
# fn = outer(sleep)
# fn()


# 装饰器的快捷写法:语法糖
def outer(func):
    def inner():
        print('我睡觉了')
        func()
        print('我起床了')

    return inner
@outer
def sleep():
    import random
    import time
    print("睡眠中...")
    time.sleep(random.randint(1, 3))

sleep()  # 其实这里是把sleep函数作为参数传入到outer函数中，调用的仍然是inner函数，只是直观上感觉调用的还是sleep函数，而且功能增加了