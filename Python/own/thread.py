#from multiprocessing import Process
#import os, time

##计算密集型任务
#def work():
#    res = 0
#    for i in range(100000000):
#        res *= i 

#if __name__ == "__main__":
#    l = []
#    print("本机为",os.cpu_count(),"核 CPU")  # 本机为4核
#    start = time.time()
#    for i in range(4):
#        p = Process(target=work)  # 多进程
#        l.append(p)
#        p.start()
#    for p in l:
#        p.join()
#    stop = time.time()
#    print("计算密集型任务，多线程耗时 %s" % (stop - start))

#from multiprocessing import Process
#import os, time

##计算密集型任务
#def work():
#    res = 0
#    for i in range(100000000):
#        res *= i 

#if __name__ == "__main__":
#    l = []
#    print("本机为",os.cpu_count(),"核 CPU")  # 本机为4核
#    start = time.time()
#    for i in range(4):
#        p = Process(target=work)  # 多进程
#        l.append(p)
#        p.start()
#    for p in l:
#        p.join()
#    stop = time.time()
#    print("计算密集型任务，多进程耗时 %s" % (stop - start))
import time
import threading

def task_thread(counter):
    print(f'线程名称：{threading.current_thread().name} 参数：{counter} 开始时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')
    num = counter
    while num:
        time.sleep(3)
        num -= 1
    print(f'线程名称：{threading.current_thread().name} 参数：{counter} 结束时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')


if __name__ == '__main__':
    print(f'主线程开始时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')

    #初始化3个线程，传递不同的参数
    t1 = threading.Thread(target=task_thread, args=(3,))
    t2 = threading.Thread(target=task_thread, args=(2,))
    t3 = threading.Thread(target=task_thread, args=(1,))
    #开启三个线程
    t1.start()
    t2.start()
    t3.start()
    #等待运行结束
    t1.join()
    t2.join()
    t3.join()

    print(f'主线程结束时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')
