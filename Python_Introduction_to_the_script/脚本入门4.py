# 高级文件名搜索
# glob模块提供了Unix风格的路径名模式匹配
import glob

print(glob.glob('*.py'))
for file in glob.iglob('../**/*.py', recursive=True):
    print(file)

from datetime import datetime
from os import scandir
import os
from pathlib import Path

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

basepath = Path('/Users/admin/PycharmProjects/AliYun_Python_Learn/File_operations')
print(basepath)
files = (entry for entry in basepath.iterdir() if entry.is_file())
for item in files:
    print(item.name)


# 使用了日期格式话
def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%y-%m-%d')
    return formated_date


def get_files(path):
    dir_entries = scandir(path)
    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()
            print(f'{entry.name}\t Last Modified: {convert_date(info.st_mtime)}')


get_files('./')
# os.mkdir函数--可以嵌套多层路径，文件夹已存在会抛出异常
# os.mkdir('./data')
# os.mkdir('data/json')
# os.rmdir函数删除目录
os.rmdir('data/json')
# os.remove函数删除文件
os.remove('hello.py')
