"""
演示函数作为参数传递
"""
# 数据是固定的，逻辑是未知的，等着你把逻辑写好，作为函数传进来

# 定义一个函数，接收另一个函数作为实参：
def test_func(calculate):  # 这里还不能确定calculate是数据参数还是函数？
    result = calculate(1, 2) # 这里根据函数的调用方式，确定calculate是一个函数
    print(type(calculate))  # <class 'function'>
    print(result)  # 3

# 定义一个作为参数的函数
def calculate(x, y):
    return x+y

# 调用，并传入函数
test_func(calculate)  # 注意这里的调用方式:calculate函数后面没有小括号，意思是calculate是作为参数传进来
# 注意，这里传入的只是封装好的函数逻辑