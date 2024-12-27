"""
演示
"""

# import random
# num = random.randint(1, 100)
# print(num)
#
# guess_num = int(input('请猜一个数字： '))
# guess_times = 1
#
#
# while guess_num != num:
#
#     if guess_num > num:
#         print('您猜大了')
#     else:
#         print('您猜小了')
#     guess_num = int(input('请再猜一个数字： '))
#     guess_times += 1
#     # print(guess_num)
# print(f'恭喜您，猜对了，您一共猜了{guess_times}次！')


# 黑马方式：

# 获取1~100内的随机数字
import random
num = random.randint(1, 100)
# 定义一个变量，记录总共猜了多少次
count = 0

# 通过一个布尔类型的变量，做循环是否继续的标记
flag = True

while flag:
    guess_num = int(input('请猜一个数字：'))
    count += 1

    if guess_num == num:
        print('恭喜您，猜中了！')
        flag = False
    else:
        if guess_num > num:
            print('您猜大了...')
        else:
            print('您猜小了...')
print(f'您一共猜了{count}次')



