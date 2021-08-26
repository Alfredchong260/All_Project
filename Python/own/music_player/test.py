import requests

url = 'http://192.168.1.112:3000/'
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Cookie':'__yjs_duid=1_6bd3377ef46f6203ea63409ef4dffd971629885864481; PHPSESSID=72o0t5oie57di9maqk84449vu4; __gads=ID=418055555e8f673a-2252820619cb0092:T=1629885868:RT=1629885868:S=ALNI_MZCd3eW7zFPI-5SMiA8Rm6E92drlQ; notice=1'
}
param = {
    "songName": 10,
    "id": 1.2
}

r = requests.post(url, headers=headers, params=param)
print(r)
