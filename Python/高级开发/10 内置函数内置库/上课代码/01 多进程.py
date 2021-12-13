"""
    一个工厂(多进程)  --> 默认一个一条自动化流水线(线程) --> 只有一个工人
                        如果想提示产量,可以购买更多的自动化流水线

    如果多线程性能达到了瓶颈,就行可以开设新的工厂

    会偷懒的任务: 多线程 (爬虫请求/数据库查询/打开文件)  io 密集型的任务
    不会偷懒的任务: 多进程 (人工智能训练模型/递归求解/大文件的读取)  cpu 密集型的任务
"""
import time
import multiprocessing


def upload():
    print("开始上传文件...")
    time.sleep(1)
    print("完成上传文件...")


def download():
    print("开始下载文件...")
    time.sleep(1)
    print("完成下载文件...")


# 一整个文件的代码都属于同一个进程
# 新的进程会把就的进程的变量,环境全部复制一遍
if __name__ == '__main__':
    # 多进程的用法与多线程保持一致
    p1 = multiprocessing.Process(target=upload)  # 新进程会把旧进程的环境变量全部复制一遍
    p2 = multiprocessing.Process(target=download)
    p1.start()
    p2.start()
