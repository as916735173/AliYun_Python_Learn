# 创建元组
# 使用()来创建元组
# 创建了一个空元组
my_tuple = ()
print(my_tuple, type(my_tuple))  # <class 'tuple'>
# 创建一个包含5个元素的元组
my_tuple = (1, 2, 3, 4, 5)
# 元组是不可变对象，不能尝试为元组中的元素重新赋值
# my_tuple[3] = 10 # TypeError: 'tuple' object does not support item assignment
print(my_tuple)

# 当元组不是空元组时，括号可以省略
# 如果元组不是空元组，它里边至少要有一个逗号 ','
my_tuple = 10, 20, 30, 40
my_tuple = 40,
print(my_tuple, type(my_tuple))

my_tuple = 10, 20, 30, 40
# 元组的解包(解构)
# 解包指的就是将元组当中每一个元素都赋值给一个变量
a, b, c, d = my_tuple
print('a =', a)
print('b =', b)
print('c =', c)
print('d =', d)

a = 100
b = 300
print('a =', a, 'b =', b)
# 交互a 和 b的值，这时我们就可以利用元组的解包
a, b = b, a
print('a =', a, 'b =', b)
# 在对一个元组进行解包时，变量的数量必须和元组中的元素的数量一致
# 也可以在变量前边添加一个*，这样变量将会获取元组中所有剩余的元素
my_tuple = 10, 20, 30, 40
a, b, *c = my_tuple
print(a, b)
a, *b, c = my_tuple
print('a =', a)
print('b =', b)
print('c =', c)
*a, b, c = my_tuple
print('a =', a)
print('b =', b)
print('c =', c)
# 不能同时出现两个或以上的*变量
# 会报错：SyntaxError: multiple starred expressions in assignment
# *a, *b, c = my_tuple
*a, b, c = 'hello world'
print('a =', a)
print('b =', b)
print('c =', c)
