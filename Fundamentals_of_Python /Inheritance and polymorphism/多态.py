# 多态是面向对象的三大特征之一
# 多态从字面上理解是多种形态
# 狗（狼狗，藏獒，哈士奇，边牧。。。。。）
# 一个对象可以以不同的形态去呈现


# 定义两个类
class A:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class B:
    def __init__(self, name):
        self._name = name

    def __len__(self):
        return 10

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class C:
    pass


a = A('孙悟空')
b = B('猪八戒')
c = C()


# 定义一个函数
# 对于say_hello() 这个函数来说，只要对象中含油name属性，他就可以作为参数传递
#   这个函数并不会考虑对象的类型，只要有name属性即可
def say_hello(obj):
    print('你好 %s' % obj.name)


# say_hello(c)


# 在say_hello_2()中我们做了一个类型检查，也就是只有obj是A类型的对象时，才可以正常使用
#   其他类型的对象都无法使用该函数，这个函数就违反了多态
# 违反了多态的函数，只适用于一种类型的对象，无法处理其他类型对象，这样导致函数的适应性非常的差
def say_hello_2(obj):
    # 做类型检查
    if isinstance(obj, A):
        print('你好 %s' % obj.name)


# say_hello_2(a)


# 鸭子类型
# 如果一个东西，走路像鸭子，叫声像鸭子，那么他就是鸭子
# len()
# 之所以一个对象能通过len()来获取长度，是因为对象中具有一个特殊方法__len__
# 换句话说，只要对象中具有__len__特殊方法，就可以通过len()来获取他的长度
l = [1, 2, 3]
s = 'hello'
print(len(l))
print(len(s))

print(len(b))
# 面相对象的三大特征
#   封装
#       - 确保对象中的数据安全
#   继承
#       - 保证了对象的可扩展性
#   多态
#       - 保证了程序的灵活性，如果我们的方法、类型和概念绑定，函数的通用性将会降低，当具有了多态，函数便更加灵活。