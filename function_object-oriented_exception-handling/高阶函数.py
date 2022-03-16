# 高阶函数
# 接收函数作为参数，或者将函数作为返回值的函数是高阶函数
# 当我们使用一个函数作为参数时，实际上是将指定的代码传递进了目标函数

# 创建一个列表
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 定一个函数:普通函数
#   可以讲指定列表中的所有偶数，保存到一个新列表中

# def fn(lst):
#     """
#         fn()函数可以讲指定列表中的的所有偶数，保存到一个新的列表中返回
#         参数：
#             list：要进行筛选的列表
#     """
#     # 创建一个新列表
#     new_list = []
#     # 对列表进行筛选
#     for n in lst:
#         # 判断n的奇偶
#         if n % 2 == 0:
#             new_list.append(n)
#     # 返回新列表
#     return new_list
#
#
# print(fn(l))


# 定义一个函数，用来检查一个任意的数字是否是偶数
def fn2(i):
    if i % 2 == 0:
        return True
    return False


# 这个函数用来检查指定的数字是否大于5
def fn3(i):
    if i > 5:
        return True
    return False


def fn(func, lst):
    """
        fn()函数可以讲指定列表中的的所有偶数，保存到一个新的列表中返回
        参数：
            list：要进行筛选的列表
    """
    # 创建一个新列表
    new_list = []
    # 对列表进行筛选
    for n in lst:
        # 判断n的奇偶
        if func(n):
            new_list.append(n)
    # 返回新列表
    return new_list


# 这个函数用来检查指定的数字是否大于5
def fn4(i):
    if i % 3 == 0:
        return True
    return False


print(fn(fn4, l))

# filter()
# filter()可以从序列中过滤出符合条件的元素，保存到一个心得序列中
# 参数：
#   1.函数，根据该函数来过滤序列（可迭代结构）
#   2.需要过滤的序列（可迭代结构）
# 返回值：
#   过滤后的新序列（可迭代的结构）


# fn4是作为参数传递进filter()函数中
#   而fn4实际上只有一个作用，就是作为filter()的参数
#   filter()调用完毕以后，fn4就已经没有作用



# 使用方法一
print(list(filter(fn4, l)))
# 使用方法二
r = filter(fn4, l)
print(list(r))
