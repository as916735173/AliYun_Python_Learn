# sort()
# 该方法用来对列表中的元素进行排序
# sort()方法默认是直接比较列表中的元素的大小
# 在sort()可以接收一个关键字参数，key
#   key需要一个函数作为参数，当设置了函数作为参数
#   每次都会以列表中的一个元素作为参数来调用函数，并且使用函数的返回值来比较元素的大小
l = ['bb', 'aaaaa', 'c', 'dddd', 'eeeeee']
l.sort()
print(l)
l.sort(key=len)
print(l)
ll = [2, 5, '1', 3, '6', '4']
ll.sort(key=str)
print(ll)
ll.sort(key=int)
print(ll)

# sorted()
# 这个函数和sort()的用法基本一致，但是sorted()可以对任意对象的序列进行排序
#   并且使用sorted()排序不会影响原来的的对象，而是返回一个新对象

# lst = [2, 5, '1', 3, '6', '4']
lst = "128367501389531"
print('排序前：', lst)
sorted(lst, key=int)
print(sorted(lst, key=int))
print('排序后：', lst)
