# -*- coding: utf-8 -*-

# 定义函数

# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回
# 函数体内部可以用return随时返回函数结果；
# 函数执行完毕也没有return语句时，自动return None
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


# 请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return。


# 空函数
# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
def nop():
    pass
    
# if age >= 18:
#    pass


# 参数检查
# 对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
    

# 返回多个值
# import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数
import math

def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny

# 然后，我们就可以同时获得两个返回值：
x,y = move(100,100,60,math.pi / 6)
print (x,y)

# 但其实这只是一种假象，Python函数返回的仍然是单一值
# 原来返回值是一个tuple！
# 但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
# 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
r = move(100,100,60,math.pi / 6)
print (r)


# 定义一个函数 quadratic(a,b,c)，接收3个参数，返回一元二次方程ax2+bx+c=0的两个解
import math
def quadratic(a,b,c):
    d = b**2 - 4*a*c
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    return x1,x2
# 测试
print ('quadratic(2,3,1)= ', quadratic(2,3,1))
print ('quadratic(1,3,-4)=', quadratic(1,3,-4))

if quadratic(2,3,1) != (-0.5,-1.0):
    print ('测试失败')
elif quadratic(1,3,-4) != (1.0,-4.0):
    print ('测试失败')
else:
    print ('测试成功')