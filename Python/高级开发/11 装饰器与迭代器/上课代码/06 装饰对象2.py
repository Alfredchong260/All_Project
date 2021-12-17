import requests
import time
import threading


def wrapper_func(target_func):
    def wrapper(*args, **kwargs):
        """之前的装饰函数"""
        # *args, **kwargs 函数的位置参数全部接受与关键字参数
        start_time = time.time()
        print('target_func', target_func, '\nargs:\t', args)
        result = target_func(*args, **kwargs)  # 然后再将参数传递给真正执行的函数
        print('运行的时间:\t', time.time() - start_time)
        return result

    return wrapper  # 把装饰函数返回出去


# 请求网页,请求图片,请求视频
@wrapper_func  # @ 装饰器语法糖
def get_html(url):
    response = requests.get(url)
    return response.text


def save_html(html, name):
    with open(name, mode='w', encoding='utf-8') as f:
        f.write(html)


# # get_html = wrapper_func(get_html)  之间的关系
# get_html = wrapper_func(get_html)
baidu_html = get_html('http://www.baidu.com')
