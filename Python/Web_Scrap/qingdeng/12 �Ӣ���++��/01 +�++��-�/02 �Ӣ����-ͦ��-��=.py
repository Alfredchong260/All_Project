import time
import multiprocessing  # 进程模块  内置


def download():
    print('开始-下载文件')
    time.sleep(1)  # 阻塞, 任务挂起
    print('完成-下载文件')


def upload():
    print('开始-上传文件')
    time.sleep(1)
    print('完成-上传文件')


if __name__ == '__main__':
    download_process = multiprocessing.Process(target=download)
    print(download_process)
    download_process.start()
    upload_process = multiprocessing.Process(target=upload).start()

    print('--主进程执行到这里了--')   # 主进程会等待子进程执行完任务以后才会退出
    # time.sleep(0.5)
"""
主进程会优先执行完毕, 会等待子进程执行完任务以后才会退出
"""
