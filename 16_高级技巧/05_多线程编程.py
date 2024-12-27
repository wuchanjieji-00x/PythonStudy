"""
多线程编程
"""

# 意义是，创建一个python程序，但同时可以做很多事情
# 如果是运行多个python程序，那叫做多任务编程

# 不传参
import threading
import time


# def sing():
#     while True:
#         print('我在唱歌')
#         time.sleep(1)
#
#
# def dancing():
#     while True:
#         print('我在跳舞')
#         time.sleep(1)
#
#
# # 测试
# if __name__ == '__main__':
#     # 创建一个唱歌的线程
#     sing_thread = threading.Thread(target=sing)
#
#     # 创建一个跳舞的线程
#     dance_thread = threading.Thread(target=dancing)
#
#     # 让线程去工作
#     sing_thread.start()
#     dance_thread.start()

# 传参
# 我们只在每个线程函数里面给个形参，通过线程调用，传入实参
# args：元组传参；kwargs:字典传参
def sing(msg):
    while True:
        print(msg)
        time.sleep(1)


def dancing(msg):
    while True:
        print(msg)
        time.sleep(1)


# 测试
if __name__ == '__main__':

    # 调用一次相当于创建了一个线程
    # 创建一个唱歌的线程
    sing_thread = threading.Thread(target=sing, args=('我要唱歌', ))

    # 创建一个跳舞的线程
    dance_thread = threading.Thread(target=dancing, kwargs={'msg': '我在跳舞'})

    # 让线程去工作
    sing_thread.start()
    dance_thread.start()
