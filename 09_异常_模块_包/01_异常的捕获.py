
# # 捕获异常基本语法  # 未正确设置异常类型，将无法捕获异常
# try:  # 表明可能出现的异常
#     f = open('C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/09_异常_模块_包/test.txt', 'r', encoding='UTF-8')
# # 报错：FileNotFoundError: [Errno 2] No such file or directory:
# # 'C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/09_异常_模块_包/test.txt'
# except: # 如果出现异常了，将执行except下的代码
#     print('出现异常了， 因为文件不存在，我将open的模式改为w模式先新建文件再打开')
#     f = open('C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/09_异常_模块_包/test.txt', 'w', encoding='UTF-8')


# # 捕获指定异常
# try:
#     print(name) # NameError: name 'name' is not defined
# except NameError as e:  # 只捕获NameError类型的异常
#     print('出现了变量未定义的异常')
#     print(e) # name 'name' is not defined  # 变量e记录了异常的具体内容


# # 捕获多个异常
# try:
#     print(1 / 0)
# except (NameError, ZeroDivisionError) as e:
#     print('出现了变量未定义或除以零的异常错误')
#     print(e)  # 输出具体异常内容
#


# # 捕获所有异常
# # 方式1：# 捕获异常基本语法
#
# # 方式2： 一般情况下用这个
# try:
#     1 / 0
# except Exception as e:
#     print(f'出现异常了,具体是：{e}')
#


# # 异常else
# # 如果没有出现异常，将要执行else下面的代码
# try:
#     print('hello')
# except Exception as e:
#     print(f'出现异常了,具体是：{e}')
# else:
#     print('恭喜你，没有出现异常')



# finally
# 不管有没有出现异常，finally下面的代码都要执行
try: # 尝试执行一段代码
    f = open('C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/09_异常_模块_包/test.txt', 'r', encoding='UTF-8')
except Exception as e: # 出现异常会执行
    print(f'出现异常了,具体是：{e}')
    f = open('C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/09_异常_模块_包/test.txt', 'w', encoding='UTF-8')
else: # 可选  # 没有异常会执行
    print('恭喜你，没有出现异常')
finally: # 可选 # 有没有异常都执行
    f.close()
    print('我是finally，有没有异常我都会执行')


