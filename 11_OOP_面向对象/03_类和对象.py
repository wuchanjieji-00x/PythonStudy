"""
演示类和对象的关系，即面向对象的编程思想
"""

# 设计一个闹钟类：
class clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)

# 构建两个闹钟对象并使其工作
clock1 = clock()
clock1.id = '003032'
clock1.price = 19.99
print(f'闹钟ID：{clock1.id}, 闹钟价格：{clock1.price}')
clock1.ring()


# 有了类之后，随便你构建对象，多少个对象都行，最后干活的都是对象
# 就相当于你有了MEB平台，照理说，你可以基于这个平台任意设计车型
import time
time.sleep(3)

clock2 = clock()
clock2.id = '003032'
clock2.price = 19.99
print(f'闹钟ID：{clock2.id}, 闹钟价格：{clock2.price}')
clock2.ring()