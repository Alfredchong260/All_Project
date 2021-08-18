# 知足的喷瓜

import requests
from lxml import etree

headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

# url = 'https://bilibili.com/'

# response = requests.get(url, headers=headers).text
# html = etree.HTML(response)
# a = html.xpath('//*[@id="internationalHeader"]/div[1]/div/div[1]/ul/li[1]/a/text()')
# print(a)

# url = 'https://i0.hdslb.com/bfs/feed-admin/dfc2c69fb68c3977599b717874bb209f1a9625f8.jpg@880w_388h_1c_95q'

# r = requests.get(url, headers=headers).content
# with open('bilibili.jpg', 'wb') as f:
#     f.write(r)

choice = 'Y'
maybe = ['Y', 'N']

def main():
    url = input('请输入您要爬取照片的网址：')
    name = input('请输入照片名称：')
    response = requests.get(url, headers=headers)

    with open(name + '.jpg', 'wb') as f:
        f.write(response.content)
    ask()

def ask():
    ask = input('是否继续，Y 是 N 否：')
    if ask.upper() not in maybe:
        ask()
    elif ask.upper() == 'Y':
        main()

if __name__ == '__main__':
    main()
