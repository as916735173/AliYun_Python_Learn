# 匿名函数 lambda 函数表达式(语法塘)
#   lambda函数表达式专门用来创建一些简单的函数，他是函数创建的又一种方式
#   语法：
#       lambda 参数列表 : 返回值
#       匿名函数一般都是作为参数使用，其他地方一般不会使用
def fn5(a, b):
    return a + b


print(fn5(123, 456))
# 等价于上面fn5函数
# lambda a, b: a + b
# 调用
print((lambda a, b: a + b)(123, 456))
# 也可以将一个匿名函数赋值给一个变量，但是一般不这么干
fn6 = lambda a, b: a + b
print(fn6(123, 456))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def fn4(i):
#     if i % 3 == 0:
#         return True
#     return False
# 等价于上面的函数
def fn4(i):
    return i % 3 == 0


# 等价于上面的
# lambda i : i % 3 ==0
r = filter(lambda i: i % 3 == 0, l)
print(list(r))

# map()
# map()函数可以对可迭代对象中的所有元素做指定的操作，然后将其添加到一个新对象中返回
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# r = map(lambda i: i+1, l)
r = map(lambda i: i**3, l)
print(r)
print(list(r))



