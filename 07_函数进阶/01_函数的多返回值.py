"""
演示函数的多返回值示例
"""

# 使用多个变量，接收多个返回值
# 类型不受限、有序
def test_return():
    return 1, 'A', True

x, y, z = test_return()
print(x, type(x))  # 1 <class 'int'>
print(y, type(y))  # A <class 'str'>  # 类型不受限
print(z, type(z))  # True <class 'bool'>

