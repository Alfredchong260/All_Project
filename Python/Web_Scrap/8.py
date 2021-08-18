import requests
import re
import time
import random
import hashlib

'''
正则就是用来获取字符串，可以实现字符串搜索，替换，匹配
正则表达式，匹配的字符串
    \w:匹配字母，数字以及下划线
    \W:匹配不是字母，数字以及下划线
    \s:匹配任意空白字符[\t\n\r\f]
    \S:匹配任意非空白字符
    \d:匹配任何数字,[0-9]
    \D:匹配任意非数字的字符
    ^ :匹配一行字符串的开头
    $ :匹配一行字符串的结尾
    . :匹配任意字符，除了换行符
    * :匹配0个或多个表达式
    ():分组
'''

url = 'https://api.live.bilibili.com/xlive/web-interface/v1/webMain/getList?platform=web'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}

response = requests.get(url, headers=headers, timeout=20)
titles = response.json()['data']['ranking_list']
for title in titles:
    print(title['link'])

content = 'Hello 123 4567 World_This is a Regex Demo'

'''
match()从字符串的起始位子开始匹配正则表达式，
如果匹配就返回成功的结果，
如果不匹配就返回none或者报错
参数：正则表达式，需要匹配的字符串，修饰符(Optional)
'''

# print(content)
# results = re.match('^Hello\s\d{3}\s\d{4}\s\w{10}', content)
# print(results.group())

'''
通用匹配
.*：能匹配换行符以外的任意字符, . 代表匹配任意字符, * 代表匹配任意次数
.*是一个贪婪匹配，默认匹配多个
'''
# result = re.match('.*', content)
# print(result.group())
'''
贪婪    非贪婪  搜索
\d+ 代表可以匹配多个数字，最少匹配一个
'''
result = re.match('^He(.*?)(\d+).*Demo$', content)
print(result.group(1))

'''
修饰符
re.S：使.包括换行符在内的所有字符
'''
# content = '''Hello 123 4567 Wor
# ld_This is a Regex Demo'''

# result = re.match('^He(.*?)(\d+).*Demo$', content, re.S)
# print(result.group(2))

'''
    search():扫描整个字符串，获取第一个匹配到的元素
'''

'''
findall():扫描整个字符串，获取所有匹配到的元素
'''

'''
熟悉正则
'''
