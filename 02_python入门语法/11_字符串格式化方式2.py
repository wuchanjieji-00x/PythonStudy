"""
演示第二种字符串格式化方式：f"占位"
"""

name = '传播智客'
setup_year = 2006
stock_price = 19.99
# f:format 格式化
message = f'我是{name}, 成立于：{setup_year}, 我今天的股价是：{stock_price}'
print(message)
# 不关心数据类型，不做精度控制