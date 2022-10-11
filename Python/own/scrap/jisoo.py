import requests
import parsel

links = ['https://www.wumaow.org/tu/2887464_5.html', 'https://www.wumaow.org/tu/942171.html', 'https://www.wumaow.org/tu/4877493.html',
         'https://www.wumaow.org/tu/2887464.html', 'https://www.wumaow.org/tu/4682257.html', 'https://www.wumaow.org/tu/4877495.html', 'https://www.wumaow.org/tu/4877497.html']


for link in links:
    response = requests.get(link)
    selector = parsel.Selector(response.text)
    break