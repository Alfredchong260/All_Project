"""
	目标网址: https://maoyan.com/board/4?offset=0
	
    猫眼100网页, 请用多进程嵌套多线程池方式实现

温馨提示: 猫眼封ip严重, 在确保代码无误的情况下尽量少运行。考验代码能力的时候来了。。。
请在下方编写代码
"""
import concurrent.futures
import requests
import csv
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

def sendRequests(url):
    '''此函数为请求指定网址'''
    response = requests.get(url, headers=headers)

    return response

def parseData(response):
    '''此函数为解析数据，返回值为元祖'''
    title = re.findall('<a href=".*?" title="(\w+)" class="image-link" data-act="boarditem-click" data-val="{movieId:\d+}">', response.text, re.S)

    actors = re.findall('<p class="star">(.*?)</p>', response.text, re.S)
    actor_list = []
    for actor in actors:
        actor_list.append(actor.strip().split('：')[1])

    releaseTime = []
    releases = re.findall('<p class="releasetime">(.*?)</p>    </div>', response.text, re.S)
    for release in releases:
        releaseTime.append(release.split('：')[1])

    rating = re.findall('<p class="score"><i class="integer">(\d.)</i><i class="fraction">(\d)</i></p>', response.text, re.S)
    rate = []
    for rates in rating:
        rate.append(rates[0] + rates[1])

    return zip(title, actor_list, releaseTime, rate)

def writeData(dataList):
    with open('猫眼.csv', 'a', encoding='utf-8') as w:
        csv_writer = csv.writer(w)
        csv_writer.writerow(dataList)

def main(url):
    '''此函数为主函数'''
    response = sendRequests(url)
    data = parseData(response)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as exe:
        for i in data:
            print(i)
            exe.submit(writeData, i)

'''此为初始化猫眼csv文件'''
with open('猫眼.csv', 'w', encoding='utf-8') as w:
    csv_writer = csv.writer(w)
    csv_writer.writerow(['戏名', '主演', '上映时间', '评分'])

with concurrent.futures.ProcessPoolExecutor(max_workers=2) as exe:
    for page in range(0, 100, 10):
        url = f'https://www.maoyan.com/board/4?offset={page}'
        exe.submit(main, url)
