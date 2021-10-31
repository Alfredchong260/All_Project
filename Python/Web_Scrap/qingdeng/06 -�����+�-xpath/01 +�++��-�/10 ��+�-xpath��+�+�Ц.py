"""
    使用 css 选择器将猫眼 100 十页全部电影信息全部提取出来。
    目标网址：https://maoyan.com/board/4
    name（电影名）
    star（主演）
    releasetime（上映时间）
    score（评分）
	
	提取出来print（）打印即可
	温馨提示: 爬取速度不要太快,加延迟,避免被封导致以后请求不到数据!
"""
import requests
import parsel
import time   # 时间模块, 内置模块


# 1.找数据对应的地址
url = f'https://maoyan.com/board/4?offset=0'

headers = {
    'Cookie': '__mta=244152890.1603971211691.1618042413519.1618044198851.63; __mta=244152890.1603971211691.1618044198851.1634556705566.64; _lxsdk_cuid=1757422618bc8-00cec1fb04d25d-303464-1fa400-1757422618bc8; __mta=244152890.1603971211691.1632809679672.1632897727972.102; uuid_n_v=v1; uuid=3C2172202DB811EC8BAB0F3D6466135E2D04577D7E3E440993213828E3D7F8DB; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk=3C2172202DB811EC8BAB0F3D6466135E2D04577D7E3E440993213828E3D7F8DB; _csrf=b4fd5c105a55e10f7c106c4df06b659df542bc4cd7b4fd7a010994c86b40807d; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1632897725,1634124634,1634302984,1634556705; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1634556705; _lxsdk_s=17c932bfabb-4b5-2bd-8e%7C%7C2',
    'Host': 'maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

# 2.请求数据
response = requests.get(url=url, headers=headers)
html_data = response.text
# 对比数据(确认数据已经请求下来了)
print(html_data)


# 3.解析数据  # 解析数据之前, 一定要确认数据是否请求到
selector = parsel.Selector(html_data)
dds = selector.xpath('//dl[@class="board-wrapper"]/dd')  # 所有的dd标签

for dd in dds:
    name = dd.xpath('.//p[@class="name"]/a/@title').get()
    star = dd.xpath('.//p[@class="star"]/text()').get().strip()
    releasetime = dd.xpath('.//p[@class="releasetime"]/text()').get().strip()
    score = dd.xpath('.//p[@class="score"]/i/text()').getall()
    score = ''.join(score)

    print(name, star, releasetime,score)




