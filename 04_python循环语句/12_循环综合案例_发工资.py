

# import random
# # num = random.randint(1, 10)  # 生成随机数
# total = 10000
#
# for i in range(1, 21):  # 20名员工
#     num = random.randint(1, 10)  # 生成随机数作为绩效
#     # 这里是需要做判断，应该用判断语句而不是循环
#     if num < 5:  # 绩效低于5，下一位，continue进入下一次循环
#         print(f'员工{i}，绩效分{num}:不发工资，下一位。')
#         continue
#     else: # 绩效大于等于5，发放工资，余额减少
#         total -= 1000
#         print(f'向员工{i}发放工资1000元，账户余额还剩{total}元')
#         if total == 0:
#             print('工资发完了，下个月再来吧')
#             break

# 请feel这里continue和break放的位置
money = 10000
for i in range(1, 21):
    import random
    num = random.randint(1, 10)
    if num < 5:
        print(f'员工{i}，绩效分{num}:不发工资，下一位。')
        continue

    if money >= 1000:
        money -= 1000
        print(f'向员工{i}发放工资1000元，账户余额还剩{money}元')
    else:
        print('工资发完了，下个月再来吧')
        break


