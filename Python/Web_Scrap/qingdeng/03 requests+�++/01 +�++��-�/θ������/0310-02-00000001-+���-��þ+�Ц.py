"""
	目标地址：https://maoyan.com/board/4?offset=0
	
	要求：
		1、请求到目标网址数据，需要在请求到的数据中看到当前页面所有的电影名字、主演、上映时间、评分等信息
		2、请列举在请求不到数据时，需要添加几个常见请求头字段（课程讲过）
		    User-Agent: 浏览器的身份标识
		    Host: 请求的客户端指定想要请求的域名地址
		    Cookie: 用户身份的标识, 能不加就不加
		    Referer: 防盗链, 告诉服务器, 咱们是从哪里过来的
		    Origin: 资源的起始位置<url地址 />
请在下方编写代码
"""
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


