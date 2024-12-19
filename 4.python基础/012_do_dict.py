# -*- coding: utf-8 -*-

# dict  dictionary

d = {'Michael':95,'Bob':75,'Tracy':85}
print ('d[\'Michael\'] =', d['Michael'])
print ('d[\'Bob\'] = ',d['Bob'])
print ('d[\'tracy\'] = ', d['Tracy'])

# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存
print ('Thomas' in d)

# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
print ('d.get(\'Thomas\', -1) = ', d.get('Thomas', -1))


# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
d.pop('Bob')
print (d)

# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d['Adam'] = 67
print (d)


# 所以，dict是用空间来换取时间的一种方法。
# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。



# 先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。
# 无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。
# dict就是第二种实现方式，给定一个名字，比如'Michael'，
# dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，也就是95这个数字存放的内存地址，直接取出来，所以速度非常快。