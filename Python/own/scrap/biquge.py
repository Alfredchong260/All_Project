import requests
import parsel

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}

class biquge:
    def __init__(self, url) -> None:
        self.url = url

    def firstRequest(self):
        response = requests.get(self.url, headers=headers)
        selector = parsel.Selector(response.text)
        links = selector.css('#list dl dd a::attr(href)').getall()
        print(links)


if __name__ == '__main__':
    # keyword = input('请输入你要查找的小说关键字：')
    url = 'https://www.xbiquge.so/book/53043/'
    # url = f'https://www.xbiquge.so/modules/article/search.php?searchkey={keyword}'
    test = biquge(url)
    test.firstRequest()
    
