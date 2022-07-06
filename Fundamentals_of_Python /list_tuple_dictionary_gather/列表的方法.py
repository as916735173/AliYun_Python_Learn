# 以下方法只适用于可变序列
# 创建一个列表
stus = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']
print('原列表:', stus)
# append()
# 列表的最后天加一个元素
stus.append('唐僧')
print('修改后', stus)
# insert()
# 向列表的的指定位置插入一个元素：仅插入不会删除覆盖
# 参数：
#       1.要插入的位置
#       2.要插入的元素
stus.insert(2, '唐三藏')
print('修改后', stus)
# extend()
# 使用新的序列来来扩展当前序列
# 需要一个序列作为参数，他会将该序列中的元素添加到当前序列中
stus.extend(['唐三藏', '黄飞虎'])  # 相当于：stus+=['唐三藏', '黄飞虎' ]
print('修改后', stus)
# clear()
# 清空序列
stus.clear()
print('修改后', stus)

stus = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']
print('原列表:', stus)
# pop()
# 根据索引删除并返回被删除的元素
# result = stus.pop(2)
# print('修改后：', stus, ' 删除了：', result)
result = stus.pop()  # 不输入索引则删除最后一个
print('修改后：', stus, ' 删除了：', result)
# remove()
# 删除指定值的元素，如果相同的值的元素有多个，则删除第一个
stus.remove('猪八戒')
print('修改后：', stus)
# reverse()
# 用来反转列表
stus.reverse()
print('修改后：', stus)
# sort()
# 用来对列表中的元素进行排序，默认升序排列
# 如果需要降序排列，需要传递一个 reverse=True 作为一个参数
my_list = list('agsdkwheoqdakdhka')
print('修改前', my_list)
my_list.sort()
print('修改后', my_list)
# 降序排列
my_list.sort(reverse=True)
print('修改后', my_list)

