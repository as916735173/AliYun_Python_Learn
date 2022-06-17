print('异常出现前')
try:
    print(c)
    print(10/0)
# except NameError:
#     # 如果except后不跟任何的内容，则此时它会捕获到所有的异常
#     # 如果在except后跟着一个异常的类型，那么此时他只会不会捕获该类型的异常
#     print('出现 NameError 异常')
# except ZeroDivisionError:
#     print('出现 ZeroDivisionError 异常')
# except IndexError:
#     print('出现 IndexError 异常')
# except :
#     print('出现未知异常')
# exception 是所有异常类的父类，相当于 except，所以如果 except 后跟着 exception，也会捕获到所有异常。
#   在异常类后面跟着 as xx 此时 xx 就是异常对象
except Exception as e:
    print("未知异常", e, type(e))
# 运用 Finally 子句即无论是否出现异常，该子句都会执行，所以通常将必须执行的代码放在 finally 子句中。
finally:
    print('无论是否出现异常，该子句都会执行')
print('异常出现后')