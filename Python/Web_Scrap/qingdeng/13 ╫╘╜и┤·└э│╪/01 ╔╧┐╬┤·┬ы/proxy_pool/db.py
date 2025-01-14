"""
数据库模块
"""
import random

import redis


class RedisClient:
    """数据库类"""
    def __init__(self, host='127.0.0.1', port=6379, db=0):
        """初始化数据库"""
        self.db = redis.Redis(host=host,  port=port, db=db, decode_responses=True)

    def exists(self, proxy):
        """判断代理有没有存在数据库"""
        # is 身份运算符
        # 如果有序集合中有当前传进来的代理, 返回 False
        # 如果没有序集合中有当前传进来的代理, 返回 True
        return self.db.zscore('PROXIES', proxy) is None

    def add(self, proxy, score=10):
        """
        添加代理到数据库, 并将代理设置为初始分数
        :param proxy: 传进来的代理
        :param score: 设置的初始分数
        """
        if self.exists(proxy):  # 如果这个代理没有存储在数据库中
            print('代理写入:', proxy)
            return self.db.zadd('PROXIES', {proxy: score})  # 插入代理代理数据

    def random(self):
        """随机在数据库中选择一个代理"""
        # 1. 尝试获取评分最高的代理, 暂时设置为100
        proxies = self.db.zrangebyscore('PROXIES', 100, 100)  # 列表
        if proxies:
            return random.choice(proxies)
        # 2. 尝试获取最低分数到最高分数中间的代理
        proxies = self.db.zrangebyscore('PROXIES', 10, 99)  # 列表
        if proxies:
            return random.choice(proxies)
        # 3. 如果查询不到代理, 就提示没有数据
        print('########---数据库为空---########')

    def decrease(self, proxy):
        """把传入的代理执行降分的操作"""
        self.db.zincrby('PROXIES', -1, proxy)  # 把传入的代理减分
        score = self.db.zscore('PROXIES', proxy)  # 查询传入代理的分数
        if score <= 0:
            self.db.zrem('PROXIES', proxy)  # zrem 删除代理

    def max(self, proxy):
        """把传入的代理设置为最大分数"""
        return self.db.zadd('PROXIES', {proxy: 100})

    def count(self):
        """获取数据库中代理的数量"""
        return self.db.zcard('PROXIES')  # zcard  查询有序集合中数据数量

    def all(self):
        """获取所有代理"""
        proxies = self.db.zrangebyscore('PROXIES', 1, 100)  # 指定分数在集合中中查询  ---返回列表
        if proxies:
            return proxies
        else:
            print('########---数据库无代理---########')

    def count_for_num(self, number):
        """指定数量获取代理, 返回一个列表"""
        all_proxies = self.all()
        proxies = random.sample(all_proxies, k=number)
        return proxies



if __name__ == '__main__':
    proxies = ['927.72.91.211:9999', '927.12.91.211:8888', '927.792.91.219:7777', '927.732.91.211:6666' ]


    redis_client = RedisClient()
    # for proxy in proxies:
    #     redis_client.add(proxy)

    # print(redis_client.random())
    # redis_client.decrease('927.72.91.211:9999')

    print(redis_client.count_for_num(4))

