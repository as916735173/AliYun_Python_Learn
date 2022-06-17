file_name = '/Users/admin/Downloads/测试图片.jpg'
# 读取模式
# t 读取文本文件（默认值),读取文本文件时， size 是以字符为单位的
# b 读取二进制文件,读取二进制文件时，size 是以字节为单位，文件过大，不宜一次性读取，需要分段读
with open(file_name, 'rb') as file_obj:
    # print(file_obj.read())
    # 将读取到到的内容写出来
    # 定义一个新文件
    new_name = 'aa.jpg'
    with open(new_name, 'wb') as new_obj:
        # 定义每次读取的大小
        chunk = 100
        while True:
            # 从已有的对象中读取数据
            content = file_obj.read(chunk)
            # 内容读取完毕，终止循环
            if not content:
                break
            # 将读取到的数据写入到新对象中
            new_obj.write(content)