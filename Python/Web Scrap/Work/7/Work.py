# 知足的喷瓜
import requests
from lxml import etree

url = "https://www.17k.com/top/refactor/top100/10_bookshelf/10_bookshelf_top_100_pc.html"

headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}

response = requests.get(url, headers=headers)
html = etree.HTML(response.content.decode('utf-8'))

results = html.xpath('//div[@class="content TABBOX"]/div[2]/div/table/tr')

def scarp(url):
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.content.decode('utf-8'))
    intro = html.xpath('//p[@class="intro"]/a/text()')[0]
    print(intro)
    print('')

def writeInTXTfile():
    pass

for result in results:
    title = result.xpath('./td[3]/a/text()')
    hrefs = result.xpath('./td[3]/a/@href')
    for href in hrefs:
        hr = 'https://www' + href.split('www')[1]
        scarp(url=hr)
