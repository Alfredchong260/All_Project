"""
定义一个用户模型（User）
    属性：姓名，年龄

定义一个方法：watch_movie。方法接收一个用户，
调用方法后打印 用户姓名、年龄、正在看电影
"""


class User:
    """用户模型"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name


def decorator(func):
    def wrapper(*args, **kwargs):
        print(kwargs)
        # 18岁以下不准看
        if kwargs['user'].age >= 18:
            result = func(*args, **kwargs)
            return result
        else:
            # raise
            raise Exception(f"{kwargs['user'].name} 18 岁以下不准看")

    return wrapper


# 18 岁以下的不能看电影
@decorator
def watch_movie(user=None):
    print("%s 正在观看电影" % user)


user1 = User('张三', 17)
user2 = User('李四', 18)

watch_movie(user=user1)
watch_movie(user=user2)

"""
    过滤url
    计算时间
    过滤年龄
    
    过滤权限  权限系统
"""
