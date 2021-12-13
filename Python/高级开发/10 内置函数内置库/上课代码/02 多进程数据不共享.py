import time
import multiprocessing
import threading


def list_append(arr):
    arr.put(1)
    arr.put(2)
    arr.put(3)
    print('len(arr):', arr.qsize())


if __name__ == '__main__':
    # arr = []
    # threading.Thread(target=list_append, args=(arr,)).start()
    # threading.Thread(target=list_append, args=(arr,)).start()
    # # 多线程数据共享,操作的是同一个列表
    # time.sleep(0.1)
    # print('thread:\t', len(arr))
    print('-------------')
    arr = multiprocessing.Queue(10)  # 将普通列表改查进程的队列,实现数据共享
    p1 = multiprocessing.Process(target=list_append, args=(arr,))
    p2 = multiprocessing.Process(target=list_append, args=(arr,))
    # 多进程数据不共享,操作的不是同一个变量
    p1.start()
    p2.start()
    time.sleep(1)
    print('process:\t', arr.qsize())
