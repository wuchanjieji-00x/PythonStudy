


# # 打开文件，不存在的文件，r, w, a
# f = open('C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/08_文件的操作/test3.txt', 'w', encoding='UTF-8')
# # write 写入：内容只写入到内存中
# f.write('hello, word')
# # flush刷新：将内存中的数据写入到硬盘中
# f.flush()
# # close()关闭：其实close方法，内置了fluse的功能
# f.close()

# 打开文件，文件已经存在.
# 对于已经存在的文件，写入功能会将文件里的内容全部覆盖掉
f = open('C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/08_文件的操作/test3.txt', 'w', encoding='UTF-8')
# write写入，flush刷新
f.write('会当凌绝顶')
f.flush()
f.close()