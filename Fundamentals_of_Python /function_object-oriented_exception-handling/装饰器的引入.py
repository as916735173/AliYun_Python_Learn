# 创建几个函数
def add(a, b):
    """
    求任意两个数的和
    """
    result1 = a + b
    return result1


def mul(a, b):
    """
    求任意两个数的积
    """
    result2 = a * b
    return result2


# 希望函数可以在计算前，打印开始计算，计算结束后打印计算完毕
#   我们可以直接通过修改函数中的代码来完成这个需求，但是会产生以下一些问题
#   ①如果要修改的函数过多，修改起来会比较麻烦
#   ②并且不方便后期维护
#   ③并且这样做会违反开闭原则（OCP）
#       程序的设计，要求开放对程序的扩展，要关闭对程序的修改
# r = add(123, 456)
# print(r)
# r = mul(123, 456)
# print(r)


# 我们希望在不修改原函数的情况下，来对函数进行扩展
def fn():
    print('我是fn函数....')


# 只需要根据现有的函数，来创建一个新的函数
# def fn2():
#     print('函数开始执行....')
#     fn()
#     print('函数执行结束....')


# fn2()


# def new_add(a, b):
#     print('函数开始执行....')
#     r = add(a, b)
#     print('函数执行结束....')
#     return r


# r = new_add(123, 456)


# print(r)


# 上边的方式，已经可以在不修改代码的情况下对函数进行扩展了
#   但是，这种方式要求我们每扩展一个函数就要手动创建一个心得函数，实在是太麻烦了
#   为了解决这个问题，我们创建一个函数，让这个函数可以自动的帮助我们生产函数

def begin_end(old):
    """
    用来对其他函数进行扩展，使其他函数可以在执行前打印开始计算执行，执行后打印执行结束
    参数：
        old 是要扩展的函数
    """

    # 创建一个新函数
    # 第一种使用方法
    # def new_function():
    #     print('函数开始执行....')
    #     # 调用被扩展的函数
    #     old()
    #     print('函数执行结束....')
    # 第二种使用方法
    def new_function(*args, **kwargs):
        print('函数开始执行....')
        # 调用被扩展的函数
        result = old(*args, **kwargs)
        print('函数执行结束....')
        return result

    # 返回新函数
    return new_function


# f = begin_end(fn)

# f
f = begin_end(fn)
f2 = begin_end(add)
f3 = begin_end(mul)
r = f2(123, 456)
r2 = f3(123, 456)
print(r, r2)


# 像begin_end()这种函数我们就称它为装饰器
#   通过装饰器，可以在不修改原来函数的情况下来对函数进行扩展
#   在开发中，我们都是通过装饰器来扩展函数的功能的
# 在定义函数时，可以通过@XXX（装饰器），来使用指定的装饰器，来装饰当前函数，
#   可以同时为一个函数指定多个装饰器，这样函数将会按照有内到位的顺序装饰
# 以下为装饰器的典型用法

# 定义一个新的装饰器
def fn4(old):
    """
    用来对其他函数进行扩展，使其他函数可以在执行前打印开始计算执行，执行后打印执行结束
    参数：
        old 是要扩展的函数
    """

    def new_function(*args, **kwargs):
        print('fn4装饰开始执行....')
        # 调用被扩展的函数
        result = old(*args, **kwargs)
        print('fn4装饰执行结束....')
        return result

    # 返回新函数
    return new_function


# 先使用begin_end装饰，然后用fn4进行装饰
@fn4
@begin_end
def say_hello():
    print("你好！")


say_hello()
