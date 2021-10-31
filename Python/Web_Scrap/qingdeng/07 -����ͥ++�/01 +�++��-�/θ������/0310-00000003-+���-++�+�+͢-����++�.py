"""
    目标网址: http://www.win4000.com/zt/dongman.html
    
    需求:
        "动漫桌面壁纸" 文字下面有很多动漫图集
        1、用xpath采集数据
        2、采集以下信息
            采集动漫图集的标题
            采集动漫图集中图片对应的url地址
            
        解析到数据用print()函数打印即可
请在下方编写代码：
"""
import parsel
import requests

url = 'http://www.win4000.com/zt/dongman.html'
# headers  能不加请求头得到数据可以不用加
headers = {
    # cookies可能会过期, cookies是有缓存时间
    'Cookie': 't=99ede285abd6095f2499765e4ddcf0d3; r=9450; Hm_lvt_492109f03bd65de28452325006c4a53c=1603797972,1603809068,1604307205,1604401143; XSRF-TOKEN=eyJpdiI6IjZoOWZraWZQbXdFWFwvR0xjNVlQNFRRPT0iLCJ2YWx1ZSI6IjRrZzZaU0tQbkVsK29iOGlyb1VqRU5iaW4rQ3FTaDRuVXBKc3NVTWNFVnV2XC84ZHoxbjE1SDZ6UHhwSGRNalg3XC94MjcrWDExdTZoekVkXC9UbzJRNnVHczdEZHdrWWNPRm9zd3pFTDZ5UExYNWErang1SmxjeDVMYnBvaTR3UXJuIiwibWFjIjoiOTYxZjk5OTg2YThkODY4ZDllMTMzOTE3OWE4NmM4ZDdlYjg2N2VjZDkwNGY1ZTE0OTNhNTgyMDRmOWFlZGU4MyJ9; win4000_session=eyJpdiI6IkxYaHlER1NFUWJJWmh2QzQxV3VMalE9PSIsInZhbHVlIjoiRkxcLzNQNXg2NEpQVXl1UndyaHpXTXBUeW1BUGhvR0RNZFp3M0lpVDF4VWJyanZaNlZFRHFGZHlcLzc2dlpuS01VM000emtzTStHd2lBV3gySkRMb25oYys2eGlDN2wrOXJjenZWMU1lNkNFeSt3QlFhQURERytlUTRTcEUyUmVzQiIsIm1hYyI6IjdiZmRhMjgzZTk4MDllYTM0YjI1ODE3Mjk4OGZmZTM1YmRlZjExN2UwYmVmOWNmMjM1NWIwYWY0OWNmZmZmZGIifQ%3D%3D; UM_distinctid=17ca7c1933017-081cd2b8b16e27-b7a1438-1fa400-17ca7c1933174b; CNZZDATA1279885023=1980447931-1625050533-null%7C1634896025',
    'Host': 'www.win4000.com',
    'Referer': 'http://www.win4000.com/zt/dongman.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}

# 2. 发送地址请求
response = requests.get(url=url, headers=headers)
html_data = response.text
# print(html_data)


# 3. 数据解析
selector = parsel.Selector(html_data)
lis = selector.xpath('//div[@class="list_cont Left_list_cont  Left_list_cont1"]//ul/li')

for li in lis:
    title = li.xpath('./a/p/text()').get()
    img_url = li.xpath('./a/img/@data-src').get()
    print(title, img_url)

