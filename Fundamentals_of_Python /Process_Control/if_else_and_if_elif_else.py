# 让用户在控制太重输入一个年龄
# age = input("请输入你的年龄：")
# age = int(age)
age = int(input("请输入你的年龄："))
# 如果用户的年龄大于18岁，则显示你已经成年了
if age >= 18:
    print("你已经成年了")
# if-else语句
# 语法
#   if 条件表达式：
#       代码块
#   else:
#       代码块
# 执行流程：
#   if-else语句在执行时，先对if后的条件表达式进行求职判断
#       如果为True，则执行if厚的代码块
#       如果为False，则执行else后的代码块
# age = 18
age = int(input("请输入你的年龄："))
if age > 17:
    print("你已经成年了！")
else:
    print("你还未成年！")
# if-elif-else语句
# 语法
#   if 条件表达式：
#       代码块
#   elif:
#       代码块
#   elif:
#       代码块
#   elif:
#       代码块
#   else:
#       代码块
# 执行流程：
#   if-elif-else语句在执行时，先自上向下依次对条件表达式进行求值判断
#       如果表达式的结果为True，则执行当前的代码块，然后语句结束
#       如果表达式的结果为False，则继续向下判断，直到找到True为止
#       如果所有的表达式的结果为False，
#age1 = 70
age1 = int(input("请输入你的年龄："))
if age1 > 200:
    print("活着可真没劲呢！")
elif age1 > 100:
    print("你也是老大不小了！")
elif age1 >= 60:
    print("你已经退休了！")
elif age1 >= 30:
    print("你已经是中年了！")
elif age1 >= 18:
    print("你已经成年了！")
else :
    print("你还是个小孩子！")
