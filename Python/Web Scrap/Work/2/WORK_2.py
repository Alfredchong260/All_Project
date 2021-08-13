import urllib.request
import requests

header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
response = requests.get('https://github.com/', headers=header)

print(response.text)
