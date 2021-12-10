import time
import threading


def download():
    print("开始下载文件...")
    time.sleep(1)
    print("完成下载文件...")


def upload():
    print("开始上传文件...")
    time.sleep(1)
    print("完成上传文件...")


start_time = time.time()

# 默认是顺序进行上传下载
# download()
# upload()
t1 = threading.Thread(target=download)
t1.start()
t2 = threading.Thread(target=upload)
t2.start()

# 默认情况下,主线程的代码执行完毕之后会等待子线程代码结束,才会结束掉程序
while len(threading.enumerate()) > 1:
    print('当前程序拥有的线程:', threading.enumerate())
    time.sleep(0.1)

print('当前程序拥有的线程:', threading.enumerate())  # enumerate 枚举 将当前程序里面的线程全部一一列出来
# 程序还没运行完毕就打印了时间 ?
print('花费的时间:\t', time.time() - start_time)  # time.time() 获取当前的时间(秒)
