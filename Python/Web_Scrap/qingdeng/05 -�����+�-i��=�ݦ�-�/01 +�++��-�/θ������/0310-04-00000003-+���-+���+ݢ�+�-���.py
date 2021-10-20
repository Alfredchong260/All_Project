"""
    使用 css 选择器将快代理中我需要的信息提取出来。
    目标网址：https://www.kuaidaili.com/free/
    
    需要解析以下数据:
        ip、
        port、
        类型
	
	提取出来print（）打印即可
	温馨提示: 爬取速度不要太快,加延迟,避免被封导致以后请求不到数据!
"""

import requests
import parsel
import time  # 时间模块, 内置模块

# 1.找数据对应的地址
url = 'https://www.kuaidaili.com/free/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

# 2.请求数据
response = requests.get(url=url, headers=headers)
html_data = response.text
# 对比数据(确认数据已经请求下来了)
print(html_data)

# 3.解析数据
selector = parsel.Selector(html_data)

trs = selector.css('.table.table-bordered.table-striped tbody tr')  # 所有的tr标签

for tr in trs:
    ip = tr.css('td:nth-child(1)::text').get()
    port = tr.css('td:nth-child(2)::text').get()
    type_ = tr.css('td:nth-child(4)::text').get()

    print(ip, port, type_)
