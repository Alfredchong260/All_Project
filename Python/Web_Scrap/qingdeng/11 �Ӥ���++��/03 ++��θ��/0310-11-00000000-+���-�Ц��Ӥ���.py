"""
	目标网址：https://www.duitang.com/
	
	作业描述：请在网页最上面搜索框输入关键字 “蜡笔小新” 进行搜索图片，根据搜索到的结果采集前十页图片
	
	作业要求：用多线程的方式实现
"""

import concurrent.futures
from tqdm import tqdm
import requests
import time
import re
import os

url = 'https://www.duitang.com/napi/blogv2/list/by_search/'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

params = {
    'kw': '蜡笔小新',
    'after_id': '24',
    'type': 'feed',
    'include_fields': 'top_comments,is_root,source_link,item,buyable,root_id,status,like_count,like_id,sender,album,reply_count,favorite_blog_id',
    '_type': '',
    '_': str(int(time.time() * 1000))
}

filename = './img'

if not os.path.exists(filename):
    os.mkdir(filename)

def sendRequests(url, param):
    '''此函数为请求目标网址，返回对象'''
    response = requests.get(url, headers=headers, params=param)

    return response

def parseLink(res):
    '''此函数为解析图片网址，返回的是列表'''
    img_url = re.findall('"path":"(.*?)"', res.text, re.S)

    return img_url


def secondRequests(img_url):
    '''此函数用于二次访问数据'''
    response = requests.get(img_url, headers=headers)

    return response

def downloadImg(res, name):
    '''此函数用于下载图片'''
    with open(f'{filename}/{name}', 'wb') as w:
        w.write(res.content)


def main(param, count):
    '''此函数为主函数，调动各个函数，形成串联'''
    res = sendRequests(url, param=param)
    links = parseLink(res)
    for link in tqdm(links, desc=f'正在下载第{count}页数据'):
        name = link.split('/')[-1]
        response = secondRequests(link)
        downloadImg(response, name)

count = 0

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as exe:
    for page in range(0, 97, 24):
        count += 1
        param = params.copy()
        param['after_id'] = str(page)
        exe.submit(main, param, count)

