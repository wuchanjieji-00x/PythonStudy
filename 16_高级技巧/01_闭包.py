"""
演示闭包的特性
"""
#
# # 简单闭包
# def outer(logo):  # 这个logo是闭包要引用的外部变量
#
#     def inner(msg):
#         print(f'<{logo}>{msg}<{logo}>')
#
#     return inner
#
# fn1 = outer('黑马程序员')
# fn1('大家好')
#
# # 我们最终得到的是一个内部函数，这个内部函数也叫做闭包函数。
# # 它的功能可以正常使用，并且它依赖的外部变量也可以正常使用
# # 我们也可以通过修改外包函数的传参，改变闭包函数依赖的外部变量



# # 使用nonlocal 关键字修改外部函数的值
# def outer(num1):
#
#     def inner(num2):
#         nonlocal num1
#         num1 += num2
#         print(num1)
#     return inner
#
# fn = outer(10)
# fn(10)
# fn(10)
# fn(10)
# fn(10)



# 使用闭包实现ATM案例
def account_create(initial_amount=0):

    def ATM(num, deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f'存款：+{num}m, 账户余额：{initial_amount}')
        else:
            initial_amount -= num
            print(f'取款：-{num}m, 账户余额：{initial_amount}')
    return ATM

atm = account_create()

atm(100)
atm(200)
atm(100, deposit=False)