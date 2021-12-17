import requests
import time
import threading


# 请求网页,请求图片,请求视频
def get_html(url):
    response = requests.get(url)
    return response.text


def get_photo(url):
    response = requests.get(url)
    return response.text


#
#
# def get_video(url):
#     response = requests.get(url)
#     return response.text


def save_html(html, name):
    with open(name, mode='w', encoding='utf-8') as f:
        f.write(html)


# 需求,计算两个函数的运行时间
"""可以在外部添加代码实现"""
# start_time = time.time()
# baidu_html = get_html('http://www.baidu.com')
# print('请求网页运行的时间:\t', time.time() - start_time)
#
# start_time = time.time()
# save_html(baidu_html, 'baidu.html')
# print('保存网页运行的时间:\t', time.time() - start_time)

"""可以直接加在函数里面"""


def wrapper_get_html(target_func, args):
    start_time = time.time()
    html = target_func(args)
    print('请求网页运行的时间:\t', time.time() - start_time)
    return html


def wrapper_save_html(target_func, html, name):
    start_time = time.time()
    target_func(html, name)
    print('保存网页运行的时间:\t', time.time() - start_time)


baidu_html = wrapper_get_html(get_html, 'http://www.baidu.com')
wrapper_save_html(save_html, baidu_html, 'baidu.html')
