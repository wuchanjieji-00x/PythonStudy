"""
字符串处理相关的工具模块
"""

def str_resverse(s):
    """
    反转输入的字符串
    :param s: 输入的字符出
    :return: 反转后的字符串
    """
    return s[::-1]

def substr(s, x, y):
    """
    功能是按照给定的下标完成给定字符串的切片
    :param s: 输入的字符串
    :param x: 切片的开始下标
    :param y: 切片的结束下标
    :return: 切片完成后的字符串
    """
    return s[x:y]


# 测试
if __name__ == '__main__':  # 防止该文件作为模块被导入的时候，测试模块也会被执行
    print(str_resverse('abcd')) # dcba

if __name__ == '__main__':
    print(substr('abcdefg', 2, 5))  # cde