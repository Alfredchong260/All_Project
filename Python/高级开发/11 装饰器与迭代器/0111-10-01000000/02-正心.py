"""
    中华人民共和国建国与1949年10月1日，请你计算到今天为止，中国总共成立了多少秒
"""

import time
import datetime

"""解法1"""
birth_day = time.strptime('1949-10-1', '%Y-%m-%d')
print(birth_day)

now = time.localtime()
print(now)

if (now.tm_mday >= birth_day.tm_mday) and (now.tm_mon >= birth_day.tm_mon):
    print('time', now.tm_year - birth_day.tm_year)
else:
    print('time', now.tm_year - birth_day.tm_year - 1)

# 年 月 日 小时 分钟 秒

"""解法2"""
birth_day_datetime = datetime.datetime(1949, 10, 1)
print(birth_day_datetime)

now_datetime = datetime.datetime.now()
diff = now_datetime - birth_day_datetime

diff_y = datetime.timedelta()  # 时间差对象 时间日期差对象
print('时间差对象:\t', diff_y)
print(diff.seconds)
