# 返回值，返回值就是函数执行以后返回的结果
# 可以通过 return 来指定函数的返回值
# 可以直接使用函数的返回值，也可以通过一个变量來接收函数的返回值
def sums(*nums):
    # 定义一个变量，来保存结果
    result = 0
    # 遍历元组，并将元组中的数进行累加
    for n in nums:
        result += n
    print(result)


sums(123, 456, 789)


# return 后边跟什么值，函数就会返回什么值
# return 后边可以跟任意的对象，甚至可以是一个函数
def fn():
    # return 100
    def fn2():
        print('hello')

    return fn2  # 返回值也可以是一个函数


r = fn()  # 这个函数的执行结果就是它的返回值
r()


# print(r)
# print(fn())
# print(r)

# 如果仅仅写一个 return 或者不写 return ，则相当于return None
def fn21():
    # return
    a = 10
    return


r = fn21()
print(r)


# 在函数中，return后的代码都不会执行，return 一旦执行函数自动结束
def fn3():
    print('hello')
    return
    print('abc')


r = fn3()
print(r)


def fn4():
    for i in range(5):
        if i == 3:
            # break  # 用来退出当前循环
            # continue  # 用来跳过当次循环
            return
        print(i)
    print('循环执行完毕！')


fn4()


def sums1(*nums):
    # 定义一个变量，来保存结果
    result = 0
    # 遍历元组，并将元组中的数进行累加
    for n in nums:
        result += n
    return result
    # print(result)


r = sums1(123, 456, 789)
print(r)


def fn5():
    return 10


# fn5和fn5()的区别
print(fn5)  # fn5是函数对象，打印fn5实际是在打印函数对象  <function fn5 at 0x10e5000d0>
print(fn5())  # fn5()是在调用函数，打印fn5()实际上是在打印fn5()函数的返回值  10
