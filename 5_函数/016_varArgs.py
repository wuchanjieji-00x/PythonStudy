# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数的参数

# 位置参数
def power(x):
    return x * x
# 对于power(x)5_函数，参数x就是一个位置参数
# 当我们调用power函数时，必须传入有且仅有的一个参数x
print (power(5))
print (power(15))

def power3(x):
    return x * x * x
print (power3(5))

# 但是如果要计算x4、x5……怎么办？我们不可能定义无限多个函数
# 你也许想到了，可以把power(x)修改为power(x, n)，用来计算xn，说干就干
def power(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print (power(5,3)) # 对于这个修改后的power(x, n)5_函数，可以计算任意n次方
# 修改后的power(x, n)函数有两个参数：x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n



# 默认参数

# print (power(5)) # Python的错误信息很明确：调用函数power()缺少了一个位置参数n。
# 这个时候，默认参数就排上用场了。
# 由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2
def power(x,n=2): # 这里的n是默认参数
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print (power(5)) # 这样，当我们调用power(5)时，相当于调用power(5, 2), 而对于n > 2的其他情况，就必须明确地传入n，比如power(5, 3)。

# 我们写个一年级小学生注册的函数，需要传入name和gender两个参数
def enroll(name,gender):
    print ('name:',name)
    print ('gender:',gender)
# 这样，调用enroll()函数只需要传入两个参数
print (enroll('Sarah','F'))
# 如果要继续传入年龄、城市等信息怎么办？这样会使得调用函数的复杂度大大增加。
# 我们可以把年龄和城市设为默认参数
def enroll(name,gender,age=6,city='beijing'):
    print ('name:',name)
    print ('gender:',gender)
    print ('age:',age)
    print ('city:',city)

print (enroll('Sarah','F')) # 这里面的name gender要加引号

# 有多个默认参数时，调用的时候，既可以按顺序提供默认参数，
# 比如调用enroll('Bob', 'M', 7)，意思是，除了name，gender这两个参数外，最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。
print (enroll('Bob','M','7'))
# 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。
# 比如调用enroll('Adam', 'M', city='Tianjin')，意思是，city参数用传进去的值，其他默认参数继续使用默认值
print (enroll('Adam','M',city='TianJin'))  # 这里的city不需要加引号



# 可变参数
# 在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个

# 我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
# 但是调用的时候，需要先组装出一个list或tuple
print (calc([1,2,3])) # numbers 是个list
print (calc((1,3,5,7))) # numbers 是个tuple

# 我们把函数的参数改为可变参数
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
# 但是，调用该函数时，可以传入任意个参数，包括0个参数
print (calc(1,2,3))
print (calc(1,3,5,7))
print (calc())

# 如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做
num = [1,2,3] # list
print (calc(num[0],num[1],num[2]))

# 这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
num = [1,2,3]
print (calc(*num)) # *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见


# 练习题
def mul(x,*args): # 这里为什么要留一个位置参数
    sum = 1
    for n in args:
        sum = sum *n
    return x*sum
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:  # 这是啥意思？
        print('测试成功!')


# 小结
# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
# 要注意定义可变参数和关键字参数的语法：
# *args是可变参数，args接收的是一个tuple
# **kw是关键字参数，kw接收的是一个dict
# 以及调用函数时如何传入可变参数和关键字参数的语法：
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数


# 例子
def hello(greeting, *args):
    if (len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))

hello('Hi') # => greeting='Hi', args=()
hello('Hi', 'Sarah') # => greeting='Hi', args=('Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello', args=('Michael', 'Bob', 'Adam')

names = ('Bart', 'Lisa')
hello('Hello', *names) # => greeting='Hello', args=('Bart', 'Lisa')