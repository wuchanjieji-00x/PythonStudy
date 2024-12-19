# -*- coding: utf-8 -*-

# set
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key

s = set([1,2,3])
print (s)
# r = set{1,2,3}
# print (r)

# 重复元素在set中自动被过滤
s1 = set([1,1,2,2,3,3])
print (s1)  

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
print (s) 

# 通过remove(key)方法可以删除元素
s.remove(4)
print (s) 

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s2 = set([1,2,3])
s3 = set([2,3,4])
print (s2 & s3) # 交集
print (s2 | s3) # 并集


# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。