"""
写出一个用户名敏感词过滤装饰器，需要过滤敏感词

要求使用函数装饰器实现，在实例化对象时，一旦名字中出现在敏感词表中的内容，提示不能创建对象（或抛出异常）。
"""
mgc = """
到货
本店
代购
扣扣
客服
微店
兼职
兼值
淘宝
小姐
包夜
"""


class User:
    """用户模型"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name


def decorator_filter_name(func):
    def wrapper(*args, **kwargs):
        # print(args)
        if args[0] in mgc.split():
            raise Exception('名字中有敏感词,不能创建')
        
        # 执行函数之前装饰
        result = func(*args, **kwargs)  # 执行创建的函数
        # 执行函数之后进行装饰

        return result

    return wrapper


@decorator_filter_name
def create(name, age):
    return User(name, age)


user1 = create('张三', 17)
user2 = create('李四', 18)
user3 = create('兼职', 18)
