import requests
import time
import random
import hashlib

"""
navigator.appVersion与用户代理有关(是一个常量)
(new Date).getTime() 与时间戳非常相近，就是当前时间乘于1000取整
parseInt(10 * Math.random(), 10) 生成一个0-10的随机数
"""

class youdao:
    def __init__(self,url,header,word):
        self.url = url
        self.header = header
        self.word = word
 
    # 获取lit参数
    def get_lit(self):
        self.lit = int(time.time()*1000)

        return self.lit
 
    # 获取salt参数
    def get_salt(self, lit):
        self.num = int(random.random()*10)
        self.salt = str(lit) +str(self.num)

        return self.salt
 
    # 获取sign参数
    def get_sign(self, salt):
        left = 'fanyideskweb'
        e = self.word
        i = salt
        right = 'Y2FYu%TNSbMCxc3t2u^XT'
        str_data = left+e+i+right

        # 创建md5的实例对象
        m=hashlib.md5()
        # 传入参数
        m.update(str_data.encode('utf-8'))
        # 进行解密
        sign = m.hexdigest()

        return sign
 
    # 获取data
    def get_data(self):
        lit = self.get_lit()
        salt = self.get_salt(lit)
        from_data = {
            'i': self.word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt, # i
            'sign': self.get_sign(salt),
            'lts': lit, # r
            'bv': '89e18957825871c419be045180c67d3b',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }

        return from_data
 
 
if __name__ == '__main__':
    url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'Referer': 'https://fanyi.youdao.com/',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-54507737@10.169.0.83; OUTFOX_SEARCH_USER_ID_NCOO=653767550.7334615; JSESSIONID=aaa51jghzLCTy8aXj-tTx; ___rl__test__cookies=1629201696472'
    }
    word = input('请输入要翻译的单词：')
    fanyi = youdao(url,headers,word)
    r = requests.post(url,headers=headers,data=fanyi.get_data())
    data = r.json()
    # print(data)
    print('输入单词：{}\n翻译为{}：'.format(data['translateResult'][0][0]['src'],data['translateResult'][0][0]['tgt']))
