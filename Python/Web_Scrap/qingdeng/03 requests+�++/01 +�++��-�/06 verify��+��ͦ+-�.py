

import requests

requests.packages.urllib3.disable_warnings()  # 忽律关闭证书验证以后引发的浸膏

url = 'https://data.stats.gov.cn/'


# verify 关键字: 是否验证网站证书, 默认情况下是验证的, 值为True
# verify=False  忽略证书验证
response = requests.get(url=url, verify=False)
html = response.text
print(html)
