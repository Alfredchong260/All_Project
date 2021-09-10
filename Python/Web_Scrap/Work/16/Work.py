'''
全局思路：
    访问页面
    得到m3u8的链接
    访问并将其返回内容记录
    根据记录的链接逐个访问并下载
    将所有ts文件进行合并

问题：
    1. 访问速度很慢
    2. 偶尔会因访问过多的报错

解决方法：
    1. 使用多线程
    2. 使用try方法，当报错时换个代理再访问
'''
import re, requests, os, random, threading, time, zipfile
from tqdm import tqdm
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

thread_lock = threading.BoundedSemaphore(value=10)
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}

proxies = ['HTTP://110.243.30.23:9999', 'HTTP://222.189.191.206:9999',
            'HTTP://106.42.163.100:9999', 'HTTP://120.83.107.69:9999',
           'HTTP://60.13.42.135:9999',  'HTTP://113.195.232.23:9999',
           'HTTP://59.62.36.74:9000', 'HTTP://218.2.226.42:80']
proxy = {'HTTP': random.choice(proxies)}
# HTTP://106.42.163.100:9999

class AZhan:
    # 初始化数据，先得到需要的网址
    def __init__(self, url):
        self.url = url

    # 主函数
    def main(self):
        try:
            response = requests.get(self.url, headers=headers, proxies=proxy, timeout=20)
            title = re.findall('<title >(.*?) - AcFun弹幕视频网 - 认真你就输啦 \(\?ω\?\)ノ- \( ゜- ゜\)つロ</title>', response.text)[0]
            m3u8_url = re.findall('"backupUrl(.*?)\"]', response.text)[0].split('\"')[2]

            if not os.path.exists('./video'):
                os.mkdir('./video')
            if not os.path.exists('./video/' + title):
                os.mkdir('./video/' + title)

            self.second_visit(m3u8_url)
            links = self.readM3u8()

            # 多线程访问页面
            print('开始下载切片视频')

            for link in tqdm(links):
                name = link.split('.ts')[0].split('.0')[1:5]
                thread_lock.acquire()
                t = threading.Thread(target=self.downloadTs, args=(link, name, title))
                t.start()

            print('切片视频下载完成')

            self.hebing(title)

        except Exception as e:
            print('Error:',e)

    # 二次访问得到m3u8的数据并写入文档
    def second_visit(self, url):
        response = requests.get(url, headers=headers, proxies=proxy, timeout=20)
        with open('acfun.m3u8', 'wb') as w:
            w.write(response.content)

    # 读取文档的网址
    def readM3u8(self):
        link_list = []
        with open('acfun.m3u8', 'r', encoding='utf-8') as r:
            for lines in r:
                line = lines.strip()
                if line.endswith('.ts'):
                    link = 'https://tx-safety-video.acfun.cn/mediacloud/acfun/acfun_video/hls/' + line
                    link_list.append(link)

        return link_list

    # 下载每个网址的内容
    def downloadTs(self, link, name, title):
        s = requests.Session()
        s.keep_alive = False
        try:
            proxy = {'HTTP': random.choice(proxies)}
            print(proxy)
            response = requests.get(link, headers=headers, proxies=proxy, verify=False)
            with open(f'./video/{title}/{name}' + '.ts', 'wb') as w:
                w.write(response.content)
                thread_lock.release()
        except Exception as e:
            print('Error:', e)
            time.sleep(1)
            print('Retrying')
            proxy = {'HTTP': random.choice(proxies)}
            response = requests.get(link, headers=headers, proxies=proxy, verify=False)
            with open(f'./video/{title}/{name}' + '.ts', 'wb') as w:
                w.write(response.content)
                thread_lock.release()


    # 读取所有ts文件的数据并二次写入mp4格式的文档
    def hebing(self, title):
        path = './video/' + title + '/'
        files = os.listdir(path)
        files.sort()
        with zipfile.ZipFile(path + 'final.mp4', mode='w') as z:
            for file in tqdm(files):
                file_path = path + file
                z.write(file_path)

if __name__ == '__main__':
    ac_num = input('请输入A站ac号：')
    url = f'https://www.acfun.cn/v/{ac_num}'
    start = time.time()
    test = AZhan(url)
    test.main()
    end = time.time()
    print('爬虫用时一共：', end-start)
