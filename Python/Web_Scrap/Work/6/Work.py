import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}

for i in range(0, 91, 10):
    url = f'https://maoyan.com/board/4?offset={i}'
    response = requests.get(url, headers=headers, proxies={'http': '119.81.189.194'}, timeout=10)
    html = etree.HTML(response.text)
    results = html.xpath('//div[@class="movie-item-info"]')

    for result in results:
        text = result.xpath('./p[1]/a/text()')[0]
        star = result.xpath('./p[2]/text()')[0].replace('主演：','').split()
        releasetime = result.xpath('./p[3]/text()')[0].replace('上映时间：','').split()
        print(text)
