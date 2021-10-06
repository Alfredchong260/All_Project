import redis

db = redis.Redis(host='127.0.0.1', port=6379, db=0,decode_responses=True)

print(db)

redis_sets = [{'188.45.56.123:6523':1}, {'16.36.56.369:6523':3}, {'69.45.56.123:6523':5},
    {'145.36.56.369:6523':2}, {'256.45.56.123:6523':4}, {'192.36.56.369:6523':6}]

for sets in redis_sets:
    # zadd 是用于插入有序集合的名字
    # proxies 是用于插入有序集合的名字
    # 集合是redis内部的集合，与python的集合类似，但不尽相同
    db.zadd('proxies', sets)

'''zrangebyscore 获得指定评分的数据'''
result = db.zrangebyscore('proxies', 1, 6)
print(result)

'''zscore 查询数据在集合中的评分'''
score = db.zscore('proxies', '145.36.56.369:6523')
print('评分',score)

'''zincrby 修改评分值'''
new = db.zincrby('proxies', 2, '145.36.56.369:6523')
print('修改后的评分',new)

'''zrem 删除指定数据'''
db.zrem('proxies', '145.36.56.369:6523')

'''zcard 查询所有有序集合中的数据'''
count = db.zcard('proxies')
print(count)

# result = db.zrangebyscore('proxies', 1, 6)
# print(result)
