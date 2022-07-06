# 集合
# 用{}来创建集合
s = {1, 10, 2, 3, 4}  # <class 'set'>
print(s, type(s))
s3 = {1, 10, 2, 3, 4, 3, 4, 10}  # <class 'set'>
print('s3 =', s3, type(s3))
# s2 = {[1, 2, 3], [4, 5, 6]}
# print(s2, type(s2))  # TypeError: unhashable type: 'list'

s = {1, 10, 2, 3, 4}  # <class 'set'>
print(s, type(s))
# 使用set()函数来创建集合
s4 = set()  # 空集合
print(s4, type(s4))
s5 = set([1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5])
print(s5, type(s5))
s6 = set('hello')
print(s6, type(s6))
# 使用set()将字典转换为集合时，只包含字典中的键
s7 = set({'a': 1, 'b': 2, 'c': 3})
print(s7, type(s7))
# 创建集合
s8 = {'a', 'b', 1, 2, 3}
# 使用in 和 not in来检查集合中的元素
print('c' in s8)
# 使用len()来获取集合中的元素的个数
print(len(s8))
# add()向集合中添加元素
s8.add(10)
print(s8, type(s8))
# update()将一个集合中的元素添加到当前集合中
ss = set('hello')
s.update(ss)
print(s, type(s))
s.update((10, 20, 30, 40, 50))
print(s, type(s))
# update()可以传递序列或字典作为参数，字典只会使用键
s.update({10: 'ab', 20: 'bc', 100: 'cd', 1000: 'ef'})
print(s, type(s))
# pop()随机删除并返回一个集合中的元素
ss1 = {'h', 1, 2, 3, 4, 100, 40, 1000, 10, 'e', 50, 20, 'o', 30, 'l'}
# result = ss1.pop()
# print(ss1)
# print(result)
# remove()删除集合中的指定元素
ss1.remove(100)
print(ss1)
# clear()清空集合
ss1.clear()
print(ss1)
# copy()对集合进行浅复制
