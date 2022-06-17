# Python 与系统模块os
#  文件和目录操作回顾
#  Os.listdir：以文件名方式列出目录下的内容
#  Os.scandir：以迭代器方式列出目录下的内容
#  Os.makedir：创建目录，可使用嵌套路径
#  Os.rmdir：删除目录
#  Os.remove：删除文件
#  os模块常用函数
#  Os.name
#  Os.getcwd
#  Os.access
import os

print(os.name)
print(os.uname())
print(os.cpu_count())
print(os.getloadavg())
print(os.getcwd())
print(os.listdir())
print(os.chdir('data'))
print(os.listdir())
# access函数可以用来方便地检查读写权限
a1 = os.access('fileio.py', os.R_OK)
a2 = os.access('fileio.py', os.W_OK)
a3 = os.access('fileio.py', os.X_OK)
print(a1, a2, a3)