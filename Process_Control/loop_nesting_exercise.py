# 练习1：
#   打印99乘法表
#   1*1=1
#   1*2=2 2*2=4
#   1*3=3 2*3=6 3*3=9
#   ...                 9*9=81
# 创建一个循环来控制图形的高度
"""i = 1
while i <= 9:
    # 创建一个内层循环来控制图形的宽度
    j = 1
    while j <= i:
        print(j, '*', i, '=', i*j, ' ', end='')
        j += 1
    print('')
    i += 1
"""
i = 0
while i <9:
    i += 1
    # 创建一个内层循环来控制图形的宽度
    j = 0
    while j < i:
        j += 1
        # print(j, '*', i, '=', i*j, ' ', end='')
        print(f'{j}*{i}={i*j} ', end='')
    print('')
# 求100以内所有的质数
# 创建一个循环，求1-100以内所有的数
i = 2
while i <= 100:
    # 创建一个变量，记录i的状态，默认认为i是质数
    flag = True
    # 判断i是否是质数
    # 获取所有可能成为i的因数的数
    j = 2
    while j < i:
        # 判断i能否被j整除
        if i % j ==0:
            # i能被j整除，证明i不是质数，修改flag为false
            flag = False
        j +=1
    # 验证结果并输出
    if flag:
        print(i)
    i += 1


