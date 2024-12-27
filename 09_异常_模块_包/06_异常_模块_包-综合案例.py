


# 创建my_utils自定义包，在包内创建：str_uyil.py 和 file_util.py 两个模块，并提供相应的函数

# 导入相应模块
import my_utils.str_util
from my_utils import file_utils

print(my_utils.str_util.str_resverse('abcd'))

print(my_utils.str_util.substr('abcdefg', 2, 5 ))

file_utils.append_to_file('C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/08_文件的操作/test_append1.txt', '明月几时有')
file_utils.append_to_file('C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/08_文件的操作/test_append1.txt', '把酒问青天')

file_utils.print_file_info('C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/08_文件的操作/test_append2.txt')
file_utils.print_file_info('C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/08_文件的操作/test_append1.txt')