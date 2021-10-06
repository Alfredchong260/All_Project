'''
调度模块
'''
from configure import SERVER_HOST, SERVER_PORT, SERVER_DEBUG
from configure import GETTER_PROXY, VERIFY_PROXY
from database import RedisClient
from verify import thread_pool
from get import proxy_list
import multiprocessing
from api import app
import time

REDIS = RedisClient()

class Schedule:
    # 1. 调度获取代理模块，免费代理会不定时更新,所以每隔一段时间就要捉取一次代理数据
    def getProxy(self):
        while True:
            for func in proxy_list:
                proxies = func()
                for proxy in proxies:
                    print(f'--代理写入数据库--\n{proxy}')
                    REDIS.add(proxy)

            time.sleep(GETTER_PROXY)

    # 2. 调度检测代理模块
    def verifyPro(self):
        while True:
            thread_pool()
            time.sleep(VERIFY_PROXY)

    # 3. 调度api服务模块
    def proxyApi(self):
        while True:
            app.run(host=SERVER_HOST, port=SERVER_PORT, debug=SERVER_DEBUG)

    # 调用这三个函数一起运行
    def run(self):
        print('########--代理池开始运行--########')
        getProxyProcess = multiprocessing.Process(target=self.getProxy)
        getProxyProcess.start()

        if REDIS.count() > 0: # 数据库有代理，才检测代理
            verifyProProcess = multiprocessing.Process(target=self.verifyPro)
            verifyProProcess.start()

        self.proxyApi()
        # proxyApiProcess = multiprocessing.Process(target=self.proxyApi)
        # proxyApiProcess.start()

if __name__ == '__main__':
    work = Schedule()
    work.run()
