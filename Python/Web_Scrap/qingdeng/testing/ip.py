import redis

db = redis.Redis(
    host='127.0.0.1',     #指定数据库所在的域名地址
    port=6379,            #指定redis数据库运行端口 
    db=0,                 #指定操作的数据库
    decode_responses=True #解码存储
)

print(db)

'''数据库有序集合操作'''
redis_sets = [{'188.45.56.123:6523':1},{'16.36.53.369:6523':2},{'69.45.56.123:6523':3},
            {'145.36.56.369:6523':4},{'256.45.56.123:6523':5},{'192.36.56.369:6523':6}]

for data in redis_sets:
    #zadd 插入一个有序集合方法
    #proxies 有序集合的名字
    #data 有序集合
    db.zadd('proxies',data)

'''根据指定的有序集合的序列，获取到有序集合<代理ip>的内容'''
result = db.zrangebyscore('proxies',1, 5)
print(result)

'''zscore 扎寻代理在集合中的评分'''
#如果擦回到就返回评分
#没有查询到就返回None
print(db.zscore('proxies', '188.45.56.123:6523'))

#集合的分数的加减操作
result = db.zincrby('proxies', -1, '192.36.56.369:6523')
print(db.zscore('proxies', '192.36.56.369:6523'))

#获取有序集合的数据数量
print(db.zcard('proxies'))
