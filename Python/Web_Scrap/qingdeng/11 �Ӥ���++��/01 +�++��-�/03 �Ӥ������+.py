import time
import threading


def get(url, headers=None):
    print(url)
    time.sleep(5)
    print(headers)


# 模拟假如有很多地址
urls = ['https://www.baidu.com/', 'https://www.taobao.com/', 'https://www.4399.com/', 'https://www.dj.com/']


for url in urls:
    get_thread = threading.Thread(target=get,
                     args=(url,),  # 通过args指定位置参数, 一定要传一个元组, 只有一个元素的元组一定要加上逗号
                     kwargs={'headers': {'user-agent': 'python'}}  # 指定关键字参数
                     )
    get_thread.start()

"""
线程的参数传递
    target: 目标函数, 只传函数名字
    args: 通过args指定位置参数, 一定要传一个元组, 只有一个元素的元组一定要加上逗号
    kwargs: 指定关键字参数
"""
