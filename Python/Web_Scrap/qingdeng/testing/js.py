import requests

url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'

headers = {
    'Cookie':'BIDUPSID=C446A34D9A0E02D0A9DB1EF7C8F615B0; PSTM=1629201683; BAIDUID=68B47A0424275A7D6331D3654050A4AE:FG=1; BAIDUID_BFESS=9E3BDCB0DF63363F1046E90F96AFD8C2:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1637151964; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1637151964; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; __yjs_st=2_ZDIyNDQ4ZjdjN2Y5MGMyZTA4YjEzM2ZkOGQ4YmRmZjdmM2ZiNzgyOWIyYmI1ZGVlMjM3Y2UyN2M2MGVlYTgyOWU5NTllN2U4M2U3NmE5NjIwZjFmOWE0NmU0ZTY2ZmMwNmE4ODkxNjgzMWIzM2EwZjkzMjFhOTFhZTRmNzM3NGI1Y2U5YjIxMjRlZGU5YzJiM2EwOTc1ZWQxNjk5YTU3ODE2YWViMDhiMTk1ZjcwMWFjNDM5NWJjODQ2MjUyNDc2NzY0YTkwZWZkMTFkNzMwZmZlZmNiYTE5ZTVjNzkxN2Y1YTE1NThmNDllYmQ2ZmYxMTI2NmJlMGYyN2EwNzliYl83XzdjM2U0ZDBm; ab_sr=1.0.1_ZDc3YTE4NDc4ZDNkM2IzNTg4NjI4ODg1ZjI1ZTQ1YjQ0MmNiNWQ2MzY5ODk3MmVhZDg0Y2ZjZTdiNDcwOThlNzFkYmQxMWRmYmYxYzQ4MzkwOTQyMDAxYjhlY2RjMzZkMDIzM2EzYWE5N2Q3ZWNiZTg0YThlN2ZhMzhhN2YxZjlkMGI5OTZlOWFkMzQxNjU2YjI3ZDRkZDdhOGU2MWNhNQ==',
    'Host': 'fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

data = {
    'from': 'zh',
    'to': 'en',
    'query': '你好',
    'transtype': 'realtime',
    'simple_means_flag': 3,
    'sign': 232427.485594,
    'token': '1d8a2bfd68c15719300f8b6fbe6ef0ce',
    'domain': 'common'
}

response = requests.post(url=url, json=data)
print(response.json())
