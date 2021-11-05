import csv
import multiprocessing
import requests
import parsel
import concurrent.futures
import time   # 时间模块, 内置模块

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

def send_requests(url):
    response = requests.get(url=url, headers=headers)
    return response.text

def parse_data(data):
    selector = parsel.Selector(data)
    lis = selector.css('.grid_view li')
    data_list = []  # 收集解析的数据
    for li in lis:
        name = li.css('.info .hd a span:nth-child(1)::text').get()
        info = li.css('.bd p:nth-child(1)::text').get().strip()
        score = li.css('.rating_num::text').get().strip()
        follow = li.css('.star span:nth-child(4)::text').get()
        print(name, info, score, follow)
        data_list.append([name, info, score, follow])
    return data_list

def save_data(data_list):
    for data in data_list:
        with open('豆瓣250.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_write = csv.writer(f)
            csv_write.writerow(data)

def run(url):
    html_data = send_requests(url)
    data = parse_data(html_data)
    save_data(data)

# 测试主函数是否能运行
# run('https://movie.douban.com/top250?start=0&filter=')

if __name__ == '__main__':

    # for page in range(0, 226, 25):
    #     url = f'https://movie.douban.com/top250?start={page}&filter='
    #     multiprocessing.Process(target=run, args=(url,)).start()

    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        for page in range(0, 226, 25):  # 一共有多少个进程  主进程 + 子进程 = 11个进程
            url = f'https://movie.douban.com/top250?start={page}&filter='
            executor.submit(run, url)

"""
对于多进程, 如果资源竞争引发了数据的缺失, 加锁也没用
    可以引入队列 queue
    
    可以通过控制进程数量, 随缘
"""


