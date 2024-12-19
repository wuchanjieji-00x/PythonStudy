# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
# 在Python中，迭代是通过 for ... in 来完成的，而很多语言比如C语言，迭代list是通过下标完成的，比如C代码
#for (i=0,i<length;i++):{
#    n = list[i];
#}

# Python的for循环抽象程度要高于C的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上
# list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代
d = {'a':1,'b':2,'c':3}
for key in d:
    print (key)  # 注意，因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()

# 由于字符串也是可迭代对象，因此，也可以作用于for循环
for ch in 'ABC':
    print (ch)

# 所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
# 那么，如何判断一个对象是可迭代对象呢？方法是通过 collections.abc 模块的 Iterable 类型判断：
from collections.abc import Iterable
print (isinstance('abc',Iterable)) # str是否可迭代
print (isinstance([1,2,3],Iterable)) # list是否可迭代
print (isinstance(123,Iterable)) # 整数是否可迭代


# 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i,value in enumerate(['a','b','c']):
    print (i,value)
# 上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码
for x,y in [(1,1),(2,4),(3,9)]:
    print (x,y)

# 练习题
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    if L == []: # if len(L)==0:  if not L:
        min = None
        max = None
    else:
        max = L[0]
        min = L[0]
        for value in L:
            if max < value:
                max = value
            if min > value:
                min = value            
    return (min,max)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


# 源码
from collections.abc import Iterable, Iterator

def g():
    yield 1
    yield 2
    yield 3

print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterable? \'abc\':', isinstance('abc', Iterable))
print('Iterable? 123:', isinstance(123, Iterable))
print('Iterable? g():', isinstance(g(), Iterable))

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
print('Iterator? \'abc\':', isinstance('abc', Iterator))
print('Iterator? 123:', isinstance(123, Iterator))
print('Iterator? g():', isinstance(g(), Iterator))

# iter list:
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):
    print(x)

print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d = {'a': 1, 'b': 2, 'c': 3}

# iter each key:
print('iter key:', d)
for k in d.keys():
    print('key:', k)

# iter each value:
print('iter value:', d)
for v in d.values():
    print('value:', v)

# iter both key and value:
print('iter item:', d)
for k, v in d.items():
    print('item:', k, v)

# iter list with index:
print('iter enumerate([\'A\', \'B\', \'C\']')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# iter complex list:
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)