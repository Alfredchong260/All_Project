"""
	- 课上的360案例，先自己实现一遍, 构建查询参数请求数据
	- 将前三页的图片数据保存下来
		
请在下方编写代码
"""

'''
程序功能：
    如果两个输入都为空，默认下载目标金智秀3页图片
    任意一个输入含有q，将判断为退出程序
    任意一个输入为空。都将执行默认下载目标金智秀及3页图片
    否则，将根据输入的页数以及关键字在指定文件夹下载图片
'''

import concurrent.futures
import requests
import random
import time
import os

requests.packages.urllib3.disable_warnings()

filename = './picture'
if not os.path.exists(filename):
    os.mkdir(filename)

url = 'https://image.so.com/j'

headers = {
    'Host': 'image.so.com',
    'Referer': 'https://image.so.com/i?q=%E9%A3%8E%E6%99%AF&src=srp',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15"
    ]

headers['User-Agent'] = random.choice(user_agent_list)

params = {
    'q': '金智秀',
    'pd': 1,
    'pn': 60,
    'correct': '金智秀',
    'adstar': 0,
    'tab': 'all',
    'sid': 'f731333001bd5a00c3db8abdc0d8a410',
    'ras': 6,
    'cn': 0,
    'gn': 0,
    'kn': 49,
    'crn': 0,
    'bxn': 20,
    'cuben': 0,
    'pornn': 0,
    'manun': 0,
    'src': 'srp',
    'sn': 60,
    'ps': 60,
    'pc': 60
}

def downloadImage(url, count):
    symbol = [1,2,3,4,5,6,7,8,9,'!','@','#','$','%','^','&','*','(',')']
    if not url.endswith('jpg'):
        first = random.choice(symbol)
        second = random.choice(symbol)
        name = str(first) + str(second) + '.jpg'
    else:
        name = url.split('.jpg')[0] + '.jpg'
    time.sleep(0.5)
    response1 = requests.get(url)
    print(f'正在下载第{count}张图')
    name = url.split('/')[-1]
    with open(f"{filename}/{name}", 'wb') as w:
        w.write(response1.content)

def visit(num, param):
    try:
        number = int(num) * 60 + 1
    except Exception:
        number = num * 60 + 1
    for page in range(60, number, 60):
        print('正在验证图片数量')
        param['sn'] = page
        param['ps'] = page
        response = requests.get(url, headers=headers, params=param, verify=False)
        time.sleep(0.5)
        data = response.json()['list']
        print('开始下载图片')
        count = 1
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as exe:
            for info in data:
                img_url = info['img']
                exe.submit(downloadImage, img_url, count)
                count += 1


def run():
    while True:
        param = params
        num = input('请输入要爬取的页数：')
        target = input('请输入需要的壁纸关键字：')
        if num.upper() == 'Q' or target.upper() == 'Q':
            break
        if num and target:
            param['q'] = target
            param['correct'] = target
            visit(num=num, param=param)
        else:
            visit(num=3, param=param)

if __name__ == "__main__":
    run()
