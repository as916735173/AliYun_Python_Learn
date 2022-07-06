# # 可变对象
# a = [1, 2, 3]
# print('修改前：', a, id(a))
# # 通过索引修改列表
# a[0] = 10
# print('修改后：', a, id(a))
# # 为变量重性赋值
# a = [4, 5, 6]
# print('修改后：', a, id(a))
a = [1, 2, 3]
b = a
print('修改前：', a, id(a))
print('修改前：', b, id(b))
b[0] = 10
print('修改前：', a, id(a))
print('修改前：', b, id(b))
b = [10, 20, 30]
print('修改前：', a, id(a))
print('修改前：', b, id(b))
