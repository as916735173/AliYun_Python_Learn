# 继承

# 定义一个类 Animal (动物)
#   这个类中需要两个方法：run() sleep()
class Animal:
    def run(self):
        print('动物会跑~~~')

    def sleep(self):
        print('动物睡觉~~~')

    # ①
    # def bark(self):
    #     print('动物嚎叫~~~')


# 定义一个类 Dog（狗）
#   这个累需要三个方法：run() sleep() bark()
# ②
# class Dog:
#     def run(self):
#         print('狗会跑~~~')
#
#     def sleep(self):
#         print('狗睡觉~~~')
#
#     def bark(self):
#         print('狗嚎叫~~~汪汪汪')


# 有一个类，能够实现我们需要的大部分功能，但不能实现全部功能
# 如何能让这个类来实现全部的功能
#   ①直接最该这个类，在这个类中添加我们需要的功能
#       -修改起来比较麻烦，并且会违反ocp原则
#   ②直接撞见一个新的类
#       -创建一个新的类比较麻烦，并且需要大量的进行复制粘贴，会出现大量的重复性代码
#   ③直接从Animal类中来继承它的属性和方法
#       -继承是面向对象三大特性之一
#       -通过继承我们可以使一个类获取到其他类中的属性和方法
#       -在定义类时，可以在类名后的括号中指定当前类的父类（超类，基类，super）
#           子类（衍生类）
# 通过继承可以直接让子类获取到父类的方法或属性，避免编写重复性的代码，并且也符合ocp原则
# 所以我们京城需要通过继承来对一个类进行扩展

class Dog(Animal):
    def bark(self):
        print('狗嚎叫~~~汪汪汪')

    def run(self):
        print('狗跑~~~')


class Hashiqi(Dog):
    def fansha(self):
        print('这是一直憨憨的2哈')


d = Dog()
h = Hashiqi()
d.run()
d.sleep()
d.bark()
h.fansha()


# isinstance()检查一个类是否是一个类的实例
# r = isinstance(d, Dog)
# r2 = isinstance(d, Animal)
# print(r, r2)

# 在创建类时，如果省略了父类，则默认父类为object
# object 是所有类的父类，所有类都继承自 object
# class Person(object):
#     pass

# issubclass()检查一个类是不是另一个类的子类
print(issubclass(Dog, Animal))
print(issubclass(Animal, object))
print(issubclass(Person,object))
