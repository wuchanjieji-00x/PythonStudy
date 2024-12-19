# -*- coding: utf-8 -*-

# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

# 函数person除了必选参数name和age外，还接受关键字参数kw
def person(name,age,**kw):
    print ('name:',name,'age:',age,'other:',kw)
# 在调用该函数时，可以只传入必选参数
print (person('Michael',30))
# 也可以传入任意个数的关键字参数
print (person('Bob',35,city='Beijing'))
print (person('Adam',45,gender='M',job='engineer'))

# 关键字参数有什么用？它可以扩展函数的功能
# 比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到
# 试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求

# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
extra = {'city':'Beijing','job':'engineer'}
print (person('Jack',24,city=extra['city'],job=extra['job']))
# 当然，上面复杂的调用可以用简化的写法
extra = {'city':'Beijing','job':'engineer'}
print (person('Jack',24,**extra)) # **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra

# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
# 仍以person()函数为例，我们希望检查是否有city和job参数：
def person(name,age,**kw):
    if 'city' in kw: # 有city参数
        pass
    if 'job' in kw: # 有job参数
        pass
    print ('name:',name,'age:',age,'other:',kw)
# 但是调用者仍可以传入不受限制的关键字参数：
print (person('Jack',24,city='Beijing',addr='Chaoyang',zipcode=123456))
# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下
def person(name,age,*,city,job): # 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
    print (name,age,city,job)
print (person('Jack',24,city='Beijing',job='Engineer'))

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name,age,*args,city,job):
    print (name,age,args,city,job)
print (person('Michael',30,1,2,3,city='Shanghai',job='Engineer')) # 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
# 命名关键字参数可以有缺省值，从而简化调用
def person(name,age,*,city='Beijing',job):
    print (name,age,city,job)
# 由于命名关键字参数city具有默认值，调用时，可不传入city参数
print (person('Jack',24,job='Engineer'))

# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
def person(name,age,city,job): # 缺少*,city和job被视为位置参数
    pass
             


# 参数组合
# 在Python中定义函数，可以用必选参数（位置参数）、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数！！
def f1(a,b,c=0,*args,**kw):
    print ('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

def f2(a,b,c=0,*,d,**kw):
    print ('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

print (f1(1,2))
print (f1(1,2,c=3))
print (f1(1,2,3,'a','b'))
print (f1(1,2,3,'a','b',x=99))
print (f2(1,2,d=99,ext=None))
# 最神奇的是通过一个tuple和dict，你也可以调用上述函数
args = (1,2,3,4)
kw = {'d':99,'x':'#'}
print (f1(*args,**kw))

args = (1,2,3)
kw = {'d':88,'x':'#'}
print (f2(*args,**kw))
# 所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。


# 例子
def print_scores(**kw):
    print('      Name  Score')
    print('------------------')
    for name, score in kw.items():
        print('%10s  %d' % (name, score))
    print()

print_scores(Adam=99, Lisa=88, Bart=77)

data = {
    'Adam Lee': 99,
    'Lisa S': 88,
    'F.Bart': 77
}

print_scores(**data)

def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()

print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)