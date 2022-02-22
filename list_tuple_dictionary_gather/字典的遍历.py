# 遍历字典
# keys() 该方法会返回字典的所有的key
#   该方法会返回一个序列，序列中保存有字典的所有的键
# 通过遍历keys()来获取所有的键
d = {'name': '孙悟空', 'age': 18, 'gender': '男'}
print(d.keys())
for k in d.keys():
    print(k)  # 打印键
    print(d[k])  # 打印值
# values()
# 该方法会返回一个序列，序列中保存有字典的所有的值
for v in d.values():
    print(v)
# items()该方法会返回字典中所有的项
# 他会返回一个序列，序列中包含有双值子序列
# 双值分别是，字典中的key和value
print(d.items())
for k1, v1 in d.items():
    print(k1, '=', v1)
