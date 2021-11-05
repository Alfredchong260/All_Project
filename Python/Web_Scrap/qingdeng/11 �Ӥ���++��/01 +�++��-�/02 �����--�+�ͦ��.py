import time
import threading  # 线程模块, 内置模块


def sing():
    # 只有函数对象才能使用多任务
    for i in range(3):
        print(f'正在唱歌...{i}')
        time.sleep(1)


def dance():
    # 只有函数对象才能使用多任务
    for i in range(3):
        print(f'正在跳舞...{i}')
        time.sleep(1)
    # 如果要计算线程执行任务的时间, 只能写在线程对应函数的内部计算
    print('执行任务花费时间: ', time.time() - start_time)


# sing()
# dance()

start_time = time.time()  # 开始时间


print('当前线程任务数量: ', threading.enumerate())

# threading.Thread(target=sing)  把 sing 函数转换成线程对象
sing_thread = threading.Thread(target=sing)
# .start()  执行线程任务
sing_thread.start()

print('当前线程任务数量: ', threading.enumerate())

dance_thread = threading.Thread(target=dance).start()
# dance_thread

print('当前线程任务数量: ', threading.enumerate())

"""
实现多线程的步骤
    1. 把普通的函数对象转换成线程对象 threading.Thread()
    2. 执行多线程  线程对象.start()
"""

