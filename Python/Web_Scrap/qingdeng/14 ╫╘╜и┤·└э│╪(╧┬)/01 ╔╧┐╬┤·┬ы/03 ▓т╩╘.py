import requests
import threading


def geter():


    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    requests.get(url='https://movie.douban.com/top250', headers=headers)
    print('正在请求...')
    return None



if __name__ == '__main__':
    while True:
        threading.Thread(target=geter).start()