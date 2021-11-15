import concurrent.futures
from tqdm import tqdm
import requests
import os

url = 'https://tuchong.com/rest/tags/%E7%BE%8E%E5%A5%B3/posts'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

params = {
    'page': 0,
    'count': 0,
    'order': 'weekly'
}

class TuChong:

    def sendRequests(self, param):
        response = requests.get(url, headers=headers, params=param)

        return response

    def parseData(self, response):
        for data in response.json()['postList']:
            author_id = data['author_id']
            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as exe:
                for ids in tqdm(data['images']):
                    img_id = ids['img_id']
                    img_url = f'https://photo.tuchong.com/{author_id}/f/{img_id}.jpg'
                    exe.submit(self.downloadImg, img_url)

    def downloadImg(self, url):
        response = requests.get(url)
        name = url.split('/')[-1]
        with open(f"{filename}/{name}", 'wb') as f:
            f.write(response.content)

    def run(self):
        param = params.copy()
        with concurrent.futures.ProcessPoolExecutor(max_workers=2) as exe:
            for i in range(5):
                param['page'] += 1
                param['count'] += 20
                response = self.sendRequests(param)
                exe.submit(self.parseData, response)

if __name__ == '__main__':
    filename = './imgs'
    if not os.path.exists(filename):
        os.mkdir(filename)

    test = TuChong()
    test.run()
