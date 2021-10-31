"""
    目标网址: http://www.win4000.com/zt/dongman.html
    
    需求:
        "动漫桌面壁纸" 文字下面有很多动漫图集
        1、用xpath采集数据
        2、采集以下信息
            采集动漫图集的标题
            采集动漫图集中图片对应的url地址
            
        解析到数据用print()函数打印即可
请在下方编写代码：
"""
import concurrent.futures
from tqdm import tqdm
import requests
import parsel
import os

filename = './pictures'

if not os.path.exists(filename):
    os.mkdir(filename)

url = 'http://www.win4000.com/zt/dongman.html'

headers = {
    'Cookie': 't=5bac2bc83ead5171e899d7f511d0a1a8; r=3937; UM_distinctid=17ca0b119bc7f9-09803cd5b1dc5c-17291209-2f7600-17ca0b119bd94c; t=2732f9b42335df3e96fc3e3d23a6b58b; r=6060; XSRF-TOKEN=eyJpdiI6IlREWnl5XC9FTjdcL2E5Sko4aHp6QkRGQT09IiwidmFsdWUiOiJwQXY3UmRsTFdzd0lkbzh2cFwvbkpXUG04TGUzU1NFZlVOdDhGcmRRT2dzZ3F5ek5CdmU1bHZBU01HcDJPRWxJZjNzWFwvXC8xRjZ4NERmTVVkY1ZreXZcL2RvcU5oZk43QmV3WUlrdVRcL1JcL2tiR3c4UUFTdVFmR1JYQ2YxWnRPK2FzcSIsIm1hYyI6IjBkNmZjYWMzZTFlYjA3MDIyNzIzN2FiNjYyZDEyMzBkNWJkZWM3OGE2MzU3ZWU2MDFiOTkzY2M3MTRiMTQwMWEifQ%3D%3D; win4000_session=eyJpdiI6InpHZ041XC9rQlwvYXkzRnlcL01DZnYwblE9PSIsInZhbHVlIjoiaTFjcXpXT0M0Y3d0K2xpUDNaTEpxYzFVckJUK3hYVkVRSEk2VVJyNHVqcWRNTjZVVXhiZFpqR3o2MitUYW56YTBXenVmTWNoRTl4N1l4MmZZWDVcL0FMRmdyc0dVbVl4dEpjZWl4blBhSWRlckhydlhRRjh1S0I0a1wvTFA3bzlWYSIsIm1hYyI6IjAzNzUwZWFkMTJkNTA3ZjAzNDIzZTJlZjc3MTU5ZWQ0ZGRmMDFlZjIyYjQ1YzMyMjdhZWZhOWI2YjUxZDIzYzQifQ%3D%3D; CNZZDATA1279885023=652441478-1634782554-null%7C1634798779',
    'Host': 'www.win4000.com',
    'Referer': 'http://www.win4000.com/zt/dongman.html',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

'''
首次访问
目标为得到所有li标签里的网址，用于二次访问
'''
response = requests.get(url, headers=headers)
selector = parsel.Selector(response.text)
infos = selector.xpath("//div[@class='Left_bar']//ul[@class='clearfix']/li")

print(response.text)

def second_visit(pages, num):
    for page in tqdm(range(1, int(pages) + 1)):
        second = f'http://www.win4000.com/wallpaper_detail_{num}_{page}.html'
        response_2 = requests.get(second, headers=headers)
        selector_2 = parsel.Selector(response_2.text)

        # 此为查找出照片的网址
        img_url = selector_2.xpath('//img[@class="pic-large"]/@src').get()

        # 此变量用于命名图片
        name = img_url.split('/')[-1]
        response_3 = requests.get(img_url)
        with open(f"{filename}/{name}", 'wb') as w:
            w.write(response_3.content)


with concurrent.futures.ThreadPoolExecutor(max_workers=3) as exe:
    for link in infos:
        '''
        二次访问
        目标为得到照片的数量以及照片的网址，用于下载图片使用
        '''
        # 此为li标签的网址
        new_url = link.xpath('./a/@href').get()     

        # 二次访问
        response_1 = requests.get(new_url, headers=headers)       
        selector_1 = parsel.Selector(response_1.text)

        # 此为所有照片的总数
        pages = selector_1.xpath('//div[@class="ptitle"]//em/text()').get()     # 

        # 此操作用于找出网址中变化的参数，后面用于访问同一系列的其它照片
        num = new_url.split('.html')[0].split('_')[-1]
        exe.submit(second_visit, pages, num)
