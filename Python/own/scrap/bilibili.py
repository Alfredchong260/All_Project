from multiprocessing import Process
import concurrent.futures
from tqdm import tqdm
import requests
import json
import os
import re

headers = {
    'referer': 'https://www.bilibili.com/video/',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

filename = '/home/cms/.Project/Python/own/scrap/video'

if not os.path.exists(filename):
    os.mkdir(filename)


def sendRequests(url):
    response = requests.get(url)

    return response


def getVideoInfo(bv_id):
    '''首次请求指定网站'''
    url = f'https://www.bilibili.com/video/{bv_id}'
    response = requests.get(url, headers=headers)

    return response


def parseData(response):
    title = re.findall(
        '<title data-vue-meta="true">(.*?)_哔哩哔哩_bilibili</title>', response)[0]
    data = re.findall(
        '<script>window.__playinfo__=(.*?)</script>', response)[0]
    json_data = json.loads(data)

    return [title, json_data]


def parseAudio(json_data, title):
    audio_url = json_data['data']['dash']['audio']

    for url in tqdm(audio_url, desc=f'正在下载{title}音频数据'):
        download(url=url['baseUrl'], title=title, type='mp3')


def parseVideo(json_data, title):
    video_url = json_data['data']['dash']['video']

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as exe:
        for url in tqdm(video_url, desc=f'正在下载{title}视频数据'):
            exe.submit(download, url['baseUrl'], title, 'mp4')

    combine()


def download(url, title, type=None):
    response = requests.get(url, headers=headers)

    dir_name = f"{filename}/{title}"

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    with open(f"{dir_name}/video.{type}", 'wb') as w:
        w.write(response.content)


def combine():
    print('开始合并视频与音频')
    command = f"ffmpeg -i {filename}/{title}/video.mp3 -i {filename}/{title}/video.mp4 -acodec copy -vcodec copy {filename}/{title.split()[0]}.mp4"
    os.system(command)

    # os.remove(f"{filename}{title}/{title}")


if __name__ == '__main__':
    bv_id = input('请输入BV号：')
    response = getVideoInfo(bv_id)
    title, json_data = parseData(response.text)
    t1 = Process(target=parseAudio, args=(json_data, title)).start()
    t2 = Process(target=parseVideo, args=(json_data, title)).start()
