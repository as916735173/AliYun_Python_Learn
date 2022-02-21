# ==  !=  is   is not
# ==  != 比较的事对象的值是否相等
# is  is not 比较的是对象的id是否相等（比较两个对象是否是同一个对象）
a = [1, 2, 3]
b = [1, 2, 3]
print(a, b)
print(id(a), id(b))
print(a == b)  # a和b的值相等，使用==会反悔Ture
print(a is b)  # a和b不是同一个对象，内存地址不同，使用is会返回False
