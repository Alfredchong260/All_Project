import time
import threading

def sing():
    for i in range(10):
        print(f'唱歌{i}')
        time.sleep(1)
    print('执行任务花费时间：', time.time() - start)

def dance():
    for i in range(10):
        print(f"跳舞{i}")
        time.sleep(1)
    print('执行任务花费时间：', time.time() - start)

start = time.time()
# sing()
# dance()

print('当前多进程数量：', threading.enumerate())

sing_thread = threading.Thread(target=sing)
sing_thread.start()

print('当前多进程数量：', threading.enumerate())

dance_thread = threading.Thread(target=dance)
dance_thread.start()

print('当前多进程数量：', threading.enumerate())

# def get(url, headers=None):
#     print(url)
#     time.sleep(3)
#     print(headers)

# start = time.time()

# urls = ['https://www.baidu.com', 'https://bilibili.com', 'https://github.com', 'https://www.jd.com']

# for url in urls:
#     print(threading.enumerate())
#     gets = threading.Thread(target=get, args=(url,), kwargs={'headers': {'user-agent': 'python'}})
#     gets.start()

