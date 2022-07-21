import concurrent.futures
from tqdm import tqdm
import threading
import requests
import parsel
import time
import re
import os

lock = threading.Lock()

filename = "./kanxiaojiejie/"
if not os.path.exists(filename):
    os.mkdir(filename)


class Kanxiaojiejie:
    def __init__(self, url) -> None:
        self.url = url

    def get_page(self):
        response = requests.get(self.url)
        selector = parsel.Selector(response.text)
        total_page_url = selector.css(".pages::text").get()

        total_pages = re.findall("\d+", total_page_url)[-1]

        return total_pages

    def first_request(self):
        response = requests.get(self.url)
        selector = parsel.Selector(response.text)

        url_list = selector.css(
            ".content article a.entry-thumbnail::attr(href)"
        ).getall()

        return url_list

    def second_request(self, url):
        response = requests.get(url)
        selector = parsel.Selector(response.text)
        img_url = selector.css("#wrapper div.entry-content img::attr(src)").getall()

        for img in tqdm(img_url):
            self.download_image(img_url=img)

    def download_image(self, img_url):
        name = img_url.split(".")[-2].split('/')[-1]
        response = requests.get(img_url)

        lock.acquire()
        with open(filename + name + ".jpg", mode="wb") as fs:
            fs.write(response.content)
        lock.release()

        time.sleep(2)

    def run(self):
        url_list = self.first_request()
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as exe:
            for url in url_list:
                exe.submit(self.second_request, url)


if __name__ == "__main__":
    url = "https://www.kanxiaojiejie.com/"
    kan = Kanxiaojiejie(url)
    pages = kan.get_page()

    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as exe:
        for page in range(1, int(pages) + 1):
            new_url = f"https://www.kanxiaojiejie.com/page/{page}"
            main = Kanxiaojiejie(new_url)
            exe.submit(main.run)
