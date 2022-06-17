# open(file, mode='r', ...)函数打开file并返回对应的文件对象
# 默认返回读取的文本内容
# 可指定mode用来写入文件而作为输出
file = open('/Users/admin/PycharmProjects/AliYun_Python_Learn/File_operations/demo.txt')
print(file.read())
file.close()  # 调用close方法关闭打开的IO

# open函数打开的文件属于IO操作，需要显式关闭，否则会造成系统资源占用
# 我们使用with...as 语句来让系统自动关闭打开的IO源
with open('/Users/admin/PycharmProjects/AliYun_Python_Learn/File_operations/demo.txt', 'r') as f:
    print(f.read())
# 'r'-->读取（默认值） 'w'-->写入，并且先截断文件
# 'x'-->排他性创建，如果文件已存在则失败 'a'-->写入，如果文件已存在则在末尾追加
# 'b'-->二进制模式  't'-->文本模式（默认） '+'打开用于更新（读取和写入）

# 列出目录下的内容
# os.listdir函数
# 返回一个文件名的列表，功能单一
import os

entries = os.listdir()
print(entries)
# os.scandir 函数
# 返回一个迭代器，元素包含了出文件名以外，还有文件类型、文件属性等信息。推荐使用
entries2 = os.scandir()
print(entries2)
entries2.close()
with os.scandir() as entries2:
    for entry in entries2:
        print(entry.name)
# 判断文件属性，过滤选择文件
from pathlib import Path

basepath = Path('/Users/admin/PycharmProjects/AliYun_Python_Learn/File_operations')
print(basepath)
files = (entry for entry in basepath.iterdir() if entry.is_file())
for item in files:
    print(item.name)
