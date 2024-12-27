

from str_tools import str_tools1
# 这个str_tools1 是str_tools文件中的StrTools类的一个实例/类对象
# 原来不仅可以导入类，还可以导入实例/类对象
# 而且，我们还可以用不同的变量重复引用这个实例/类对象

s1 = str_tools1
s2 = str_tools1

print(id(s1))
print(id(s2))
# 返回的id是同一个



