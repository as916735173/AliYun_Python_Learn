# 练习1：
#   求100以内的所有奇数之和
# 获取所有100以内数
"""i = 0
result = 0
while i < 100:
    i += 1
    # 判断是否是奇数
    if i%2!=0:
        result += i
print('result =', result)"""
# 获取100以内所有的奇数
i = 1
while i < 100:
    i += 2
    print(i)
# 练习2：
#   求100以内所有7的倍数的和，以及个数
i = 7
# 创建一个变量，来保存结果
result = 0
# 闯进一个计数器，用来记录循环执行的次数
# 计数器就是一个变量，专门用来记录次数的变量
count = 0
while i < 100:
    # 为计数器加1
    count += 1
    result += i
    i += 7
print('总和为：', result, '总个数为：', count)

# 练习3：
#   水仙花指数是指一个 n 位数（n>=3），它的每个位上的数字的n次幂只和等于它本身（例如：1**3+5**3+3**3=153）
#   求1000以内所有的水仙花数

# 获取1000以内的三位数
i = 100
while i < 1000:
    # 判断i是否是水仙花数
    # 假设，i的百位数是a，十位数是b，个位数是c
    # 求i的百位数
    a = i // 100
    # 求i的十位数
    # b = i // 10 % 10
    b = (i - a * 100) // 10
    # 求i的个位数
    # c = (i - a * 100) - b * 10
    c = i % 10
    if a**3 + b**3 + c**3 == i:
        print(i)
    i += 1

# 获取用户输入的任意数，判断其实否是质数
num = int(input('输入一个任意的大于1的整数：'))

# 判断num是否是质数，只能被1和他自身整除的数就是质数
# 获取到所有的可能整除num的整数
i = 2
# 创建一个变量，用来记录num是否质数，默认认为num是质数
flag = True
while i < num:
    # 判断num能否被i整除
    # 如果num能被i整除，则说明num一定不是质数
    if num % i == 0:
        # 一旦进入判断，则证明num不是质数，则需要将flag修改为false
        flag = False
    i += 1
if flag :
    print(num,'是质数')
else:
    print(num,'不是质数')
