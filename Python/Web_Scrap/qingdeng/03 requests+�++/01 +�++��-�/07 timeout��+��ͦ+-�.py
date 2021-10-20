

import requests


url = 'https://data.stats.gov.cn/'

try:
    # timeout 设置请求的时间, 单位秒, 超过这个时间程序会报错(Read timed out), 可以通过异常捕获解决
    response = requests.get(url=url, verify=False, timeout=0.5)
    html = response.text
    print(html)
except Exception as e:
    print(e)
