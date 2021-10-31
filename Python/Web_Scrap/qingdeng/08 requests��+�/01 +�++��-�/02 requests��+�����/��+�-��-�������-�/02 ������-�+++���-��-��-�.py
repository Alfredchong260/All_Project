"""
https://www.biquwx.la/10_10582/5103238.html
"""

import requests
import re
import os

if not os.path.exists('三寸人间'):
    os.mkdir('三寸人间')

response = requests.get('https://www.biquwx.la/10_10582/')
response.encoding = response.apparent_encoding
html_data = response.text

# 部分章节的地址,
result = re.findall('<dd><a href="(.*?)" title=".*?">.*?</a></dd>', html_data, re.S)


def download(url, times=5):  # 参数名字可以自己定义  默认有一次正常请求 + 5次异常重试 = 6次
    all_url = 'https://www.biquwx.la/10_10582/' + url

    try:
        response_2 = requests.get(all_url)
        response_2.encoding = response_2.apparent_encoding
        html_data_2 = response_2.text
        # 提取每个章节的章节名
        title = re.findall('<h1>(.*?)</h1>', html_data_2, re.S)[0]
        print('正在下载:', title)
        result_2 = re.findall('<div id="content"><!--go-->.*?(.*?)<!--over-->.*?</div>', html_data_2, re.S)
        contend = result_2[0].replace('&nbsp;', '').replace('<br/>', '\n')

        with open('三寸人间\\' + title + '.txt', mode='w', encoding='utf-8') as f:
            f.write(contend)
    except Exception as e:
        print(e)
        if times >= 1:
            download(url, times=times - 1)  # 函数内部调用函数本身<函数的递归>  # 利用了函数的特性


for res in result:
    download(res)
