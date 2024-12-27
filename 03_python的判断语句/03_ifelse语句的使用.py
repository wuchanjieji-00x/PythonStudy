"""
演示python中 if else 的组合判断语句
"""
# age = int(input('请输入您的年龄：'))  # 定义键盘输入，获取年龄数据
#
# if age >= 18:
#     print('您已成年，需要买票10元')
# else:
#     print('您未成年，可以免费游玩')
# print('祝您游玩愉快')



# 练习
print('欢迎来到黑马游乐园')
length = int(input('请输入您的身高(cm)：'))  # 定义键盘输入获取身高数据

if length > 120:
    print('您的身高超出120cm，游玩需要购买10元')
else:
    print('您的身高未超出120cm，可以免费游玩')

print('祝您游玩愉快')
