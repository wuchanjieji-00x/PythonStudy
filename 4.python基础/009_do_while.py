# -*- coding: utf-8 -*-

# while 循环

#计算100以内所有奇数之和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print (sum)

#计算1+2+3+...+100：
sum = 0
n = 1
while n <= 100:
    sum = sum +n
    n = n + 1
print (sum)

#计算1*2*3*...*100:
acc = 1
m = 1
while m <= 100:
    acc = acc * m
    m = m +1
print (acc)
