from tqdm import tqdm
import requests
import concurrent.futures
import time
import re
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}

start = time.time()
class sticker:
    def getResponse(self, url):
        global filename
        filename = './sticker/'
        if not os.path.exists(filename):
            os.mkdir(filename)

        response = requests.get(url, headers=headers)

        return response

    def getInfo(self, response):
        titles = re.findall('<a href=".*?" title="(.*?)">', response.text)
        images = re.findall('<img class="ui image lazy" data-original="(.*?)"', response.text)

        return zip(titles, images)

    def format(self, title):
        mode = re.compile(r'[\/\|\:\*\?\"<>]')
        new = re.sub(mode, '_', title)

        return new

                
    def saveInfo(self, img_url, title):
        img_content = requests.get(url=img_url, headers=headers)
        print(f'正在下载{title}')
        if img_url.endswith('jpg'):
            with open(f"{filename}{title}.jpg", 'wb') as w:
                w.write(img_content.content)

        elif img_url.endswith('gif'):
            with open(f"{filename}{title}.gif", 'wb') as w:
                w.write(img_content.content)

    def main(self, url):
        response = self.getResponse(url)
        infos = self.getInfo(response)
        for index in infos:
            title = index[0]
            img_url = index[1]
            title = self.format(title)
            if len(title) > 50:
                title = title[:10]
            self.saveInfo(img_url, title)


if __name__ == '__main__':
    test = sticker()
    exe = concurrent.futures.ThreadPoolExecutor(max_workers=8)
    for page in range(1, 11):
        url = f'https://www.fabiaoqing.com/biaoqing/lists/page/{page}.html'
        exe.submit(test.main, url)
    exe.shutdown()
    end = time.time()
    print(f'总用时：{end-start}')
