


class StrTools():
    pass

str_tools1 = StrTools()

# 从始至终，我们只创建了一个类对象，避免构造很多的类对象，节省内存空间和开销


# 思想：
# 构建一次类对象，重复使用

s1 = str_tools1
s2 = str_tools1

print(id(s1))
print(id(s2))