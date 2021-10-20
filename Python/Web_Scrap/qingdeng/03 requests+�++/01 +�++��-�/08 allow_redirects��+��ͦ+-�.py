

import requests


url = 'http://github.com/'

# requests如果有重定向, 默认情况下回自动的重定向
# allow_redirects=False  阻止重定向, 默认是 True
response = requests.get(url=url, allow_redirects=False)
print(response.status_code)
