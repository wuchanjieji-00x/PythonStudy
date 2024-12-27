"""
演示
"""
# 统计如下字符串中有几个字母a
name = 'itheima is a brand of itcast'

# 在循环外部定义一个计数变量
count = 0

# for 临时变量 in 序列：
#     循环代码
for x in name:
    if x == 'a':
        count += 1
    # print(f'{name}中共含有：{count}个字母a') # print语句写这里是不对的
print(f'{name}中共含有：{count}个字母a')
