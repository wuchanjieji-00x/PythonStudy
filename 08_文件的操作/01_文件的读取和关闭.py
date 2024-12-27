


# # 打开文件
# f = open('C:/Users/xiaozh52/pythonstudy/forTest/test1.txt', 'r', encoding='UTF-8')
# print(type(f))  # <class '_io.TextIOWrapper'> 文本IO封装

# # 读取文件：read()
# # 传实参：代表读取多少个字节；不传实参：读取全部内容；当前read会从上一个read停止处继续读取
# # print(f'读取10个字节的结果：{f.read(10)}')
# print(f'读取全部内容的结果：{f.read()}')
# print('-----------------------------')
# print(f'读取全部内容的结果：{f.read()}') # 上面已经读完了，再读就读不出来了.

# 说明指针已经走到文件末尾，再往后读，指针已经找不到内容了，所以，只要在文件打开一次的过程中，
# 读取操作是默认一个接一个往后读，直到文件末尾


print('-----------------------------')


# # 读取文件：readlines()
# # 读取文件的全部行，并封装到列表中
# lines = f.readlines()
# print(f'lines的对象的类型：{type(lines)}')  # lines的对象的类型：<class 'list'>
# print(lines)  # []


# # 读取文件：readline()
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# line4 = f.readline()
# line5 = f.readline()
# print(line1)
# print(line2)
# print(line3)
# print(line4)
# print(line5)


# # 读取文件：for循环
# for line in f:
#     print(line)

# # 关闭文件：close()，解除对文件的占用
# f.close()  # 这里的f对应的是文件打开时赋予的对象名，所以这里只要启用f的close方法就可以关闭打开的文件


# # with open 语法操作文件 : 程序执行完毕后，自动close文件
# with open('C:/Users/xiaozh52/pythonstudy/forTest/test1.txt', 'r', encoding='UTF-8') as f:
#     for line in f:
#         print(line)


# 练习
num = 0
with open('C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/08_文件的操作/word.txt', 'r',encoding='UTF-8') as f:
    for line in f:
        # print(line)
        # print(type(line)) # <class 'str'>
        line = line.strip()  # 去除开头和结尾的空格以及换行符
        list1 = line.split(' ') # 按照空格进行切分
        # print(list1)

        for x in list1:
            if x == 'itheima':
                # global num
                num += 1
print(num)



# 教程
# 打开文件
f = open('C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/08_文件的操作/word.txt', 'r',encoding='UTF-8')

# # 方式1：读取全部内容，得到一个字符串，通过字符串count方法统计itheima出现的次数
#
# content = f.read()
# count = content.count('itheima')
# print(count)  # 6

# 方式2：读取内容， 一行一行的读取
count = 0
for line in f:
    line = line.strip()
    words = line.split(' ')
    # print(type(words))  # <class 'list'>
    for word in words:
        if word == 'itheima':
            count += 1
print(count)


# 关闭文件
f.close()




