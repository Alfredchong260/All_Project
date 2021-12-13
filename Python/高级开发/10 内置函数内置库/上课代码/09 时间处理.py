import time

print(time.time())
# 时间戳是一个浮点数
print('时间戳(10):', time.time())
print('时间戳(13):', time.time() * 1000)
print('时间戳(hex):', hex(int(time.time() * 1000)))

# 结构化时间是一个对象性
local_time = time.localtime(1639144390)  # 可以传入一个时间戳(10)
print('结构化时间对象:', local_time)
print(local_time.tm_mon)
print(local_time.tm_mday)

# 字符串时间
print(time.strftime('%Y-%m-%d %H:%M:%S %p', local_time))

# 2021-12-10 21:53:10
old_time = time.strptime('2021-12-10 21:53:10', '%Y-%m-%d %H:%M:%S')
print(old_time)

print(time.mktime(old_time))
# 电脑时间同步,然后获取电脑时间
