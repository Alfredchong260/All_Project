import concurrent.futures
from tqdm import tqdm
import requests
import parsel
import os
import re

url = 'https://www.520mmtv.com/tag/ke.html'

filename = './video/'
if not os.path.exists(filename):
    os.mkdir(filename)

def sendRequest():
    '''
    首次访问主页面
    :return: 响应体对象
    '''
    response = requests.get(url)
    
    return response

def parseData(response):
    '''
    解析出所有二级链接
    :param response: 响应体对象
    :return: 二级链接
    '''
    selector = parsel.Selector(response.text)
    li_lst = selector.css('.update_area_lists.cl li')
    for li in li_lst:
        link = li.css('a::attr(href)').get()
        yield link

def secondRequest(url):
    '''
    访问二级链接
    :param url: 二级链接
    '''
    response = requests.get(url)
    video_url = re.findall('url: "(.*?)",', response.text, re.S)[0]
    name = video_url.split('/')[-1]
    requestVideo(name, video_url)

def requestVideo(name, url):
    '''
    访问.mp4网址以及下载影片
    :param name: .mp4的前缀名
    :param url: .mp4的链接
    '''
    response = requests.get(url)
    file_size = int(response.headers.get('Content-Length'))
    pbar = tqdm(total=file_size)  # 设置进度条的长度
    with open(filename + name, 'wb') as f:
        for chunk in response.iter_content(1024*1024*2):
            f.write(chunk)
            pbar.set_description('正在下载中......')
            pbar.update(1024*1024*2)  # 更新进度条长度
        pbar.close()

def run():
    '''
    主函数
    作为所有函数的核心，调度各个函数
    '''
    response = sendRequest()
    links = parseData(response)
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as exe:
        for link in links:
            exe.submit(secondRequest, link)

run()
