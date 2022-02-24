# 比如有如下三行代码，这三行代码是一个完整的功能
# print('hello')
# print('你好')
# print('再见')
# 定义一个函数
def fn():
    print('这是第一个函数！')


# print(fn)  # <function fn at 0x10b5a0280>
# print(type(fn)) # <class 'function'>
# fn是函数对象，fn()是调用函数
# print是函数对象，print()是调用函数
fn()


# 定义一个函数，可以用来求任意两个数的和
# def sum():
#     a = int(input())
#     b = int(input())
#     print(a+b)
# sum()
def fn2(a, b):
    print(a + b)
