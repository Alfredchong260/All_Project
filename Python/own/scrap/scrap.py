'''
qq音乐大部分音乐已下架，等以后看它是否会宠幸上架音乐
'''


import random
import requests
from pprint import pprint
import json

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}


proxies = ['HTTP://110.243.30.23:9999', 'HTTP://222.189.191.206:9999',
            'HTTP://106.42.163.100:9999', 'HTTP://120.83.107.69:9999',
           'HTTP://60.13.42.135:9999',  'HTTP://113.195.232.23:9999',
           'HTTP://59.62.36.74:9000', 'HTTP://218.2.226.42:80']

proxy = {'HTTP': random.choice(proxies)}

class qq_music:
    def __init__(self, url):
        self.url = url

    def main(self):
        music_list = self.search()
        print(music_list)

    def search(self):
        li = []
        response = requests.get(url, headers=headers, proxies=proxy).text
        music_json = response[9:-1]
        json_data = json.loads(music_json)
        music_list = json_data['data']['song']['list']
        for music in music_list:
            mid = music['mid']
            name = music['title']
            singer = music['singer'][0]['name']
            li.append((mid, name, singer))

        return li

    def download(self, music_list):
        for music in music_list:
            music_mid = music[0]
            musicn_name = music[1]
            music_singer = music[2]
            url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"8846039534","calltype":0,"userip":""}},"req_0"{"module":"GetVkeyServer","method":"CgiGetVkey","param":{"guid":"8846039534","songmid":["%s"],"songtype":[0],"uin":"1152912504784213523","loginflag":1,"platform":"20"}},"comm":{"uin":"1152912504784213523","format":"json","ct":24,"cv":0}}' % music_mid
            response = requests.get(url, headers=headers, proxies=proxy)
            print(response)

if __name__ == "__main__":
    pages = input('请输入你要查询的资料：')

    url = f'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.top&searchid=64896423324569528&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w={pages}'

    test = qq_music(url)
    test.main()
