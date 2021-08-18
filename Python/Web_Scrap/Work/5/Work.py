# 知足的喷瓜

import requests
from lxml import etree

# url = 'https://github.com'
# headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

# response = requests.get(url, headers=headers)
# html = etree.HTML(response.text)
# results = html.xpath('//div[@class="d-flex flex-wrap py-5 mb-5"]/div[2]/ul/li')
# # results = html.xpath('//ul[@class="qm-rank clearfix js-rank"]/text()')
# # print(results)

# for result in results:
#     text = result.xpath('./a/text()')
#     print(text)
input = input("URL:")
response = requests.get("https://youtube.com/results?search_query=" + input)

html = etree.HTML(response.text)
result = html.xpath('//a/text()')
print(result)
