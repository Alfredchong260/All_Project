


# 1.找数据所对应的地址
import parsel
import requests

base_url = 'https://www.jdlingyu.com/tuji'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

# 2. 发送请求
response = requests.get(url=base_url, headers=headers)
html_data = response.text
# print(html_data)

# 3. 数据解析 xpath
selector = parsel.Selector(html_data)
url_list = selector.xpath('//div[@class="post-module-thumb"]/a/@href').getall()  # 得到了每一个相册详情页地址
# print(url_list)

for url_ in url_list:
    html = requests.get(url=url_, headers=headers).text

    selector_2 = parsel.Selector(html)
    pic_url_list = selector_2.xpath('//div[@class="entry-content"]//img/@src').getall()
    # print(pic_url_list)

    # 继续请求图片数据
    for pic_url in pic_url_list:
        pic_data = requests.get(url=pic_url, headers=headers).content

        file_name = pic_url.split('/')[-1]
        with open('img\\' + file_name, mode='wb') as f:
            f.write(pic_data)
            print('下载完成:', file_name)


# Alt + enter