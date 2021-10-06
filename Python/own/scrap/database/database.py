from configure import INIT_SCORE, HIGH_SCORE, MINIMUM_SCORE, HIGHEST_SCORE, CHANGE_SCORE
from configure import REDIS_HOST, REDIS_PORT, REDIS_DATABASE, REDIS_OBJECT
import redis
import random

class RedisClient:

    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DATABASE):
        self.db = redis.Redis(host=host, port=port, db=db, decode_responses=True)

    def exists(self, proxy):
        """判断传入的代理，是否已经在数据库中"""

        return not self.db.zscore(REDIS_OBJECT, proxy) is None

    def add(self, proxy, score=INIT_SCORE):
        """
        添加代理到数据库
        :param proxy: 传入的代理
        :param score: 设置初始分数
        """
        if not self.exists(proxy): # 如果数据库中没有当前代理
            # 进行数据的插入
            return self.db.zadd(REDIS_OBJECT, {proxy:score})
            
    def random(self):
        """随机选择一个代理"""
        # 尝试获取满分的代理
        # 尝试去最低分到最高分中同范围代理的数据
        # 如果查不到数据，就提示没有数据
        proxies = self.db.zrangebyscore(REDIS_OBJECT, HIGH_SCORE, HIGH_SCORE)
        if len(proxies):
            return random.choice(proxies)

        proxies = self.db.zrangebyscore(REDIS_OBJECT, MINIMUM_SCORE, HIGHEST_SCORE)
        if len(proxies):
            return random.choice(proxies)

        print('#####数据为空#####')

    def decrease(self, proxy):
        '''传入一个代理，如果检测不过关，那么评分执行见分的操作'''
        self.db.zincrby(REDIS_OBJECT, CHANGE_SCORE, proxy) # 把传入的代理减分
        score = self.db.zscore(REDIS_OBJECT, proxy)

        if score <= 0:
            self.db.zrem(REDIS_OBJECT, proxy)

    def max(self, proxy):
        '''传入一个代理，如果检测过关，就将代理设置为100分'''
        return self.db.zadd(REDIS_OBJECT, {proxy:HIGH_SCORE})

    def count(self):
        '''获取数据库中所有代理的数量'''
        return self.db.zcard(REDIS_OBJECT)

    def all(self):
        """获取所有代理"""
        proxies = self.db.zrangebyscore(REDIS_OBJECT, MINIMUM_SCORE, HIGH_SCORE)
        if proxies:
            return proxies
        else:
            print('#####---数据库为空---#####')

    def count_for_num(self, num):
        """指定数量获取代理，返回一个列表"""
        all_proxy = self.all()
        proxies = random.sample(all_proxy, k=num)
        return proxies

    def get100Proxy(self):
        '''选取一个100分的代理，如果没有则返回None'''
        try:
            proxies = self.db.zrangebyscore(REDIS_OBJECT, HIGH_SCORE, HIGH_SCORE)
            return proxies
        except Exception:
            return None


if __name__ == '__main__':
    redis_client = RedisClient()
    proxies = ['927.72.91.211:9999', '927.12.81.211:8888', '927.792.91.219:7777', '927.732.91.211:6666']

    a = redis_client.count_for_num(2)
    print(a)
