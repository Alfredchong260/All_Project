import multiprocessing
import time

def download():
    print('开始下载')
    time.sleep(1)
    print('下载完成')

def upload():
    print('开始上传')
    time.sleep(1)
    print('上传完成')

multi1 = multiprocessing.Process(target=download)
multi2 = multiprocessing.Process(target=upload)

multi1.start()
multi2.start()

def get(url, headers=None):
    print(url)
    time.sleep(3)
    print(headers)

start = time.time()

urls = ['https://www.baidu.com', 'https://bilibili.com', 'https://github.com', 'https://www.jd.com']

for url in urls:
    gets = multiprocessing.Process(target=get, args=(url,) , kwargs={'headers':'python'})
    gets.start()


