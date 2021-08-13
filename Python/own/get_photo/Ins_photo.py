'''
全局思路：
    得到链接以便能进行接下来的数据爬取
    将得到的链接二次处理得到内层数据
    将内层数据下载成jpg
'''

import requests
from lxml import etree

url = 'https://www.instagram.com/_soyaaaa.____/'
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}

response = requests.get(url ,headers=headers)
html = etree.HTML(response.text)
results = html.xpath()
print(results)
    
# results = html.xpath('//article[@class="ySN3v"]/div/div/div[1]/div[1]/a/div[1]/div/img')
# print(results)

# with open('jisoo_' + '.jpg', 'wb') as f:
#     f.write(response.content)

