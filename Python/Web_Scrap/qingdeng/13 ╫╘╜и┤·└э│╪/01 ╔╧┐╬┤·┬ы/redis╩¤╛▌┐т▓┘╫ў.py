import redis


# 创建一个redis数据库对象
db = redis.Redis(
        host='127.0.0.1',  # 指定数据库所在的域名地址  127.0.0.1 表示计算机的本地地址
        port=6379, # 指定redis数据库运行的端口
        db=0, # 指定操作的数据库,
        decode_responses=True  # 解码存储
    )

print(db)

"""数据库有序集合操作"""  # 是redis数据库的一个概念
redis_sets = [{'188.45.56.123:6523': 1}, {'16.36.56.369:6523': 2}, {'69.45.56.123:6523': 3},
              {'145.36.56.369:6523': 4}, {'256.45.56.123:6523': 5}, {'192.36.56.369:6523': 6}]

for data in redis_sets:
    # zadd  插入一个有序集合方法
    # proxies  有序集合的名字
    # data  有序集合
    db.zadd('proxies', data)


"""根据指定的有序集合的序列, 获取到有序集合<代理ip>结合的内容"""
result = db.zrangebyscore('proxies', 1, 3)
print(result)

"""zscore  查询代理在集合中的评分"""
# 如果查询到了就返回评分
# 没有查询到就返回 None
score = db.zscore('proxies', '188.45.56.123:6523')
print('代理评分:', score)

"""zincrby 修改集合的分数"""
# -1  操作序列的分数(可正可负)
db.zincrby('proxies', -1, '256.45.56.123:6523')
score = db.zscore('proxies', '256.45.56.123:6523')
print('修改后的分数: ', score)


"""zcard 获取有序集合的数据数量"""
count = db.zcard('proxies')
print('当前集合内的数据数据量为:', count)



