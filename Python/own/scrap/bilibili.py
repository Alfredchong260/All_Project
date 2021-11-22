from pprint import pprint
import requests
import re

headers = {
    'referer': 'https://www.bilibili.com/video/',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

def sendRequests(url):
    response = requests.get(url)
    
    return response

def getVideoInfo(bv_id):
    '''首次请求指定网站'''
    url = f'https://www.bilibili.com/video/{bv_id}'
    response = requests.get(url, headers=headers)

    return response

def parseData(response):
    '''解析出需要的数据'''
    title = re.findall('<title data-vue-meta="true">(.*?)</title>', response.text, re.S)[0]
    cid = re.findall('"cid":(.*?),', response.text, re.S)[0]
    session = re.findall('"session":"(.*?)"', response.text, re.S)[0]
    print(title, cid, session)

def getVideoContent(bv, cid, session):
    '''获取视频url以及音频url'''
    url = f'https://api.bilibili.com/x/player/playurl?cid={cid}&qn=32&type=&otype=json&fourk=1&bvid={bv}&fnver=0&fnval=9768&session={session}'
    json_data = sendRequests(url).json()

    pprint(json_data)

bv = 'BV1Db411b7Vx'
cid = '78922728'
session = '599644f1907897062216365f5cfadd9d'

# response = getVideoInfo(bv)
# parseData(response)
getVideoContent(bv, cid, session)
