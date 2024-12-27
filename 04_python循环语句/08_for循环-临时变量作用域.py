"""
演示for循环中临时变量的作用域
"""
for i in range(5):
    print(i)
# print(i)  # 警告i可能没有被定义  # 实际上临时变量i可以访问到，但是不符合规范，不建议这样做
# python中，黄色为警告，红色为错误

# 那如果想要访问临时变量怎么办？那最好在循环外预先定义临时变量：
i = 0
for i in range(5):
    print(i)
print(i)