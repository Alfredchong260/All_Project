import requests
import execjs

url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

headers = {
    'Cookie': 'OUTFOX_SEARCH_USER_ID=1223187872@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=947712054.6160226; _ntes_nnid=435facd8204fccbdfd4fbc82223ed9ce,1629277310982; JSESSIONID=aaatHaN0RxuABdxsYgU0x; ___rl__test__cookies=1637156091884',
    'Host': 'fanyi.youdao.com',
    'Referer': 'https://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

while True:
    word = input('请输入你要翻译的字：')

    if word == '0':
        break

    with open('./youdao.js', 'r', encoding='utf-8') as r:
        js = r.read()

    compile_result = execjs.compile(js)
    encode_result = compile_result.call('youdao', word)

    data = {
        'i': '你好',
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        # 'salt': '16371560918901',
        # 'sign': 'dcf2398c5d444279fe519f561b5244b7',
        # 'lts': '1637156091890',
        # 'bv': 'ff04ea1796cbff534bc8b37e6dd25131',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME',
    }
    data.update(encode_result)

    response = requests.post(url, headers=headers, data=data)
    print(response.json())
