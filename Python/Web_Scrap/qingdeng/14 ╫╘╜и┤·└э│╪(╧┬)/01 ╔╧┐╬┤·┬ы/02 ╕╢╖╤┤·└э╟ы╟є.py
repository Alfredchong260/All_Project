import requests


def get_proxy():
    """获取代理的函数"""
    proxy_json = requests.get(
        url='http://tiqu.pyhttp.taolop.com/getip?count=1&neek=13873&type=2&yys=0&port=1&sb=&mr=2&sep=0&ts=1&ys=1&cs=1&time=2').json()
    print('获取到的代理:', proxy_json)
    proxy = proxy_json['data'][0]['ip'] + ":" + str(proxy_json['data'][0]['port'])
    print('提取出来的代理:', proxy)

    proxies = {
        "http": "http://" + proxy,
        "https": "http://" + proxy,
    }
    return proxies


# get_proxy()

"""用代理请求百度"""
headers = {
    # 'Cookie': '__mta=244152890.1603971211691.1618042413519.1618044198851.63; __mta=244152890.1603971211691.1618044198851.1634556705566.64; _lxsdk_cuid=1757422618bc8-00cec1fb04d25d-303464-1fa400-1757422618bc8; __mta=244152890.1603971211691.1632809679672.1632897727972.102; uuid_n_v=v1; uuid=3C2172202DB811EC8BAB0F3D6466135E2D04577D7E3E440993213828E3D7F8DB; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk=3C2172202DB811EC8BAB0F3D6466135E2D04577D7E3E440993213828E3D7F8DB; _csrf=b4fd5c105a55e10f7c106c4df06b659df542bc4cd7b4fd7a010994c86b40807d; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1632897725,1634124634,1634302984,1634556705; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1634556705; _lxsdk_s=17c932bfabb-4b5-2bd-8e%7C%7C2',
    # 'Host': 'maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
response = requests.get(url='https://movie.douban.com/top250', headers=headers, proxies=get_proxy())
print(response.text)
