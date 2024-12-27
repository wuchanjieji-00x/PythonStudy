"""
文件处理相关的工具模块
"""
# 函数1：
def print_file_info(file_name):
    """
    函数功能：将给定路径的文件内容输出到控制台
    :param file_name:即将读取的文件路径
    :return:None (只print)
    """
    f = None  # 防止警告，这里提前定义一个空变量  # None在if判断里等价于False
    try:
        f = open(file_name, 'r', encoding='UTF-8')
        content = f.read()
        print('文件的全部内容如下：')
        print(content)
    except Exception as e:
        print(f'程序出现异常了，具体原因是：{e}')
    finally:
        if f:  # 如果变量是None，表示False；如果有任何内容，则不是None，即为True
            f.close() # 这里是为了防止，文件本来就不存在，则f一直是None（False),那么f.close()肯定会报错


# 函数2：
def append_to_file(file_name, data):
    """
    功能：将指定的数据追加写入到指定的文件中
    :param file_name: 指定的文件路径
    :param data: 要追加写入的数据
    :return: None(只print)
    """
    f = open(file_name, 'a', encoding='UTF-8')
    f.write(data)
    f.write('\n')
    f.close()

# 测试
if __name__ == '__main__':  # 这一行不能注释掉
    # # 函数1：
    # print_file_info('C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/08_文件的操作/bill.txt')
    # print_file_info('C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/08_文件的操作/bill.txtxx')
    # # 程序出现异常了，具体原因是：[Errno 2] No such file or directory:
    # # 'C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/08_文件的操作/bill.txtxx'

    # 函数2：
    append_to_file('C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/08_文件的操作/test_append.txt', '会当凌绝顶')
    append_to_file('C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/08_文件的操作/test_append.txt', '一览众山小')

