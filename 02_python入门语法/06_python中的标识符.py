
# 规则1：内容限定
# 限定只能使用：中文、英文、数字、下划线。
# 注意：不能以数字开头

# 错误的代码示范
# 1_name = '张三'   # SyntaxError: invalid decimal literal  语法错误
# name_! = '张三'  # SyntaxError: invalid decimal literal  语法错误

name_ = '张三'
_name = '张三'
_1_name = '张三'


# 规则2: 大小写敏感
Itheima = '黑马程序员'
itheima = 666
print(Itheima)
print(itheima)


# 规则3： 不可使用关键字
# 错误的代码示例：使用了关键字
# class = 1  # SyntaxError: invalid syntax
# def = 1  # SyntaxError: invalid syntax
Class = 1
Def = 1
# 关键字同样大小写敏感