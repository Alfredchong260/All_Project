import requests
from lxml import etree

url = 'https://www.bilibili.com/video/BV1h7411374f'
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

response = requests.get(url, headers=headers)
html = etree.HTML(response.text)

results = html.xpath('//ul[@class="list-box"]/li')

for result in results:
    path = result.xpath('./a/@href')
    print(path)
