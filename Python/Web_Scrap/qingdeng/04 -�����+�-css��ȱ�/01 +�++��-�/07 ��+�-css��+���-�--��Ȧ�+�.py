import requests
import parsel

response = requests.get('https://www.biquwx.la/10_10582/5103238.html')

response.encoding = response.apparent_encoding

html_data = response.text
# print(html_data)

# 数据解析
# 1. 转换数据类型
selector = parsel.Selector(html_data)

# 2. 使用css语法解析数据
bookname = selector.css('.bookname h1::text').get()
print(bookname)


content = selector.css('#content::text').get()
print(content)