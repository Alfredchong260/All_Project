import datetime

# date 日期 time 时间
# datetime 日期时间 封装了 time 时间
birth_day = datetime.datetime(1949, 10, 1, 0, 0, 0)
today = datetime.datetime.today()  # 获取的是当前的时间
print(today)
print(today.strftime('%Y-%m-%d %H:%M:%S'))
print(dir(today))
print(today.weekday())  # 0 - 6 表示星期一到星期日
print(today.date())  # 0 - 6 表示星期一到星期日
print(today.time().strftime('%H:%M:%S'))  # 0 - 6 表示星期一到星期日

print('today:\t', today)
one_day = datetime.timedelta(days=1)  # timedelta 时间差对象
one_hour = datetime.timedelta(hours=1)  # timedelta 时间差对象
print(type(today))
print(type(one_day))  # 两个不同的类可以实现四则运算
print('today:\t', today - one_day * 10)
print('today:\t', today - one_day * 100)
print('today:\t', today - one_hour * 100)
diff = today - birth_day
print(diff)
print(diff.days)
print(dir(diff))
