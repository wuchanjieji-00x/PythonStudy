"""
数据定义的类
"""

class Record:

    def __init__(self, date, order_id, money, province): # 魔术方法：构造方法
        # 定义并赋值成员变量
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province

    def __str__(self):  # 修改成字符串，直接print内容，而非内存地址
        return f'{self.date}, {self.order_id}, {self.money}, {self.province}'