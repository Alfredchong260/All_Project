import requests
from lxml import etree

url = 'https://www.17k.com/'
header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

response = requests.get(url, headers=header)
# print(response.content.decode('utf-8'))
html = etree.HTML(response.content.decode('utf-8'))

ul_list = html.xpath('//ul[@class="Top1"]')
# print(ul_list)

for ul in ul_list:
    title = ul.xpath('./li/a/text()')
    print(title)
