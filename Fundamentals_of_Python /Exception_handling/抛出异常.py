# 也可以自定义异常类，只需创建一个类继承 Exception 即可
class MyError(Exception):
    pass

def add(a, b):
    # 如果a和b中有负数，就向调用处抛出异常
    if a < 0 or b < 0:
        # raise 用于向外部抛出异常，后面可以跟一个异常类或者异常类的实例。
        # raise Exception
        # 我们抛出异常的目的，是告诉外部此处存在问题，希望引起注意并加以处理。此处抛出目的仅仅是抛出异常而不处理异常结果。
        # raise Exception('两个参数中不能有负数')
        raise MyError('自定义的异常')
        # 也可以通过 if else 来代替异常的处理
        # return None
    r = a + b
    return r


print(add(-123, 456))
