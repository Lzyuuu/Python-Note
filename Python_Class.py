# Program Start
# 静态变量
class Static_car(object):
    type = 'car'
c1 = Static_car()
print('静态变量type:')
print('c1.type = ' + c1.type)
print('Static_car.type = ' + Static_car.type)

# 动态变量
class Init_car(object):
    type = 'car'

    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        print('创建了类')

c2 = Init_car('Lamborghini', 'yellow')
print(c2.type)
print(Init_car.type)
print('name:%s, colour:%s'%(c2.name, c2.colour))