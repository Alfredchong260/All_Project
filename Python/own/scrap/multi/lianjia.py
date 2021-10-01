import concurrent.futures
import requests
import parsel
import time
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}

def firstRequest(url):
    response = requests.get(url, headers=headers)
    return response

def parseData(response):
    datalist = []
    selector = parsel.Selector(response)
    ls = selector.css('.clear.LOGCLICKDATA')
    for l in ls:
        title = l.css('.title a::text').get()
        address = l.css('.positionInfo a::text').getall()
        intro = l.css('.houseInfo span::text').get()
        follow = l.css('.followInfo span::text').get()
        unitPrice = l.css('.unitPrice span::text').get()
        totalPrice = l.css('.totalPrice span::text').get()

        print([title, address, intro, follow, unitPrice, totalPrice])
        datalist.append([title, address, intro, follow, unitPrice, totalPrice])

    return datalist

def saveData(datas):
    for data in datas:
        with open('链家.csv', 'a', encoding='utf-8', newline='') as w:
            writer = csv.writer(w)
            writer.writerow(data)

def run(url):
    a = firstRequest(url)
    datalist = parseData(a)
    saveData(datalist)

if __name__ == '__main__':
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as exe:
        for page in range(1, 101):
            url = f'https://cs.lianjia.com/ershoufang/pg{page}/'
            exe.submit(run, url)
    print(f'花费时间：{time.time() - start}')
