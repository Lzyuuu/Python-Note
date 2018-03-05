def addone(some_func):          # 定义 addone 装饰器，对输入的函数得到的数值结果加一
    def inner(*args, **kw):     # 定义内嵌函数 inner ，最后是返回函数名，所以需要有内嵌函数的存在
        print('call %s()' % some_func.__name__)     # 接收装饰对象的函数名并打印输出
        ret = some_func(*args, **kw)        # 在内嵌函数中运行一次装饰对象函数
        return ret + 1          # 返回数值加一的值
    return inner                # 返回的是 inner 函数，因此需再次调用

@addone     # 语法糖， addone 装饰器
def add(x, y, z):
    return x + y - z

# 此处的 add 已经是装饰后的新函数
result = add(5, 6, 3)
print(result)