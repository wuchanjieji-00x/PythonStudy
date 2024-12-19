# -*- coding: utf-8 -*-

# 条件判断
hight = 1.75
wight = 80.5
bmi = 80.5 / (hight**2)
if bmi < 18.5:
    print('过轻')
elif bmi >= 18.5 and bmi < 25:
    print('正常')
elif bmi >=25 and bmi < 28:
    print('过重')
elif bmi >= 28 and bmi < 32:
    print('肥胖')
else: 
    print('严重肥胖')


# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')
