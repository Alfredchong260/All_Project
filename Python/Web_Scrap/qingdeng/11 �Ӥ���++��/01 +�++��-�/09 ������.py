import concurrent.futures  # 导入池子模块
import time


def thread_function(name):
    print("子线程 %s: 启动" % name)
    time.sleep(2)
    print("子线程 %s: 完成" % name)


if __name__ == "__main__":

    # ThreadPoolExecutor  创建线程池对象
    # max_workers 最大任务数据
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for i in range(10):
            # executor.submit()   向线程池中提交任务
            executor.submit(thread_function, i)
