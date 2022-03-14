# help()是python中的内置函数
# 通过help()函数可以查询Python中的函数的用法
# 语法：help(函数对象)
# help(print)  # 获取print()函数的使用说明
# Help on built-in function print in module builtins:
# print(...)
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
#
# Prints the values to a stream, or to sys.stdout by default.\
# Optional keyword arguments:
# file: a file - like object(stream);defaults to the current sys.stdout.
# sep: string inserted between values, default a space.
# end: string appended after the last value, default a newline.
# flush: whether to forcibly flush the stream.

# 文档字符串
# 在定义函数时，可以在函数内部编写文档字符串，文档字符串就是函数的说明
#   当我们边谢了文档字符串，就可以通过help()函数来查看函数的说明
#   文档字符串非常简单，其实直接在函数的第一行写一个字符串就是文档字符串
def fn(a: int, b: bool, c: str = 'hello') -> int:
    """
    这是一个文档字符串的实例

    函数的作用：。。。。。。。
    函数的参数：
        a,作用,类型,默认值。。。。。
        b,作用,类型,默认值。。。。。
        c,作用,类型,默认值。。。。。
    """
    return 10


help(fn)
