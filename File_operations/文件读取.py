# 打开文件
file_name = 'demo2.txt'
try:
    # 调用 open（）来打开一个文件，可以将文件分成两种类型
    #   一种，是纯文本文件（使用 utf-8 等编码编写的文本文件）
    #   一种，是二进制文件（图片，mp3，ppt 等这些文件）
    # open（）打开文件时是默认以文本文件的形式打开的，但是 open（）默认的编码为 none
    # 因此在处理文本文件时，必须要制定文件的编码,此时在后面带编码 utf-8 就可以打开文件。
    with open(file_name, encoding='utf-8') as file_obj:
        # 如果直接调用read()她会将文本文件中的所有内容全部都读取出来
        #   如果要读取的文件较大的话，会一次性将文件的所有内容加载到内存中，容易导致内存泄露
        #   所以对于较大的文件，不要直接调用read（）
        # help( ) 查看命令的帮助手册
        # read(size =n) 可以接收一个 n (整数类型)做为参数，作为每次读取的字符数量
        #   默认值为-1，他会读取文件中的所有字符
        #   可以为size指定一个值，这样read()会读取到指定数量的字符，每一次读取都是从上一次读取到的位置开始读取的
        #   如果字符的数量小于size，则会读取剩余所有的字符
        #   如果已经读取到了文件的最后了，则会返回''空串
        # 通过read()来读取文件中的内容
        # content = file_obj.read(-1)
        content = file_obj.read(6)
        content = file_obj.read(6)
        content = file_obj.read(6)
        content = file_obj.read(6)
        content = file_obj.read(6)
        content = file_obj.read(6)
        content = file_obj.read(6)
        content = file_obj.read(6)
        print(content)
        print(len(content))
except FileNotFoundError:
    print(f'{file_name}这个文件不存在')

# 读取大文件的方式
#   方法一
# file_name = 'demo3.txt'
# try:
#     with open(file_name, encoding='utf-8') as file_obj:
#         # 定义一个变量来指定每次读取的大小
#         chunk = 200
#         # 创建一个循环来读取文件
#         while True:
#             # 读取chunk大小的内容
#             content_z = file_obj.read(chunk)
#             # 检查是否读取到了内容
#             if not content_z:
#                 # 内容读取完毕，退出循环
#                break
#             # 输出内容
#             print(content_z, end='')
# except FileNotFoundError:
#     print(f'{file_name}这个文件不存在')
# 方法二
file_name = 'demo3.txt'
try:
    with open(file_name, encoding='utf-8') as file_obj:
        # 定义一个变量来保存文件的内容
        file_content_z = ''
        # 定义一个变量来指定每次读取的大小
        chunk = 200
        # 创建一个循环来读取文件
        while True:
            # 读取chunk大小的内容
            content_z = file_obj.read(chunk)
            # 检查是否读取到了内容
            if not content_z:
                # 内容读取完毕，退出循环
                break
            # 输出内容
            file_content_z += content_z
except FileNotFoundError:
    print(f'{file_name}这个文件不存在')

print(file_content_z)
