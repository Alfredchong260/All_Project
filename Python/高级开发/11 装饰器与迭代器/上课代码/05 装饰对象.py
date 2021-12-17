import requests
import time
import threading


# 请求网页,请求图片,请求视频
def get_html(url):
    response = requests.get(url)
    return response.text


def save_html(html, name):
    with open(name, mode='w', encoding='utf-8') as f:
        f.write(html)


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


# 1. 对函数进行装饰,可以得到装饰之后的函数
wrapper_func_get_html = wrapper_func(get_html)
baidu_html = wrapper_func_get_html('http://www.baidu.com')


wrapper_func_save_html = wrapper_func(save_html)
print(wrapper_func_get_html)  # wrapper_func_get_html
print(wrapper_func_save_html)  # wrapper_func_save_html

# 2. 调用装饰之后的函数,得到结果
baidu_html = wrapper_func_get_html('http://www.baidu.com')
wrapper_func_save_html(baidu_html, 'baidu.html')

soso_html = wrapper_func_get_html('http://www.soso.com')
wrapper_func_save_html(soso_html, 'soso.html')

html_360 = wrapper_func_get_html('https://hao.360.com/')
wrapper_func_save_html(html_360, '360.html')

"""
    一个函数实现了逻辑 + 计时
    一个函数实现逻辑 一个函数实现计时
"""
