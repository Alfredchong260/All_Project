from tqdm import tqdm
import requests
import re
import os

filename = './三寸人间'
if not os.path.exists(filename):
    os.mkdir(filename)

url = 'https://www.biquwx.la/10_10582/'

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0'
}

response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding

links = re.findall('<dd><a href="(.*?)" title=".*?">.*?</a></dd>', response.text, re.S)
links = links[1:11]

for link in tqdm(links):
    request_url = url + link
    response2 = requests.get(request_url, headers=headers)
    response2.encoding = response2.apparent_encoding
    title = re.findall('<h1>(.*?)</h1>', response2.text, re.S)
    fiction = re.findall('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br/><br/>', response2.text, re.S)
    info = '\n'.join(fiction)
    with open(f"{filename}/{title[0]}.txt", 'w') as w:
        w.write(info)
