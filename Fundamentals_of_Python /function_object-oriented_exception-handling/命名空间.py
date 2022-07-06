# 命名空间(namespace)
# 命名空间指的是变量存储的位置，每一个变量都需要存储到指定的命名空间当中
# 每一个作用域都会有一个它对应的命名空间
# 全局命名空间用来保存全局变量，函数命名空间用来保存函数中的变量
# 命名空间实际上就是一个字典，是一个专门用来存储变量的字典
# locals()用来获取当前作用域的命名空间
# 如果在全局作用域中调用locals()则获取全局命名空间，如果在函数作用域中调用locals()则获取函数命名空间空间
# 返回的是一个字典
scope = locals()  # 当前命名空间
print(type(scope))
# print(scope)
a = 20
# print(a)
# print(scope['a'])
# 向scope中添加一个key-value
scope['c'] = 1000  # 向字典中添加key-value就相当于在全局重创建了一个变量（一般不建议这么做）
# print(c)


def fn4():
    a = 10
    # scope = locals()  # 在函数内部调用locals()会获取导函数的命名空间
    # scope['b'] = 20  # 可以通过scope来操作函数的命名空间，但是也是不建议这么做
    # globals()函数可以用来在任意位置获取全局命名空间
    global_scope = globals()
    print(global_scope)
    print(global_scope['a'])
    global_scope['a'] = 30
    # print(scope)


fn4()
