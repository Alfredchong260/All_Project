import requests

url = 'https://maoyan.com/board/4?offset=0'

headers = {
    # Cookie 用户身份的标识, 能不加就不加
    'Cookie': '__mta=244152890.1603971211691.1618042413519.1618044198851.63; __mta=244152890.1603971211691.1618044198851.1634124634500.64; _lxsdk_cuid=1757422618bc8-00cec1fb04d25d-303464-1fa400-1757422618bc8; uuid_n_v=v1; uuid=E0B4C05015EC11ECACB66DD114C789FB42997E34249C405FA4FC35FA6C611AF3; _lxsdk=E0B4C05015EC11ECACB66DD114C789FB42997E34249C405FA4FC35FA6C611AF3; __mta=244152890.1603971211691.1632809679672.1632897727972.102; _csrf=79e19b30f4bcd25ff46a2e6c2f2bc92e4fa22a1d01371d99f6d18cb0aa227212; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1632723474,1632809677,1632897725,1634124634; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1634124634; _lxsdk_s=17c796b196a-071-0ec-cd1%7C%7C3',
    'Host': 'maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

response = requests.get(url, headers=headers)
print(response.text)

"""
method: 请求方法 get post
url: 请求网址(数据所在的地址)

headers: (可选的) 请求头字段的关键字参数
cookies: (可选的) 用户身份标识, 字典
proxies: (可选的) ip代理的关键字参数

params: (可选的) 请求的查询参数
data: (可选的) 请求的请求参数 <post请求>

timeout: (可选的) 设置请求响应的时间, 一旦超过, 程序会报错
allow_redirects: (可选的) 是否允许重定向, 默认是允许的
verify: (可选的) 是否验证证书< ca证书 ssl证书 >  如果代码请求的地址没有证书, 程序会报错

json: (可选的) json提交的请求参数<post请求>

files: (可选的) 文件
auth: (可选的) 权限认证
"""


