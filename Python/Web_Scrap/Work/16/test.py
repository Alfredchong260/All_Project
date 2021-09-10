import requests

headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}

response = requests.get('https://m3api.awenhao.com/index.php?note=kkRp738drbtca264gexj1&raw=1&n.m3u8', headers=headers)
print(response)
