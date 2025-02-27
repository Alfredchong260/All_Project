# 1. 找数据请求地址
import execjs
import requests

url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'


headers = {
    # 百度翻译必须加 cookies
    'Cookie': 'BAIDUID=D4B444FE78CBB3678CAE11C526796E68:FG=1; __yjs_duid=1_0a8d75cb5648c564de71ed2e03d94b0b1618921552610; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; PSTM=1618925144; BIDUPSID=50AE456C4D0161AF2C9CFC1C0156FB10; MCITY=-158%3A; BDUSS=mNIVzFHZ3JEZ1k5NnBmTkpFdk03VW56dmRaR1Z-ZEVoNmQzcGprSllOWVdzSWRoRVFBQUFBJCQAAAAAAAAAAAEAAAD9hL2nuti-~M~oMzEzNjQxOQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYjYGEWI2Bhb; BDUSS_BFESS=mNIVzFHZ3JEZ1k5NnBmTkpFdk03VW56dmRaR1Z-ZEVoNmQzcGprSllOWVdzSWRoRVFBQUFBJCQAAAAAAAAAAAEAAAD9hL2nuti-~M~oMzEzNjQxOQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYjYGEWI2Bhb; H_WISE_SIDS=110085_127969_132548_164325_178384_178637_179345_179380_179449_181133_181135_181482_181588_182000_182273_182529_183030_183330_183630_183976_184012_184321_184655_184735_184794_184811_185029_185036_185306_185517_185635_185879_185924_186039_186319_186411_186597_186643_186716_186743_186831_186844_186894_187019_187084_187121_187206_187215_187287_187418_187485_187532_187562_187605_187668_187726_187789_187815_187877_187929_188181_188294_188426_188521_188733_188754_188832_188846_188898_189056_189096_189097_189143; BAIDUID_BFESS=D4B444FE78CBB3678CAE11C526796E68:FG=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=7; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=34837_34067_31254_34657_34584_34518_34830_1996_26350_34627_34473_34700; BA_HECTOR=0004258hah84a52l5o1gmdojm0q; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1632641112,1632987239,1632987320,1634132601; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1634132601; ab_sr=1.0.1_MzFjZWQzYzgwZTRkNGUyYWUwZmZjYjIxNTdhZWI3OTczNWM5MmIwYjdhOGJjMDBmZTA3N2VlMDQ2NWQ4Y2I2ODcwZGNmODZmNDk3NjE0ZDU1YzNiNzEwMDFmZTg1OTM5N2VlNjJkNTk5NTI1MmQ2NDZkMTI0NDEwMjJlYzMzZDA3NTBmNmQyZmRjZGEzZDQ5YWFkZGNmNjkxYTlhOWI0MTUwNDA3ZjZkNGM1Njk1NmJmZjQ2YzlhYmI0NGJjZWNm',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}


while True:
    word = input('请输入你要翻译的汉字(输入0退出系统):')

    if word == '0':
        break

    with open('02 百度翻译js解密.js', mode='r', encoding='utf-8') as f:
        js_code = f.read()
    compile_result = execjs.compile(js_code)  # 传入js代码, 编译
    encode_result = compile_result.call('e', word)  # 得到加密的数据


    data = {
        'from': 'zh',
        'to': 'en',
        'query': word,
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': encode_result,
        'token': '29393d4cb49253d48d82066cf4824d95',
        'domain': 'common',
    }


    response = requests.post(url=url, headers=headers, data=data)
    json_data = response.json()
    """提取返回的翻译的结果"""
    fanyi_result = json_data['trans_result']['data'][0]['dst']
    print(fanyi_result)



