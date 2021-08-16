'''
全局思路：
    得到链接以便能进行接下来的数据爬取
    将得到的链接二次处理得到内层数据
    将内层数据下载成jpg
'''

import requests
import re
from lxml import etree

url = 'https://www.instagram.com/_soyaaaa.____/'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'
}

response = requests.get(url ,headers=headers)
html = etree.HTML(response.text)

print(response.text)
# print(href)

# results = html.xpath('//div[@class=" _2z6nI"]/article/div[1]/div/div[1]/div[1]/a/@href')[0]
# results = html.xpath('/html/body/div[1]/section/main/div/div[4]/article/div[1]/div/div[1]/div[1]/a/@href')
# print(results)
    

# with open('jisoo_' + '.jpg', 'wb') as f:
#     f.write(response.content)

