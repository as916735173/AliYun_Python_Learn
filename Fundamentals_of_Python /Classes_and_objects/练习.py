class Dog:
    """
        表示狗的类
    """

    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def jiao(self):
        """
            狗叫的方法
        :return:
        """
        print('汪汪汪')

    def yao(self):
        """
            狗咬的方法
        :return:
        """
        print('啊呜，咬死你！')

    def run(self):
        """
            狗跑的方法
        :return:
        """
        print('%s 快乐的奔跑着！！！'%self.name)


d = Dog('旺财', 8, 'male', 30)
# print(d.name, d.age, d.gender, d.height)
# 目前我们可以直接通过 对象.属性 的方式来修改属性的值，这种方式导致对象中的属性可以随意修改，
#   非常的不安全，值可以任意修改，不论对错
# 现在需要一种方式来增强数据的安全性
#   1.数据不能任意修改（让你改才能改，不让改就不能动）
#   2.属性不能修改为任意的值（例如年龄不能是负数，必须要合法）
d.name = '大黄'
d.run()