file_name = 'demo4.txt'
# 使用open打开文件时必须要指定打开文件所要做的操作（读，写，追加）
#   如果不指定操作类型，则默认是 读取文件 ，而读取文件时是不能向文件中写入的
# r 表示只读的
# w 表示是可写的--使用 w 来写入文件时，如果文件不存在会创建文件，如果文件存在则会截断文件，截断文件指删除原来文件中的所有内容
# a 表示追加内容
# x 用来新建文件，如果文件不存在则创建，存在则报错
# + 为操作符增加功能
#   r+ : 既可读又可写，文件不存在会报错
#   w+ : 在写的基础上增加读的功能
#   a+ : 在追加内容上变成可读的
with open(file_name, 'a', encoding='utf-8') as file_obj:
    # write()用来向文件中写入内容
    # 如果操作的是一个文本文件的话，则 write()需要穿第一个字符串作为参数
    # write( ) 可以分多次向文件中写入内容
    # 如果要传递非字符串的值时，需要调用 str 做一个类型转换
    # 并且 write( ) 写入不会自动换行，需要加入  \n
    file_obj.write('Hello World !\n')
    file_obj.write('Hello World !\n')
    file_obj.write('Hello World !\n')
    file_obj.write(str(123) + '123123\n')
    # write( ) 实际上有返回值，写入完成以后，该方法会返回写入的字符的个数
    r = file_obj.write(str(123)+'123123\n')
    print(r)