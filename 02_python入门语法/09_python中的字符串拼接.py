# 字符串 字面量之间的拼接
print('学IT来黑马' + '月薪过万')

# 字符串字面量和字符串变量的拼接
name = '黑马程序员'
address = '建材城东路9院'
print('我是：' + name + '我的地址是：' + address)

# 错误代码示例
tel = 4006189090
print('我的电话是：' + tel)  # TypeError: can only concatenate str (not "int") to str
# 不能将int或float直接和str 或其他类型拼接