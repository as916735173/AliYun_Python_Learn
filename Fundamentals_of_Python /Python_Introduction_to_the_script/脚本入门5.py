# tarfile 模块用来处理TAR文件
import tarfile
# 添加文件到压缩包
with tarfile.open('src.tar.gz', mode='w:gz') as tar:
    tar.add('hello.py')
    tar.add('fileio.py')
# 读取压缩包文件列表，并打印
with tarfile.open('src.tar.gz', mode='r:gz') as tar:
    for member in tar.getmembers():
        print(member.name)