# !/usr/bin/env python3
# -*- coding: utf-8 -*-


# 比如构造一个1, 3, 5, 7, ..., 99的列表，可以通过循环实现
L = [] # L是个List
n = 1
while n <= 99:
    L.append(n) # 将n添加到L中
    n = n + 2
print (L)
