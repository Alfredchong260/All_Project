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


# def wrapper_get_html(target_func, args):
#     start_time = time.time()
#     html = target_func(args)
#     print('请求网页运行的时间:\t', time.time() - start_time)
#     return html
#
#
# def wrapper_save_html(target_func, html, name):
#     start_time = time.time()
#     target_func(html, name)
#     print('保存网页运行的时间:\t', time.time() - start_time)


def wrapper_func(target_func, *args, **kwargs):
    # *args, **kwargs 函数的关键字参数与位置参数全部接受
    start_time = time.time()
    print('target_func', target_func, '\nargs:\t', args)
    result = target_func(*args, **kwargs)  # 然后再将参数传递给真正执行的函数
    print('运行的时间:\t', time.time() - start_time)
    return result


baidu_html = wrapper_func(get_html, 'http://www.baidu.com')
wrapper_func(save_html, baidu_html, 'baidu.html')
