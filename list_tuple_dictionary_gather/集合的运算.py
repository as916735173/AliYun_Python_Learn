# 在对两个集合进行运算时，不会影响原来的集合，而是返回一个运算结果
# 创建两个集合
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

# & 交集运算
result = s1 & s2
print('resulit =', result)  # resulit = {3, 4, 5}

# | 并集运算
result = s1 | s2
print('resulit =', result)  # resulit = {1, 2, 3, 4, 5, 6, 7}

# - 差集运算
result = s1 - s2
print('resulit =', result)  # resulit = {1, 2}

# ^ 异或集运算，获取只在一个集合中出现的元素
result = s1 ^ s2
print('resulit =', result)  # resulit = {1, 2, 6, 7}

# <= 检查一个集合是否是另一个集合的子集
#   如果a集合中的元素全部都在b集合中出现，那么a集合就是b集合的子集，b集合就是a集合的超集
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
result = a <= b
# result = {1, 2, 3} <= {1, 2, 3}  # True
# result = {1, 2, 3, 4, 5} <= {1, 2, 3}  # False
print('resulit =', result)  # resulit = True

# < 检查一个集合是否是另一个集合的真子集
# 如果超集b中含有子集a的所有元素，并且b中还有a中美有的元素，则b就是a的真超集，a是b的真子集
result3 = {1, 2, 3} < {1, 2, 3}  # False
result4 = {1, 2, 3} < {1, 2, 3, 4, 5}  # True

# >= 检查一个集合是否是另一个集合的超集
# > 检查一个集合是否是另一个集合的真超集
