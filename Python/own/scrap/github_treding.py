import concurrent.futures
from tqdm import tqdm
import threading
import requests
import random
import parsel
import time
import csv

lock = threading.Lock()

url = "https://github.com/topics"

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
}

proxies = [
    "HTTP://110.243.30.23:9999",
    "HTTP://222.189.191.206:9999",
    "HTTP://106.42.163.100:9999",
    "HTTP://120.83.107.69:9999",
    "HTTP://60.13.42.135:9999",
    "HTTP://113.195.232.23:9999",
    "HTTP://59.62.36.74:9000",
    "HTTP://218.2.226.42:80",
]
proxy = {"HTTP": random.choice(proxies)}


def firstRequests():
    response = requests.get(url, headers=header, proxies=proxy)
    selector = parsel.Selector(response.text)

    topics = [
        i.strip()
        for i in selector.css(".f3.lh-condensed.mb-0.mt-1.Link--primary::text").getall()
    ]
    desc = [
        i.strip() for i in selector.css(".f5.color-fg-muted.mb-0.mt-1::text").getall()
    ]
    links = [
        url + "/" + i.split("/")[-1]
        for i in selector.css(
            ".no-underline.flex-1.d-flex.flex-column::attr(href)"
        ).getall()
    ]

    return zip(topics, desc, links)


def writer():
    with open(
        "/home/cms/.Project/Python/own/scrap/github_info.csv",
        mode="w+",
        encoding="utf-8",
        newline="",
    ) as fs:
        csv_writer = csv.writer(fs)
        for i in firstRequests():
            csv_writer.writerow(i)


def secondRequests(new_url):
    response = requests.get(new_url, headers=header, proxies=proxy)
    selector = parsel.Selector(response.text)
    links = selector.css(".text-bold.wb-break-word::attr(href)").getall()
    print(links)


def main():
    new_url = firstRequests()
    for i in new_url:
        print(i[-1])
        secondRequests(new_url=i[-1])
        break

main()
