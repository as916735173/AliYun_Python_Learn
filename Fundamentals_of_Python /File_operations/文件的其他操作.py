import os
from pprint import pprint
# os.listdir()
#   获取指定目录的目录结构，需要一个路径作为参数，会获取到该路径下的目录结构，默认路径为 .
#   当前目录，该方法会返回一个列表，目录中的每一个文件（夹）的名字都是列表中的一个元素
r1 = os.listdir()
pprint(r1)
# os.getcwd()
#   获取当前所在的目录
r2 = os.getcwd()
pprint(r2)
# os.chdir()
#   切换当前所在的目录，作用相当于 cd
r3 = os.chdir('../..')
r2 = os.getcwd()
pprint(r2)
# os.mkdir()
#   创建目录
# 在当前目录下创建一个名字为 aaa 的目录
# os.mkdir('xxx')
# os.rmdir()
# 删除目录
# os.rmdir('xxx')
# os.remove()  删除文件
# open('aa.txt', 'w')
# os.remove('aa.txt')
# os.rename(‘旧名字’, ‘新名字’)
#   可以对一个文件进行重命名，也可以用来移动一个文件
# 重命名文件
# os.rename('aa.txt', 'bb.txt')
# 移动文件
os.rename('bb.txt', '/Fundamentals_of_Python /File_operations/bb.txt')
