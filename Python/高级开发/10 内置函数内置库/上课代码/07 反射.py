class Circle:
    def __init__(self):
        pass


class Rect:
    def __init__(self):
        pass


arr = []
c = Circle()
print('判断实例对象:', isinstance(arr, list))
print('判断实例对象:', isinstance(c, Circle))
print('判断实例对象:', isinstance(c, Rect))

import pprint

# globals 当前文件运行之后,全局环境变量里面的东西
pprint.pprint(globals())


def lambda_func():
    a = 10
    # locals 获取局部环境下的所有变量
    pprint.pprint(locals())


lambda_func()
# globals()['c'] = 1
