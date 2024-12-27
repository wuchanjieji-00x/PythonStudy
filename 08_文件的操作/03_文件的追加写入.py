


# 打开一个不存在的文件  'a'模式
f = open('C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/08_文件的操作/test4.txt', 'a', encoding='UTF-8')
f.write('会当凌绝顶')
f.flush()
f.close()


# 打开一个存在的文件  'a'模式
f = open('C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/08_文件的操作/test4.txt', 'a', encoding='UTF-8')
f.write('\n一览众山小')
f.flush()
f.close()