import time
import threading


def work():
    print('5. 洗茶杯：1min')
    time.sleep(1)
    print('6. 放茶叶：1min')
    time.sleep(1)


start_time = time.time()
print('1. 洗壶：1min')
time.sleep(1)
print('2. 灌凉水：1min')
time.sleep(1)
print('3. 烧水：1min')
time.sleep(1)
print('4. 等水烧开：3min')
# 多线程任务需要在等待之前发布
t1 = threading.Thread(target=work)
t1.start()
time.sleep(1)  # 等水烧开的时间
time.sleep(1)  # 等水烧开的时间
time.sleep(1)  # 等水烧开的时间

# 5 6 这两步需要在等水烧开的时候去做
# print('5. 洗茶杯：1min')
# time.sleep(1)
# print('6. 放茶叶：1min')
# time.sleep(1)

print('7. 泡茶：1min')
time.sleep(1)
print('花费的时间:\t', time.time() - start_time)  # time.time() 获取当前的时间(秒)

# 多线程的作用是将普通对象变成多线程对象
