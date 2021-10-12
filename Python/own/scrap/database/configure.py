'''
项目配置
'''

'''数据库配置'''
REDIS_HOST = '127.0.0.1'            # 数据库所在地址
REDIS_PORT = 6379                   # 数据库所在端口
REDIS_DATABASE = 0                  # 操作哪一个数据库
REDIS_OBJECT = 'PROXIES'            # 数据库操作对象

'''时间间隔配置'''
GETTER_PROXY = 60 * 5               # 获取代理的时间间隔
VERIFY_PROXY = 60 * 6               # 验证代理的时间间隔

'''服务器配置'''
SERVER_HOST = '127.0.0.1'           # api服务器地址
SERVER_PORT = 5000                  # api接口

SERVER_DEBUG = True                 # 是否开启debug模式

'''测试地址'''
TEST_URL = 'https://github.com/'    # 测试代理的网址
TIMEOUT = 10                        # 设置超时时间
WORKERS_NUM = 10                    # 最大线程量

'''数据库分数设置'''
INIT_SCORE = 60                     # 初始分数
HIGH_SCORE = 100                    # 最高分数
MINIMUM_SCORE = 1                   # 最低分数
HIGHEST_SCORE = 99                  # 范围指定

CHANGE_SCORE = -20                  # 减分的操作
