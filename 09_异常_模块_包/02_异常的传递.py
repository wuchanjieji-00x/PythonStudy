

# 定义一个出现异常的方法：
def func1():
    print('func1开始执行')
    num = 1 / 0
    print('func1结束执行')
def func2():
    print('func2开始执行')
    func1()
    print('func2结束执行')
def func3():
    print('func3开始执行')
    func2()
    print('func3结束执行')
def main():
    try:
        func3()
    except Exception as e:
        print(f'出现异常了，异常内容是：{e}')  # 出现异常了，异常内容是：division by zero
    # 可以看出：我们想要捕获异常的话，并不需要到出现异常的原始位置
    # 只要函数/方法之间存在调用关系（层级关系）,我们在最顶级的调用这里就可以捕获异常

main()

# Traceback (most recent call last):
#   File "C:\Users\xiaozh52\pythonstudy\pycharm\itheima_python\09_异常_模块_包\02_异常的传递.py", line 19, in <module>
#     main()
#   File "C:\Users\xiaozh52\pythonstudy\pycharm\itheima_python\09_异常_模块_包\02_异常的传递.py", line 17, in main
#     func3()
#   File "C:\Users\xiaozh52\pythonstudy\pycharm\itheima_python\09_异常_模块_包\02_异常的传递.py", line 14, in func3
#     func2()
#   File "C:\Users\xiaozh52\pythonstudy\pycharm\itheima_python\09_异常_模块_包\02_异常的传递.py", line 10, in func2
#     func1()
#   File "C:\Users\xiaozh52\pythonstudy\pycharm\itheima_python\09_异常_模块_包\02_异常的传递.py", line 6, in func1
#     num = 1 / 0
# ZeroDivisionError: division by zero

# 可以看到：异常从最底层的func1传递到最高层的main函数，再到main函数的调用