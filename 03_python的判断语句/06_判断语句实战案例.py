"""
演示判断语句实战案例：终极猜数字
"""
# import random
# num = random.randint(1, 10)
# print(num)
#
# guess_num = int(input('请猜一个数字：'))
#
# if guess_num == num:
#     print('恭喜您，第一次就猜中了！')
#
# else:
#     if guess_num > num:
#         print('大了，请再猜一次：')
#     else:
#         print('小了，请再猜一次：')
#
#     guess_num = int(input('请再猜一个数字：'))
#     if guess_num == num:
#         print('恭喜您，这次猜中了！')
#     else:
#         if guess_num > num:
#             print('这次大了')
#         elif guess_num < num:
#             print('这次小了')
#
#     guess_num = int(input('最后一次机会，请猜一个数字：'))
#     if guess_num == num:
#         print('恭喜您，最后一次机会猜中了')
#
#     else:
#         print('三次机会用完了，没有猜中...')



# 123
#     else:
#         print('这次猜小了，请猜最后一次：')
#         if int(input()) == num:
#             print('恭喜您，最后一次机会，您终于猜对了！')
#         elif int(input()) > num:
#             print('不好意思，最后一次机会，这次您猜大了')
#         else:
#             print('不好意思，最后一次机会，您还是猜小了...')
#
# else:
#     print('小了，请再猜一次：')
#
#     if int(input()) == num:
#         print('恭喜您，第二次就猜中了！')
#
#     elif int(input()) > num:
#         print('这次大了，请猜最后一次：')
#         if int(input()) == num:
#             print('恭喜您，最后一次机会，您终于猜对了！')
#         elif int(input()) > num:
#             print('不好意思，最后一次机会，还是大了...')
#         else:
#             print('不好意思，最后一次机会，这次您猜小了...')
#     else:
#         print('还是小了，请猜最后一次：')
#         if int(input()) == num:
#             print('恭喜您，最后一次机会，您终于猜对了！')
#         elif int(input()) > num:
#             print('不好意思，最后一次机会，这次您猜大了...')
#         else:
#             print('不好意思，最后一次机会，您还是猜小了...')


# 方式3：
import random
num = random.randint(1, 10)
print(num)

guess_num = int(input('请猜一个数字：'))

if guess_num == num:
    print('恭喜您，第一次就猜中了！')

else:
    if guess_num > num:
        print('大了，请再猜一次：')

        guess_num = int(input('请再猜一个数字：'))
        if guess_num == num:
            print('恭喜您，这次猜中了！')
        else:
            if guess_num > num:
                print('还是大了')

                guess_num = int(input('最后一次机会，请猜一个数字：'))
                if guess_num == num:
                    print('恭喜您，最后一次机会猜中了')
                else:
                    print('三次机会用完了，没有猜中...')

            else:
                print('这次小了')

                guess_num = int(input('最后一次机会，请猜一个数字：'))
                if guess_num == num:
                    print('恭喜您，最后一次机会猜中了')
                else:
                    print('三次机会用完了，没有猜中...')
    else:  #guess_num < num:
        print('小了，请再猜一次：')

        guess_num = int(input('请再猜一个数字：'))
        if guess_num == num:
            print('恭喜您，这次猜中了！')
        else:
            if guess_num > num:
                print('这次大了')

                guess_num = int(input('最后一次机会，请猜一个数字：'))
                if guess_num == num:
                    print('恭喜您，最后一次机会猜中了')
                else:
                    print('三次机会用完了，没有猜中...')

            elif guess_num < num:
                print('还是小了')

                guess_num = int(input('最后一次机会，请猜一个数字：'))
                if guess_num == num:
                    print('恭喜您，最后一次机会猜中了')
                else:
                    print('三次机会用完了，没有猜中...')