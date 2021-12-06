import concurrent.futures
from tqdm import tqdm
import threading
import requests
import parsel

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}

lock = threading.Lock()

class biquge:
    def __init__(self, url) -> None:
        self.url = url

    def firstRequest(self):
        response = requests.get(self.url, headers=headers)
        selector = parsel.Selector(response.text)
        links = selector.css('#list dl dd a::attr(href)').getall()
        return links

    def secondRequests(self, url):
        response = requests.get(url, headers=headers)
        response.encoding = response.apparent_encoding
        selector = parsel.Selector(response.text)
        content = selector.css('#content::text').getall()
        return '\n'.join(content)

    def saveData(self, content):

        lock.acquire()

        with open('黑暗扎基奥特曼.txt', 'a', encoding='utf-8') as w:
            w.write(content)

        lock.release()

    def run(self):
        links = self.firstRequest()
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as exe:
            for link in tqdm(links):
                content = exe.submit(self.secondRequests, self.url + link).result()
                exe.submit(self.saveData(content))

if __name__ == '__main__':
    url = 'https://www.xbiquwx.la/35_35709/'
    test = biquge(url)
    test.run()
    
