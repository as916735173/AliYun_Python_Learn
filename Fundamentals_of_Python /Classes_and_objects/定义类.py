# 尝试定义一个表示人的类
class Person:
    # 在类的代码中，我们可以定义变量和函数
    # 在类中我们所定义的变量，将会成为所有的实例的公共属性
    # 所有实例都可以访问这些变量
    a = 10
    b = 20
    name = 'swk'  # 公共属性，所有实例都可以访问

    # 在类中也可以定义函数，类中的定义的函数，我们称为方法
    # 这些方法可以通过该类的所有实例来访问
    def say_hello(self):
        # 方法每次被调用时，解析器都会自动传递一第一个实参
        # 第一个参数就是调用方法的对象本身
        #   如果是p1调的，则第一个参数就是p1对象
        #   如果是p2调的，则第一个参数就是p2对象
        # 一般我们都会将这个参数命名为self
        # print(self)
        # print('你好！')
        print('你好，我是%s'%self.name)

# 创建Person的实例
p1 = Person()
p2 = Person()
print(p1.a, p2.b)
# 调用方法，对象.方法名()
# 方法调用和函数调用的区别
# 如果是函数调用，则调用时传几个参数，就会有几个实参
# 但是如果是方法调用，默认传递一个参数，所以方法中至少要定义一个形参
# p1.say_hello()
# p2.say_hello()
# 修改p1的name属性
p1.name = 'zbj'
p2.name = 'shs'
# print(p1)
# print(p2)
p1.say_hello()
p2.say_hello()
print(p1.name, p2.name)
