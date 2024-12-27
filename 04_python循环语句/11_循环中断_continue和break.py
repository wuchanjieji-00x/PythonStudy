"""
演示循环中断控制，break和continue
"""
#  continue
# for i in range(1, 6):
#     print(1)
#     continue
#     print(2)  # 这个print不会被打印，且系统一直在提示有问题

# continue的嵌套使用，作用域
# for i in range(1, 6):
#     print(1)
#     for j in range(1, 6):
#         print(2)
#         continue  # 这个continue只作用在内层循环，不会影响外层
#         print(3) # 这个print不会被打印，且系统一直在提示有问题
#     print(4)

# 演示循环中断语句break
# for i in range(1, 100):
#     print(1)
#     break  # 直接game over，结束当前数据流的循环。也就是说，外层循环再次循环的时候，依然会进内层循环
#     print(2)
# print(3)

# break的嵌套使用：
for i in range(1, 6):
    print(1)
    for j in range(1, 6):
        print(2)
        break  # 直接game over，结束当前数据流的循环。也就是说，外层循环再次循环的时候，依然会进内层循环
        print(3)
    print(4)