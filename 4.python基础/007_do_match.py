# -*- coding: utf-8 -*-

# 模式匹配

# if 语句
# score = 'B'
# if score == 'A':
#     print ('score is A.');
# if score == 'B':
#     print ('score is B.');
# elif score == 'C':
#     print ('score is C.');
# else:
#     print ('invalid score')


# 模式匹配
# score = 'B'

#match score:  # 这里为什么会报错？ match函数写的不对吗？ 版本的问题，升级版本
#    case 'A':
#        print ('score is A.')
#    case 'B':
#        print ('score is B.')
#    case 'C':
#        print ('score is C.')
#    case _: # _表示匹配到其他任何情况
#        print ('invalid score')


# 复杂匹配
age = 15
match age:
    case x if x  < 10:
        print (f'< 10 years old: {x}')
    case 10:
        print ('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print ('11~18 years old.')
    case 19:
        print ('19 years old.')
    case _:
        print ('not sure')

# 匹配列表
