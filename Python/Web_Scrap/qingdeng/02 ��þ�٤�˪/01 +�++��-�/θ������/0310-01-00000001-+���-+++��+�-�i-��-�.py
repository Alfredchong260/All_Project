"""
将上课的案例-爬取小说完善。爬取《剑来》前面十章的小说数据,分别保存在不同的txt文件下

	-- 网址： https://www.biquge7.com/book/1031/

请下下方开始编写代码
"""

"""
https://www.biquwx.la/10_10582/5103238.html
"""
import requests
import re


response = requests.get('https://www.biquwx.la/10_10582/')
response.encoding = response.apparent_encoding
html_data = response.text
# print(html_data)

# 解析前面十章小说数据对应的地址(url)
# <dd><a href="(.*?)" title=".*?">.*?</a></dd>
result = re.findall('<dd><a href="(.*?)" title=".*?">.*?</a></dd>', html_data, re.S)
print(result[1:11])

for res in result[1:11]:
    all_url = 'https://www.biquwx.la/10_10582/' + res
    # print(all_url)

    response_2 = requests.get(all_url)

    response_2.encoding = response_2.apparent_encoding

    html_data_2 = response_2.text

    # 提取每个章节的章节名
    title = re.findall('<h1>(.*?)</h1>', html_data_2, re.S)[0]
    print('正在下载:', title)
    result_2 = re.findall('<div id="content"><!--go-->.*?(.*?)<!--over-->.*?</div>', html_data_2, re.S)
    contend = result_2[0].replace('&nbsp;', '').replace('<br/>', '\n')

    # 数据保存
    with open(title, mode='w', encoding='utf-8') as f:
        f.write(contend)


