# 打开文件
file_name = 'demo.txt'

# 调用open()来打开文件
file_obj = open(file_name)

# 当我们获取了文件对象以后，所有的对文件的操作都应该通过对象来进行
# 读取文件中的内容
# read()方法，用来读取文件中的内容，他会将内容全部保存为一个字符串返回

content = file_obj.read()

print(content)

# 关闭文件
# 调用close()方法关闭文件
# file_obj.close()
# file_obj.read()

# with...as语句
with open(file_name) as file_obj:
    # 在with 语句中可以直接使用 file_obj 来做文件操作
    # 此时这个文件只能在 with 中使用，一旦 with 结束则文件会自动 close()
    print(file_obj.read())
file_name = 'hello'

try:
    with open(file_name) as file_obj:
        print(file_obj.read())
except  FileNotFoundError:
    print(f'{file_name}文件不存在~~')
