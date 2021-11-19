'''
    项目配置文档
'''

"""数据路配置"""
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DATABASE = 0

REDIS_OBJECT = 'PROXIES'


"""时间间隔配置"""
GETTER_PROXY = 60 * 5
VERIFY_PROXY = 60 * 8
TIMEOUT = 10


"""服务器配置"""
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000

"""测试地址"""
URL = 'https://www.baidu.com'


"""数据库分数设置"""
INIT_SCORE = 50
HIGH_SCORE = 100
MINIMUM_SCORE = 1
HIGHEST_SCORE = 99


"""分数操作"""
CHANGE_SCORE = -10
