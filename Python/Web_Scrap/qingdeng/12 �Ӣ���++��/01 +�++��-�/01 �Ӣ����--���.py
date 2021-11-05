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


# download()
# upload()


"""
多任务<多线程和多进程>, 对于多进程来说, 任务执行必须写在  "if __name__ == '__main__':"  下面
因为计算机在执行py代码的时候找不到主进程
"""
if __name__ == '__main__':
    # 1. 把函数对象转换成一个进程对象
    download_process = multiprocessing.Process(target=download)
    print(download_process)
    # 2. 执行进程对象的任务
    download_process.start()

    upload_process = multiprocessing.Process(target=upload).start()

"""
可以查看线程任务数据量
但是对于多进程, 不借助一些终端命令是看不到进程数量的, 可以理解为多线程的任务数量
"""
