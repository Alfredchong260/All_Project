'''
    调度模块
'''
from configure import GETTER_PROXY, VERIFY_PROXY
from concurrent.futures import as_completed
from verify import verify_thread_pool
from database import RedisClient
from get import proxies_list
import concurrent.futures
import multiprocessing
from api import app
import time

Client = RedisClient()

class Schedule:

    # 调度获取代理的模块
    def getter(self):
        while True:
            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as exe:
                for func in proxies_list:
                    # 捕捉连接错误，当发生连接错误，等待两秒后重新尝试
                    try:
                        proxies = func(exe)
                        for proxy in as_completed(proxies):
                            for i in proxy.result():
                                print(i)
                                Client.add(proxy=i)
                                time.sleep(1)
                    except ConnectionError:
                        time.sleep(2)
                        proxies = func(exe)
                        for proxy in as_completed(proxies):
                            for i in proxy.result():
                                print(i)
                                Client.add(proxy=i)
                                time.sleep(1)
            time.sleep(GETTER_PROXY)

    # 调度验证代理模块
    def verify_proxy(self):
        while True:
            verify_thread_pool()
            time.sleep(VERIFY_PROXY)

    # 调用api服务模块
    def api_server(self):
        app.run()


    # 这三个方法需要一起去执行,进程
    def run(self):
        # 把所有的函数转换成进程对象
        print('代理池开始进行')
        multiprocessing.Process(target=self.getter).start()
        
        if Client.count() > 0:
            multiprocessing.Process(target=self.verify_proxy).start()
        multiprocessing.Process(target=self.api_server).start()

if __name__ == "__main__":
    Schedule().run()
