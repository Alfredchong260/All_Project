# 1. 找数据请求地址
import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'

params = {'op': 'keyword'}

# 构建的post请求的请求参数<表单数据>
data = {
    'cname': '',
    'pid': '',
    'keyword': '北京',
    'pageIndex': '1',
    'pageSize': '10',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

# 2. 请求数据
# data 关键字传递post请求提交的请求参数
response = requests.post(url=url, params=params, headers=headers, data=data)
json_data = response.text
print(json_data)
