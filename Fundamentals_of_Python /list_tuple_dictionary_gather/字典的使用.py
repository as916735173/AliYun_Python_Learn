# 创建字典
# 使用{}
# 语法：{k1:v1, k2:v2, k3:v3}
# 使用dict()函数来创建字典
# 每一个参数都是一个键值对，参数名就是键，参数值就是值（这种方式创建的字典，key都是字符串）
d = dict(name='孙悟空', age=18, gender='男')
# 也可以将一个包含双值子序列的序列转换为字典
# 双值序列，序列中只有两个值，[1,2] ('a', 'b') 'ab'
# 子序列，如果序列中的元素也是序列，那么我们就称这个元素为子序列
# [(1,2),(3,4)]
d = dict([('name', '孙悟空'), ('age', 18)])
print(d, type(d))
# len()获取字典中的键值对的个数
print(len(d))
# in：检查字典中是否包含指定的键值对
# not in：检查字典中是否不包含指定的键值对
print('hello' in d)
print('hello' not in d)
# 获取字典中的值，根据键来获取值
# 语法：d[key]
print(d['name'])
# 当key是一个变量是可以不加引号，如下：
n = 'name'
print(d[n])
# 如果通过[]来获取值时，如果键不存在，会抛出异常--KeyError
# get(key[, default])该方法用来根据键来获取字典中的值
print(d.get('name'))
#   如果获取的键在字典中不存在，则会返回None
#   也可以制定一个默认值，来作为第二个参数，这样获取不到值时将会返回默认值
print(d.get('hello', '默认值'))

# 修改字典
# d[key] = value 如果key存在则覆盖，不存在则添加
d['name'] = 'sunwukong'  # 修改字典的key-value
d['address'] = '花果山'  # 向字典中中添加key-value
print(d)
# setdefault(key[, default])可以用来向字典中添加key——value
#   如果key已经存在于字典中，则返回key的值，不会对字典做任何操作
#   如果key不存在，择向字典添加这个key，并设置value
d.setdefault('name', '猪八戒')
print(d)
result = d.setdefault('hello', '默认值')
print(d)
print(result)
# update([other])
# 讲其他的字典中的key-value添加到当前字典中
d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {'d': 4, 'e': 5, 'f': 6}
# d1.update(d2)
# 如果有重复的key，后边的会替换当前的key
d3 = {'d': 4, 'e': 5, 'f': 6, 'a': 7}
d1.update(d3)
print(d1)
# print(d2)

# 删除，可以使用 del 来删除字典中的 key-value
d = {'a': 1, 'b': 2, 'c': 3}
del d['a']
del d['b']
print(d)
# popitem()
# 随机删除字典中的一个键值对，一般都会删除最后一个键值对
#   删除之后，他会将删除的key-value作为返回值返回
#   返回的是一个元组，元组中有两个元素，第一个元素是删除的key，第二个是删除的value
d = {'a': 1, 'b': 2, 'c': 3}
d.popitem()
result = d.popitem()
print(result)
# pop(key[,default])
# 根据key删除字典中的key-value
# 会将被删除的value返回
# 如果删除不存在的key，会抛出异常---popitem()删除一个空字典会抛出异常，del()删除一个不存在的键值对也会抛出异常
#   如果指定了默认值，在删除不存在的key时，不会报错，而是直接返回默认值
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
result1 = d.pop('d')
result2 = d.pop('z', '这是默认值')
print(result1, result2)

# clear()用来清空字典
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
result3 = d.clear()
print(result3)

# copy
# 该方法用于对字典进行浅复制
# 复制以后的对象，和原对象是独立的，修改一个不会影响另一个
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# d2 = d  # 这种不叫复制
d2 = d.copy()
print('d =', d, id(d))
print('d2 =', d2, id(d2))
d['a'] = 100
print('d =', d, id(d))
print('d2 =', d2, id(d2))
# 浅复制只会简单的复制对象内部的值，如果直也是一个可变对象，这个可变对象不会被复制
d = {'a': {'name': '孙悟空', 'age': 18}, 'b': 2, 'c': 3, 'd': 4}
d2 = d.copy()
d2['a']['name'] = '猪八戒'
print('d =', d, id(d))
print('d2 =', d2, id(d2))
