import requests

url = 'http://test/mingrisoft.com/uploads/ebook/548/22.jpg'
try:
    response = requests.get(url)
except Exception as e:
    print('Connect Error')
    print(e)
