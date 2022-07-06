class A(object):
    def test(self):
        print('AAA')


class B(object):
    def test(self):
        print('B中的test方法~~~')
    def test2(self):
        print('8888')


# 在Python中是支持多重继承的，也就是我们可以为一个累同事指定多个父类
#   可以在类名后的()后边添加多个类，来实现多重继承
#   多重继承，会使子类同时用有多个父类，并且会获取到所有父类中的方法
# 在开发中没有特殊情况，应该尽量避免使用多重继承，因为多重继承会让我们的代码过于复杂
# 如果多个父类当中有同名的方法，则会先在第一个父类中寻找，然后找第二个，第三个，前面的会覆盖后面的
# class C(B):
#     pass
class C(B, A):
    pass


# 类名.__bases__这个属性可以用来获取当前类的所有父类
# print(C.__bases__)  # (<class '__main__.B'>,)
print(B.__bases__)  # (<class 'object'>,)
print(C.__bases__)  # (<class '__main__.A'>, <class '__main__.B'>)
c = C()
c.test()
c.test2()

