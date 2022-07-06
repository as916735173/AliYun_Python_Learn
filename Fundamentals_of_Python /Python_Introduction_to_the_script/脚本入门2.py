# 类：一个模板，包含了数据和方法的定义
# 对象：实例化后称为对象，变得具体
# 属性：类中的变量
# 方法：类中的函数。shelf关键字作为参数的函数

class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks
e.tricks