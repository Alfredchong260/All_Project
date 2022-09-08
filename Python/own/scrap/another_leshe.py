from tqdm import tqdm
import requests
import aiohttp
import asyncio
import parsel
import time
import os

filename = "/home/cms/.Project/Python/own/scrap/lenglui/"



header = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36"
}


def get_page(url):
    response = requests.get(url, headers=header)
    selector = parsel.Selector(response.text)
    pages = selector.css("ul.page-numbers li:nth-child(6) a::text").get()

    return pages


async def downloadImg(url, session):
    title = url.split("/")[-1]
    response = await session.get(url, ssl=False)
    content = await response.read()
    with open(f"{filename}{title}", "wb") as fs:
        fs.write(content)


async def firstRequests(url, session):
    response = await session.get(url, headers=header, ssl=False)
    html = await response.text()
    selector = parsel.Selector(html)
    links = selector.css("div.placeholder a::attr(href)").getall()

    return links


async def secondRequests(url, session):
    response = await session.get(url, headers=header, ssl=False)
    html = await response.text()
    selector = parsel.Selector(html)
    img_url = selector.css(
        ".entry-content.u-text-format.u-clearfix img::attr(data-srcset)"
    ).getall()

    return img_url


async def main():
    pages = get_page(url)
    print(pages)
    links = []
    async with aiohttp.ClientSession() as session:
        for i in range(1, int(pages) + 1):
            links = await firstRequests(f"{url}/page/{i}", session)
            for link in links:
                img_url = await secondRequests(url=link, session=session)
                for img in tqdm(img_url):
                    await downloadImg(img, session)


url = input("请输入网页地址：")
start = time.time()

if not os.path.exists(filename):
    os.mkdir(filename)
asyncio.run(main())

print("time taken :", time.time() - start)
