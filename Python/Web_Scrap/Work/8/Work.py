#知足的喷瓜

'''
    全局思路：
        把页面源代码全部爬取下来
        再以正则将所有内层链接筛选出来
        之后将所有代码封装
        最后把数据写入txt文本

    问题：
        1. 有某些链接并不属于内层链接
        2. 内层链接的标题获取方法并不一致，所以没办法通过一次的re.findall()函数获取所有标题
        3. 抓取出的数据太多，太杂乱，且有些数据并不需要
        4. 数据都以列表的形式进行保存，当以格式对数据进行修饰时，数据混合在一起了，没办法以正常的形式显示
    解决方法：
        1. 判断数据开头是否是https，是就继续下一步操作，不是就将其筛选出来
        2. 以if条件来区别，各分配不同的寻标题方法
        3. 以if条件来辨别那些数据需要并纳入列表中，不需要的数据则无视
        4. 以zip的方法将两个列表合并起来，再以for循环依次把数据导入
'''

import requests 
import re

url = 'https://www.shiguangkey.com/'

headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

# 用re得到数据后进行二次修饰
def getTitle(titles):
    li = []
    for tit in titles:
        if tit[0] == "<":
            li.append(tit.split("05d8fb82>")[-1].replace("\n", '').replace('      ', ''))
        else:
            li.append(tit.replace("\n", '').replace('      ', ''))
    return li

# 得到需要的内层链接
def getLink(links):
    count = 0
    li = []
    for link in links:
        if link[0:5] == "https":
            if link.split(".com/")[1].split("/")[0] == "course":
                count += 1
                while 1 < count <= 7:
                    # print(link)
                    li.append(link)
                    break
                while 40 > count > 7:
                    # print(link)
                    li.append(link)
                    break

            elif link.split(".com/")[1].split('/')[0] == "goodsDetail":
                # print(link)
                pass
            else:
                pass
        else:
            pass
    return li

def writeInTXT(result):
    with open("课堂.txt", "a+") as f:
        f.write(result)

# 设置格式来编排数据
def format(links_, titles_):
    format = '''标题：{}\n网址：{}\n\n'''.format(titles_, links_)
    return format

# 请求网页得到源代码
def main():
    response = requests.get(url, headers=headers)
    response = str(response.text)

    # 以re来得到需要的数据
    links = re.findall('a href="(.*?)" ', response, re.S)
    tits = re.findall('data-v-05d8fb82>(.*?)</a>', response, re.S)

    # 调用函数来修饰数据
    links_ = getLink(links)
    titles_ = getTitle(titles=tits)

    # 以列表保存多个数据，再以for循环逐个显示
    results = []
    
    for i,j in zip(links_, titles_):
        results.append(format(links_=i, titles_=j))

    for result in results:
        writeInTXT(result)

# 调用主函数
main()
