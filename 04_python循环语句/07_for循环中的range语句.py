"""
演示python中的range语句
"""

# range语法1：  range(num):从0开始到num结束，不包含num本身, 一个数字序列
# for x in range(10):
#     print(x)

# ragne语法2：range(num1, num2): 从num1开始，到num2结束，不包含num2，步长（步进）默认为1, 一个数字序列
# for x in range(5, 10):
#     print(x)

# range语法3：range(num1,num2,step): 从num1开始，到num2结束，不包含num2, 步长（步进）为step，一个数字序列
# for x in range(5, 10, 2):
#     print(x)


# 通过range快速的确定我们for循环要执行的次数
# i = 1
# while i <= 5:
#     print('送花')
#     i += 1
# 等价于
# for x in range(5):
#     print('送花')


# 练习
num1 = 1
num2 = 100
count = 0
for x in range(num1, num2):
    if x % 2 == 0:
        count += 1
print(f'{num1}到{num2}(不含{num2}本身)范围内，有{count}个偶数')
