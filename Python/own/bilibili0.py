import os
import sys
from you_get import common as you_get
import queue
import threading
import time
 
exitFlag = 0
 
class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print("开始线程："+self.name)
        downloading_video(self.name, self.q)
        print("退出线程：" + self.name)
 
def downloading_video(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            videoUrl = q.get()
            queueLock.release()
            # print("%s downloading %s" % (threadName, videoUrl))
            #第一种方法用os调用you-get
            cmd = "you-get -o E://video/ " + videoUrl
            os.system(cmd)
            #第二种方法用sys调用you-get ...我觉得没上面的方便
            # path = 'E:\\video\'   #设置下载目录
            # sys.argv = ['you-get','-o',path,videoUrl]   #sys传递参数执行下载
            # you_get.main()
        else:
            queueLock.release()
        time.sleep(2)
 
threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4", "Thread-5", "Thread-6"]    #线程个数
videoList = [
    'https://www.bilibili.com/video/av97994896',
    'https://www.bilibili.com/video/av98149221',
    'https://www.bilibili.com/video/av啥啥啥',
    'https://www.bilibili.com/video/av啥啥啥',
    'https://www.bilibili.com/video/av啥啥啥',
    'https://www.bilibili.com/video/av啥啥啥',
    'https://www.bilibili.com/video/av啥啥啥',
    'https://www.bilibili.com/video/av啥啥啥',
    'https://www.bilibili.com/video/av啥啥啥'
]     #待下载的视频列表
queueLock = threading.Lock()
workQueue = queue.Queue(30)
threads = []
threadID = 0
 
if __name__ == '__main__':
    # 创建新线程
    for tName in threadList:
        thread = myThread(threadID, tName, workQueue)
        thread.start()
        threads.append(thread)
        threadID += 1
    # 填充队列
    queueLock.acquire()
    for word in videoList:
        workQueue.put(word)
    queueLock.release()
    # 等待队列清空
    while not workQueue.empty():
        pass
    # 通知线程是时候退出
    exitFlag = 1
    # 等待所有线程完成
    for t in threads:
        t.join()
    print("退出主线程")
