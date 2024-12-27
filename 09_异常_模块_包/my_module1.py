

__all__ = ['calculate']  # 只作用在要导入自定义模块函数的字符’*‘上

# 在当前文件目录下创建一个自定义模块，my_module1
# 在自定义模块下，自定义函数供其他程序导入使用
def calculate(a, b):
    print(a + b)
def calculate1(a, b):
    print(a - b)


# 测试
# 输入main点回车
if __name__ == '__main__':    #只要运行这个文件，这个判断条件就置True
    calculate(1, 2)
# 在这里经过if处理后，下面的测试代码只能运行自定义模块时才能运行
# 在外部程序导入时，if的判断条件为False，测试代码不会运行