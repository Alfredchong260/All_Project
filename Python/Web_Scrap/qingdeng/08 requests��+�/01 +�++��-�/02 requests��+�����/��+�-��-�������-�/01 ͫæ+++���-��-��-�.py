

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
result = re.findall('<dd><a href="(.*?)" title=".*?">.*?</a></dd>', html_data, re.S)

for res in result:
    all_url = 'https://www.biquwx.la/10_10582/' + res
    response_2 = requests.get(all_url)
    response_2.encoding = response_2.apparent_encoding
    html_data_2 = response_2.text
    # 提取每个章节的章节名
    title = re.findall('<h1>(.*?)</h1>', html_data_2, re.S)[0]
    print('正在下载:', title)
    result_2 = re.findall('<div id="content"><!--go-->.*?(.*?)<!--over-->.*?</div>', html_data_2, re.S)
    contend = result_2[0].replace('&nbsp;', '').replace('<br/>', '\n')

    with open('三寸人间\\' + title, mode='w', encoding='utf-8') as f:
        f.write(contend)


