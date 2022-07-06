# 质数练习第一次优化
# 模块，通过模块可以对Python进行扩展
# 引入一个time模块，来统计程序执行的时间
from time import *
# time()函数可以用来获取当前的时间，返回的单位是秒
# 获取程序开始的时间
# 优化前：
#   10000个数6.440781116485596 秒
# 优化后：
#   10000个数0.7861707210540771 秒
#源程序
# begin_time = time()
# i = 2
# while i <= 100:
#     flag = True
#     j = 2
#     while j < i:
#         if i % j == 0:
#             flag = False
#         j += 1
#     if flag:
#         # pass
#         print(i)
#     i += 1
# end_time = time()
# print('程序执行的花费了：', end_time - begin_time, '秒')

# 第一次优化
# begin_time = time()
# i = 2
# while i <= 100:
#     flag = True
#     j = 2
#     while j < i:
#         if i % j == 0:
#             flag = False
#             # 一旦进入判断，则证明i一定不是质数，此时内层循环没有继续执行的必要
#             # 使用break来退出内层的循环
#             break
#         j += 1
#     if flag:
#         # pass
#         print(i)
#     i += 1
# end_time = time()
# print('程序执行的花费了：', end_time - begin_time, '秒')

# 第二次优化
begin_time = time()
i = 2
while i <= 100000:
    flag = True
    j = 2
    while j <= i ** 0.5:
        if i % j == 0:
            flag = False
            # 一旦进入判断，则证明i一定不是质数，此时内层循环没有继续执行的必要
            # 使用break来退出内层的循环
            break
        j += 1
    if flag:
        pass
        # print(i)
    i += 1
end_time = time()
print('程序执行的花费了：', end_time - begin_time, '秒')
