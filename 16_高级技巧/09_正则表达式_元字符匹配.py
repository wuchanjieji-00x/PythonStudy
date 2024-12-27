'''
演示python正则表达式使用元字符进行匹配
'''
import re

s = "itheima1 @@ python2 !!666 ## itccast3"

# 字符串前面带上r标记，表示字符串中转义字符无效，就是普通字符的意思
# result1 = re.findall(r'\d',s)
# result2 = re.findall(r'\W',s)
# result3 = re.findall(r'[a-zA-Z]',s)
# result4 = re.findall(r'[0-9]',s)
# result5 = re.findall(r'[5-7]',s)
# result6 = re.findall(r'[b-eF-Z3-6]',s)
# print(result6)

# 匹配账号，只能由字母和数字组成，长度限制6到10位
# r = r'^[0-9a-zA-Z]{6,10}$'
# s = '1234aHbxG'
# print(re.findall(r,s))

# 匹配QQ号，要求纯数字，长度5-11，第一位不为0r = r'^[1-9][0-9]{4,10}$'
# # s = '1546425'
# # print(re.findall(r,s))
#


# 匹配邮箱地址，只允许qq,163,gmail这三种邮箱地址
# {内容}.{内容}.{内容}.@{内容}.{内容}.{内容}.{内容}.
r1 = r'^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$'
r2 = r'(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)'
# [\w-] ： a-zA-Z0-9_ 和- 字符（集合）
# [\w-]+: 前面的字符（a-zA-Z0-9_-）至少出现一次，也就是至少一个字符
# (\.[\w-]+)* : .{内容} 出现0次或无数次
# @ ： @字符
# (qq|163|gmail) ： 供应商域名限制，或的关系（集合）
# (\.[\w-]+)+ ：.{内容} 出现1次或无数次
# ^r$ : 从字符串开头到结尾遍历
# (^r$) : 将规则作为一个整体
# r'' : 转义无效
s = 'a.b.c.d.e.f.g@qq.com.a.z.c.d.e'
print(re.findall(r2,s))  # findall函数会把所有()内的都作为输出单独输出
print(re.match(r2,s))    # 这里用match比较好