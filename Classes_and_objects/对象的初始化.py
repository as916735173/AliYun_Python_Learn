class Person:
    print('Person代码块中的代码')

    # name = 'swk'
    # 在类中可以定义一些特殊方法（魔术方法）
    # 特殊方法都是以__开头，__结尾的方法
    # 特殊方法不需要我们自己调用,不要尝试去调用特殊方法
    # 特殊方法将会在特素的时刻自动调用
    # 学习特殊方法
    #   1.特殊方法什么时候调用
    #   2.特殊方法有什么作用
    # 创建对象的流程
    # p1 = Person()的运行流程
    # 1.创建一个变量
    # 2.在内存中创建一个新对象
    # 3.执行类的代码块中的代码（只在类定义的时候执行一次）
    # 4.__init__(self)方法执行
    # 5.将对象的id赋值给变量
    # init会在对象创建以后立即执行
    # init可以用来向新创建的对象中初始化属性
    # 调用类创建对象时，类后边的所有参数都会依次传递到init()中
    def __init__(self, name):
        # print('init方法被执行了~~')
        # print(self)
        # 通过self向新建的对象中初始化属性

        self.name = name

    def sey_hello(self):
        print('大家好，我是%s' % self.name)


# 目前来讲，对于Person来说name是必须的，并且每一个对象中的name属性基本上都不同
# 而我们现在是将name属性定义为对象以后，手动添加到对象中，这种方式很容易出现错误
# 我们希望用户在创建对象时，必须设置name属性，如果不设置对象讲无法创建
# 并且属性的创建应该是自动完成的，而不是在创建对象以后手动完成
# p1 = Person()
# # 当Person没有name属性时，可以手动添加
# p1.name = '孙悟空'
# p2 = Person()
# p2.name = '猪八戒'
#
# p1.sey_hello()
# p2.sey_hello()
p1 = Person('孙悟空')
p2 = Person('猪八戒')
p3 = Person('沙和尚')
p4 = Person('唐三藏')
# p1.__init__()  # 不要去调用
p1.sey_hello()
p2.sey_hello()
p3.sey_hello()
p4.sey_hello()