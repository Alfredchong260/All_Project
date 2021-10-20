"""
    使用 css 选择器将快代理中我需要的信息提取出来。
    目标网址：https://www.kuaidaili.com/free/
    
    需要解析以下数据:
        ip、
        port、
        类型
	
	提取出来print（）打印即可
	温馨提示: 爬取速度不要太快,加延迟,避免被封导致以后请求不到数据!
"""
from tqdm import tqdm
import requests
import parsel
import time

headers = {
    'Host': 'www.kuaidaili.com',
    'Referer': 'https://www.kuaidaili.com/',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

def formatter(ips, ports, types):
    for ip, port, type in zip(ips, ports, types):
        data = f'IP：{ip}\nPORT：{port}\n类型：{type}'
        yield data

def show(info):
    print(info)

def download(info):
    with open('./ip.txt', 'a') as w:
        w.write(info)

def main(selector, num):
    tbody = selector.css('.table.table-bordered.table-striped tbody')
    print('开始扫描数据')
    for body in tbody:
        ip = body.css('td:nth-child(1)::text').getall()
        port = body.css('td:nth-child(2)::text').getall()
        type = body.css('td:nth-child(4)::text').getall()
        data = formatter(ips=ip, ports=port, types=type)
        if num == 1:
            for info in tqdm(data):
                download(info)
        elif num == 2:
            for info in data:
                show(info)

def run():
    while True:
        num = input('请输入要爬取的页数：')
        choice = input('是否要保存数据 (Y/N)：')
        if num.upper() == 'Q':
            break
        if num and choice.upper() == 'Y':
            try:
                pages = int(num)
            except Exception:
                print('只能输入数字')
            for page in range(1, pages + 1):
                url = f'https://www.kuaidaili.com/free/inha/{page}/'
                response = requests.get(url, headers=headers)
                selector1 = parsel.Selector(response.text)
                main(selector=selector1, num=1)
                time.sleep(2)
        elif num and choice.upper() == 'N':
            try:
                pages = int(num)
            except Exception:
                print('只能输入数字')
            for page in range(1, pages + 1):
                url = f'https://www.kuaidaili.com/free/inha/{page}/'
                response = requests.get(url, headers=headers)
                selector1 = parsel.Selector(response.text)
                main(selector=selector1, num=2)
                time.sleep(2)

if __name__ == "__main__":
    run()
