from tqdm import tqdm
import requests
import re
import os

filename = './leshe/'
if not os.path.exists(filename):
    os.mkdir(filename)

# main = 'https://www.leshe.us/xz/mtyh/15269.html'
url = input('请输入url：')

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
}
response = requests.get(url, headers=headers)
page_num = re.findall('<a class="page-numbers" href=".*?">(.*?)</a>', response.text)[-1]

for i in range(1, int(page_num) + 1):
    new = f"{url}/page/{i}"
    response = requests.get(new, headers=headers)
    links = re.findall('<a target="_blank" href="(.*?)" title=".*?" rel="bookmark">.*?</a>', response.text)
    for link in tqdm(links):
        response = requests.get(link, headers=headers)
        imgs = re.findall('<img src="(.*?)" title=".*?" alt=".*?" />', response.text)
        for img in imgs:
            name = img.split('/')[-1]
            response = requests.get(img, headers=headers)
            with open(f"{filename}{name}", 'wb') as w:
                w.write(response.content)
