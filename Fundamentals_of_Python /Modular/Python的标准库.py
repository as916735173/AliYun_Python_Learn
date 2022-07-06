# 开相即用
# 为了实现开箱即用的思想，Python中为我们提供了一个模块的标准库
# 在这个标准库中，有很多很强大的模块我们可以直接使用
#   并且标准课会随着python的安装一同安装
# sys模块，他里面提供了一些变量和函数，使我们可以获取到Python解析器的信息，
#   或者通过函数来操作python解析器

# 引入sys模块
import sys

# sys.argv
# 获取执行代码时，命令行中所包含的参数
# 该属性是一个列表，列表当中保存了当前命令中的所有参数
# print(sys.argv)

# sys.modules
# 获取当前程序中引入的所有模块
# modules是一个字典，字典的可以是模块的名字，字典的value是模块对象
# print(sys.modules)

# pprint模块他给我们提供了一个方法 pprint() 该方法可以用来对打印的数据进行简单格式化
import pprint

# pprint.pprint(sys.modules)

# sys.path
# 他是一个列表，列表中保存的是模块的搜索路径
# pprint.pprint(sys.path)


# sys.platform
# 表示当前的运行平台
# print(sys.platform)

# sys exit() 函数用来退出程序
# sys.exit()
# print('hello')

# os模块让我们可以对操作系统进行访问
import os
# os.environ()通过改属性可以获取到系统的环境变量
# pprint.pprint(os.environ)
pprint.pprint(os.environ['PATH'])

# os.system() 可以用来执行操作系统的命令
os.system('ls')
