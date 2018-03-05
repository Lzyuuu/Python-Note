# Decorator Program

# Program 1 对坐标进行加减，并通过装饰器检测边界
# Coordinate Program Start
print('Program 1. Coordinate function')
# 定义坐标类
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Coord:" + str(self.__dict__)

one = Coordinate(100, 200)
two = Coordinate(300, 200)
three = Coordinate(-100, -100)

def wrapper(some_func):
    def checker(a, b):
        print('Call %s function' % some_func.__name__)
        if a.x < 0 or a.y < 0:
            a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
        if b.x < 0 or b.y < 0:
            b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
        ret = some_func(a, b)
        if ret.x < 0 or ret.y < 0:
            ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
        return ret
    return checker

@wrapper
def add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)

@wrapper
def sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)

print(sub(one, two))
print(add(one, three))


# Program 2 设计一个时间区间计算的装饰器，计算阶乘函数的运行时间
# Function Time Program Start
import time
import functools

print('========================')
print('Program 2. Function Time')

def timing(some_func):
    def caltime(*args, **kw):
        t1 = time.time()
        some_func(*args, **kw)
        t2 = time.time()
        print('Call %s function, use %f second' % (some_func.__name__, t2 - t1))
        return t2 - t1
    return caltime

@timing
def factorial(n):
    return functools.reduce(lambda x,y : x * y, range(1, n+1))

factorial(50)

# Program 3 设计一个带参数的装饰器
# 实际上是利用了二层嵌套，定义一个装饰加强器，来对装饰器进行加强，返回一个新的装饰器，再用新的装饰器处理函数
import time
import functools

print('========================')
print('Program 3')

def decomaker(arg):
    def decotiming(some_func):
        @functools.wraps(some_func)    # 如果注释掉此处则最后输出的函数名为 caltime ，目的是将some_func中的状态抓取出来赋予给装饰后的函数
        def caltime(*args, **kw):
            t1 = time.time()
            some_func(*args, **kw)
            t2 = time.time()
            if arg == 's':
                print('Call %s function, use %f s' % (some_func.__name__, t2 - t1))
            elif arg == 'ms':
                print('Call %s function, use %f ms' % (some_func.__name__, 1000*(t2 - t1)))
            else:
                print('ERROR')
            return t2 - t1
        return caltime
    return decotiming

@decomaker('s')
def factorials(n):
    return functools.reduce(lambda x, y : x * y, range(1, n+1))

factorials(50)
print(factorials.__name__)