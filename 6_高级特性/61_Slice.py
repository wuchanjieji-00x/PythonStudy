# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 取一个list或tuple的部分元素
L = ['Miahcel','Sarah','Tracy','Bob','Jack']
# 笨方法
print ([L[0],L[1],L[2]])
# 取前N个元素，也就是索引为0-(N-1)的元素，可以用循环
r = []
n = 3
for i in range(n): # 注意这里不包括n
    r.append(L[i])
    # r.append(i)
print (r)


# 切片 Slice  也叫做截取函数
#L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素
print (L[0:3])
# 如果第一个索引是0，还可以省略
print (L[:3])
# 也可以从索引1开始，取出2个元素出来：
print (L[1:3])
# 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
print (L[-2:]) # 注意显示的顺序没有颠倒
print (L[-2:-1]) # 注意，这里是不包括-1的。记住倒数第一个元素的索引是-1

# 切片操作十分有用。我们先创建一个0-99的数列
L = list(range(100)) # 注意，这里不包括100
print (L)
# 可以通过切片轻松取出某一段数列。比如前10个数：
print (L[:10])
# 后10个数
print (L[-10:])
# 前11-20个数
print (L[10:20]) # 注意，起始点是10，明确说了第11个数开始，序号是从0开始的
# 前10个数，每两个取一个
print (L[:10:2])
# 所有数，每5个取一个
print (L[::5])
# 甚至什么都不写，只写[:]就可以原样复制一个list
print (L[:])
# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
T = (0,1,2,3,4,5)
print (T[:3]) # 注意这里用的也是[]
# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
S = 'ABCDEFG'
print (S[:3])
print (S[::2])
print (S[::-1]) # 倒序输出


# 有了切片操作，很多地方循环就不再需要了。Python的切片非常灵活，一行代码就可以实现很多行循环才能完成的操作


# 练习题不会做！！！

def trim(s): 
    while s and s[0] == ' ':   # 去除开头空格
        s = s[1:]
    while s and s[-1] == ' ':  # 去除结尾空格（这里需要反向查找）
        s = s[:-1]
    return s  # 返回处理后的字符串

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')