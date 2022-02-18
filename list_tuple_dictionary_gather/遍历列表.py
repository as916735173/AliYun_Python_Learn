# 遍历列表，指的就是将列表中的所有元素取出来
# 创建一个列表
stus = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']
print('原列表:', stus)
# 遍历列表:笨方法
print(stus[0])
print(stus[1])
print(stus[2])
print(stus[3])
print(stus[4])
print(stus[5])
# 创建一个while循环，来遍历列表
print('--------遍历开始-------')
i = 0
while i < len(stus):
    print(stus[i])
    i += 1
# 通过 for 循环来遍历列表
# for循环语法：
#    for 变量 in 序列:
#       代码块
# for 循环的代码块汇会执行多次，序列中有几个元素就会执行几次，
#   每执行一次就会将序列中的一个元素赋值给变量
print('--------遍历开始-------')
for s in stus:
    print(s)
