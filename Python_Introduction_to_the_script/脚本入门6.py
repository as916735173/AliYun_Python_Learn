# 从多个文件读取内容
# fileinput模块用来从多个文件的流中读取内容
# 默认从脚本传入参数读取
# import fileinput
# for line in fileinput.input():
#     if fileinput.isfirstline():
#         print(f'\nReading {fileinput.filename()} ---')
#         print('---->', line, end='')
#     print()

# Shutil 的高阶文件操作
# Shutil 模块提供了移动、复制文件或目录的函数
# 还提供了压缩文件的函数
import shutil
# 移动、复制文件或目录
# shutil.copy('data/data.txt', 'data2.txt')
shutil.make_archive('data2', 'tar', 'data/')
