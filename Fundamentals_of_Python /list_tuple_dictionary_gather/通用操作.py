# 创建一个列表
stus = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']
# + 和 *
# + 可以讲两个列表拼接为一个列表
# * 可以将列表重复指定的次数
my_list = [1, 2, 3] + [4, 5, 6]
print(my_list)
# in 和 not in
# in 用来检查指定元素是否存在于列表中
#   如果存在，反悔True，否则返回False
# not in 用来检查指定元素是否不存在于列表中
#   如果不存在，反悔True，否则返回False
print('沙和尚' in stus)
print('牛魔王' in stus)
print('沙和尚' not in stus)
print('牛魔王' not in stus)
# len()获取列表中的元素的个数
# min()获取列表中的最小值
# max()获取列表中的最大值
arry = [10, 1, 2, 5, 100, 55, 76]
print(len(arry), min(arry), max(arry))
# 两个方法（method），方法和函数基本一样，只不过方法必须通过 对象.方法() 的形式调用
# xxx.print() 方法实际上就是和对象关系紧密的函数
# s.index() 获取指定元素在列表中的第一次出现的位置
# 如果要获取列表中没有的参数会抛出异常
print(stus.index('沙和尚'))
# index() 的第二个参数，表示查找的起始位置，第三个参数，表示查找的结束位置
stus = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精', '沙和尚', '沙和尚']
print(stus.index('沙和尚', 3, 7))
# s.count() 统计指定元素在列表中出现的次数
print(stus.count('沙和尚'), stus.count('牛魔王'))
