"""
演示if_elif_else 多条件判断语句的使用
"""
# height = int(input('请输入您的身高(cm): '))
# vip_level = int(input('请输入您的VIP等级(1~5): '))
# day = int(input('请告诉我今天是几号：'))
#
# # 通过if判断，可以使用多条件判断的语法
# if height < 120:
#     print('您的身高未超过120cm，可以免费')
# elif vip_level > 3:
#     print('您的vip等级大于3，可以免费')
# elif day == 1:
#     print('今天是1号免费日，可以免费')
# else:
#     print('不好意思，条件都不满足，需要购票10元')
# print('祝您游玩愉快')

# 多条件判断下，各个条件是互斥的

# 将input写入判断条件中，节省代码量
# print('欢迎来到黑马游乐园')
# if int(input('请输入您的身高(cm): ')) < 120:
#     print('您的身高未超过120cm，可以免费')
# elif int(input('请输入您的VIP等级(1~5): ')) > 3:
#     print('您的vip等级大于3，可以免费')
# elif int(input('请告诉我今天是几号：')) == 1:
#     print('今天是1号免费日，可以免费')
# else:
#     print('不好意思，条件都不满足，需要购票10元')
# print('祝您游玩愉快')


# 练习
num = 10
if int(input('请输入第一次猜想的数字：')) == num:
    print('恭喜，一次就猜对了')
elif int(input('猜错了，再猜一次：')) == num:
    print('猜对了！')
elif int(input('猜错了，最后再猜一次：')) == num:
    print('恭喜，最后一次机会猜对了！')
else:
    print('sorry，全部猜错了，我想的是：10')

# if判断条件，各个条件之间互斥，但又是按照顺序来的


