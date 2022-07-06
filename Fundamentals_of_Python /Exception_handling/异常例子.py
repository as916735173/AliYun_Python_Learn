print('hello')
try:
    # try中放置的是有可能出现错误的代码
    print(10 / 0)
except:
    # except中放置的是出错以后的处理方式
    print('哈哈出错了')
else:
    print('程序正常执行')
print('你好')
