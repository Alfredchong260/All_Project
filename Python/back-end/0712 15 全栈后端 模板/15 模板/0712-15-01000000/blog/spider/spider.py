import requests
import parsel

response = requests.get('http://www.tkv5.cn/sitemap.xml')
sel = parsel.Selector(response.text)
urls = sel.xpath('//url')
for url in urls:
    link = url.xpath('./loc/text()').get()
    print(link)
