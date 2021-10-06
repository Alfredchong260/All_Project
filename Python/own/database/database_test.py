import redis

db = redis.Redis(host='127.0.0.1',
    port=6379,
    db=0,
    decode_responses=True
    )

print(db)

redis_sets = [{'188.45.56.123:6523': 1}, {'16.36.56.369:6523':3}, {'69.45.56.123:6523':5},
            {'145.36.56.369:6523':2}, {'256.45.56.13:6523':4}, {'192.36.56.369:6523':6}]

'''zadd 是插入一个有序集合(set)'''
for sets in redis_sets:
    # proxies是有序集合的名字
    # sets 集合(redis数据库的集合概念，与python不同)
    db.zadd('proxies', sets)

'''zrangebyscore 获取指定评分的数据'''
result = db.zrangebyscore('proxies', 1, 3)
print(result)

'''zscore 查询数据在集合的评分'''
score = db.zscore('proxies', '145.36.56.369:6523')
print('评分', score)


'''zincrby 修改评分值'''
db.zincrby('proxies', 1, '145.36.56.369:6523')
score = db.zscore('proxies', '145.36.56.369:6523')
print('修改后的评分', score)

'''zrem 删除数据'''
db.zrem('proxies', '145.36.56.369:6523')


'''查询所有有序集合中的数据'''
count = db.zcard('proxies')
print(count)

# result = db.zrangebyscore('proxies', 1, 6)
# print(result)
