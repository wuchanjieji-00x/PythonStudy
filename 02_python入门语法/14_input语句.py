"""
演示python中的input语句
获取键盘的输入信息
"""
# print('请告诉我你是谁？')
# name = input()
# print('GET!!!, 你是%s' % name)

# # print的提示信息可以放进input函数中
# name = input('请告诉我你是谁？')
# print('GET!!!, 你是%s' % name)


# # 输入数字类型
# num = input('请告诉我你的密码？')
# print('你的密码的类型是：', type(num))  # 你的密码的类型是： <class 'str'>
# # input函数默认获取的数据类型都是字符串

# # 如果需要其他类型，请自行转换
# num = input('请告诉我你的密码？')
# num = int(num)
# print('你的密码的类型是：', type(num))  # 你的密码的类型是： <class 'int'>



# 练习
user_name = input('请输入您的用户名称：')
user_type = input('请输入您的用户类型：')
print(f'您好：{user_name}, 您是尊贵的：{user_type}用户，欢迎您的光临！')