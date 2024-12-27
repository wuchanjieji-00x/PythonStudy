


# 打开文件得到文件对象，准备读取
fr = open('C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/08_文件的操作/bill.txt', 'r', encoding='UTF-8')

# 打开文件得到文件对象，准备写入
fw = open('C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/08_文件的操作/bill.txt.bak', 'w', encoding='UTF-8')

# for 循环读取文件
for line in fr:
    line =line.strip()  # 去除首尾空格和换行符
    if line.split(',')[4] == '测试': # 根据逗号分割，得到list，每个元素都是字符串，第五个元素如果是测试的话，就不输出，继续下一次循环
        continue
    fw.write(line) # 将不是测试的line写入到fw文件对象中
    fw.write('\n') # 记得每一行末尾要添加换行符

fr.close() # 关闭文件
fw.close()
