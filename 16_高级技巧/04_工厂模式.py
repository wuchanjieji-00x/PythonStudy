


class Person:
    pass


class Worker(Person):
    pass

class Student(Person):
    pass

class Teacter(Person):
    pass

class PersonFactory:

    def get_person(self, p_type):
        if p_type == 'w':
            return Worker()
        elif p_type == 's':
            return Student()
        else:
            return Teacter()

person = PersonFactory()
worker = person.get_person('w')
student = person.get_person('s')
teacter = person.get_person('t')

# 这样的话，创建这三个实例对象的时候，使用的是统一入口，这是优点1
# 优点2就是：当子类的成员改变时，那么你一个一个的创建出的实例都需要改，但是通过工厂模式，你只需要改变工厂模式内部的逻辑就可以了
# 就相当于，对于同一个产品，如果是每个人都来生产一个自己的产品，那么当这个产品需要改变，那么大家手里的产品都需要改变，
# 但是如果这个产品是由工厂统一生产再销售給每个人的话，当这个产品需要做改变的话，那么只需要工厂改变生产线就可以了