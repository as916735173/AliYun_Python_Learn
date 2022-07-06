with open('demo4.txt', 'rb') as file_obj:
    print(file_obj.read(110))
    print(file_obj.read(30))
    # seek 和 tell 位置代表的是字节，如果读取的是utf-8是一个位置3个字节读取文件的位置.py
    # seek() 可以修改当前读取的位置
    file_obj.seek(55, 0)
    file_obj.seek(80, 1)
    # seek()需要两个参数
    #   第一个是要切换到的位置
    #   第二个是计算位置方式
    #       可选值：0 从头计算，1 从当前位置计算，2 从最后位置开始计算
    print(file_obj.read(2))
    # tell() 方法用来查看当前读取到的位置
    print('当前读取到了-->', file_obj.tell())