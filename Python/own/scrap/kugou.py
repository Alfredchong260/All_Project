import requests
import re

url = 'https://www.kugou.com/yy/html/rank.html'

headers = {
    'referer': 'https://www.kugou.com/',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
