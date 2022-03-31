import concurrent.futures
from tqdm import tqdm
import requests
import re

headers = {
    'Host': 'www.enterdesk.com',
    'Referer': 'https://www.google.com/',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
}
url = 'https://www.enterdesk.com'

response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding
print(response.text)
