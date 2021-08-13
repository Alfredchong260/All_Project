import requests
from lxml import etree

url = "https://www.17k.com/top/refactor/top100/10_bookshelf/10_bookshelf_top_100_pc.html"

headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}

response = requests.get(url, headers=headers)
print(response)
# html = etree.HTML(response.content.decode('utf-8'))

# results = html.xpath('//div[@class="content TABBOX"]/div[2]/div/table/tr')

# for result in results:
#     title = result.xpath('./td[3]/a/text()')
#     hrefs = result.xpath('./td[3]/a/@href')
#     for href in hrefs:
#         hr = 'https://www' + href.split('www')[1]
#         print(hr)
#         r = requests.get(url=hr, headers=headers)
#         htm = etree.HTML(r.content.decode('utf-8'))
#         intro = htm.xpath('//p[@class="intro"]/a/text()')
