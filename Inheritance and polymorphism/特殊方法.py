# 特殊方法，也称为魔术方法
# 特殊方法都是以 __ 开头和结尾的
# 特殊方法一般不需要我们手动调用，需要在一些特俗情况下自动执行

# 定义一个Person类
class Person(object):
    """
    人类
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__() 这个特殊方法会在尝试讲对象转换为字符串的时候调用
    # 它的作用可以用来指定对象转换为字符串的结果
    def __str__(self):
        # return 'Hello Person!!!'
        return 'Person [name = %s, age = %d]' % (self.name, self.age)

    # __repr__() 这个特殊方法会在对当前对象使用repr() 函数时调用
    # 它的作用是指定对象在 '交互模式' 中直接输出的效果
    def __repr__(self):
        return 'Hello'

    # object._lt_(self,other) 小于<
    # object._le_(self,other) 小于等于<=
    # object._eq_(self,other) 等于==
    # object._ne_(self,other) 不等于!=
    # object._gt_(self,other) 大于>
    # object._ge_(self,other) 大于等于>=
    # __gt__会在对象做大于比较的时候调用，该方法的返回值将会作为比较的结果
    # 他需要两个参数，一个self表示当前对象，other表示和当前对象中比较的对象
    # self > other
    def __gt__(self, other):
        return self.age > other.age

    # __len__(self)获取对象的长度

    # object._bool_(self)
    # 可以通过 bool 来指定对象转换为布尔值的情况
    def __bool__(self):
        return self.age > 22

# object._add_(self,other) 加法运算 +
# object._sub_(self,other) 减法运算 -
# object._mul_(self,other) 乘法运算 *
# object._matmul_(self,other)
# object._truediv_(self,other)
# object._floordiv_(self,other)
# object._mod_(self,other)
# object._divmod_(self,other)
# object._pow_(self,other[,modulo])
# object._lshift_(self,other)
# object._rshift_(self,other)
# object._and_(self,other)
# object._xor_(self,other)
# object._or_(self,other)


# 创建两个Person类的实例
p1 = Person('孙悟空', 18)
p2 = Person('猪八戒', 22)

# 打印p1
# 当我们打印一个对象时，实际上打印的是对象中的特殊方法 __str__() 的返回值
# print(p1)  # <__main__.Person object at 0x109e91150>
print(p1)
print(repr(p2))
print(p1 > p2)
print(p2 > p1)
print(bool(p1))
if p1:
    print(p1.name, '已经成年了')
else:
    print(p1.name, '还未成年')
