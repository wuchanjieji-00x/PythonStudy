


# 定义一个函数，接收另一个函数作为实参：
def test_func(calculate):  # 这里还不能确定calculate是数据参数还是函数？
    result = calculate(1, 2) # 这里根据函数的调用方式，确定calculate是一个函数
    print(type(calculate))  # <class 'function'>
    print(result)  # 3


# 方式1：
# 定义一个作为参数的函数
def calculate(x, y):
    return x+y

# 调用，并传入函数
test_func(calculate)  # 注意这里的调用方式:calculate函数后面没有小括号，意思是calculate是作为参数传进来
# 注意，这里传入的只是封装好的函数逻辑


# 方式2：使用lambda匿名函数
test_func(lambda x, y: x + y)

# 两种方式输出完全一样
# lambda匿名函数：
# 1.函数体只能写一行，
# 2.只作为临时使用，只作用在当前函数调用中 （意思是不能和def定义的有名称的函数一样重复调用，二次或多次使用只能再写一个lambda函数）