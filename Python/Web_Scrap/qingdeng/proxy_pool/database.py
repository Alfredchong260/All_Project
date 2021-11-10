from configure import REDIS_HOST, REDIS_PORT, REDIS_OBJECT, REDIS_DATABASE
from configure import HIGH_SCORE, MINIMUM_SCORE, HIGHEST_SCORE, CHANGE_SCORE, INIT_SCORE
import random
import redis

class RedisClient:
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DATABASE):
        '''初始化数据库'''
        self.db = redis.Redis(
            host=host,
            port=port,
            db=db,
            decode_responses=True
            )

    def exists(self, proxy):
        '''判断这里是否存在于数据库'''
        #如果有序集合中有当前传进来的代理，返回False
        #如果有有序集合没有当前传进来的代理，返回True
        return self.db.zscore(REDIS_OBJECT, proxy) is None

    def add(self, proxy, score=INIT_SCORE):
        '''
        添加代理到数据库，并将代理设置为初始分数
        :param proxy:传进来的代理
        :param score:设置的初始分数
        '''
        if self.exists(proxy):
            print('代理写入中')
            return self.db.zadd(REDIS_OBJECT, {proxy: score})

    def random_proxy(self):
        '''随机在数据库选择一个代理'''
        # 1. 尝试获取评分最高的代理，暂时设置为100
        proxies = self.db.zrangebyscore(REDIS_OBJECT, HIGH_SCORE, HIGH_SCORE)
        if proxies:
            return random.choice(proxies)
        # 2. 尝试获取最低分数到最高分数中间的代理
        proxies = self.db.zrangebyscore(REDIS_OBJECT, MINIMUM_SCORE, HIGHEST_SCORE)
        if proxies:
            return random.choice(proxies)
        # 3. 如果查询不到代理，就提示没有代理
        else:
            print('#####数据库为空#####')

    def  decrease(self, proxy):
        '''把传入的代理进行降分的操作'''
        self.db.zincrby(REDIS_OBJECT, CHANGE_SCORE, proxy)
        score = self.db.zscore(REDIS_OBJECT, proxy)
        if score <= 0:
            self.db.zrem(REDIS_OBJECT, proxy)

    def max(self, proxy):
        '''把传进来的代理设置为最大分数'''
        return self.db.zadd(REDIS_OBJECT, {proxy: HIGH_SCORE})

    def count(self):
        '''获取数据库中代理的总数'''
        return self.db.zcard(REDIS_OBJECT)

    def all(self):
        '''获取所有代理，返回值为列表'''
        proxies = self.db.zrangebyscore(REDIS_OBJECT, MINIMUM_SCORE, HIGH_SCORE)
        if proxies:
            return proxies
        print('#####----数据库为空----#####')

    def count_for_num(self, num):
        '''指定数量获取代理，返回值为列表'''
        all_proxies = self.all()
        return random.sample(all_proxies, k=num)

    def getfullmark(self):
        '''随机在数据库选择一个代理'''
        # 1. 尝试获取评分最高的代理，暂时设置为100
        proxies = self.db.zrangebyscore(REDIS_OBJECT, HIGH_SCORE, HIGH_SCORE)

        return proxies

if __name__ == '__main__':
    proxies = ['927.72.91.211:9999', '927.12.91.211:8888', '927.792.91.219:7777', '927.732.91.211:6666']
    redis_client = RedisClient()
    # result = redis_client.count_for_num(2)
    # print(result)
    for proxy in proxies:
        redis_client.add(proxy)
