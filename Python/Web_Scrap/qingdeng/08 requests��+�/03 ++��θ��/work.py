import requests
import csv

url = 'https://index.mysteel.com/zs/newprice/getChartMultiCity.ms'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

params = {
    'catalog': '%E7%BA%BF%E6%9D%90_:_%E7%BA%BF%E6%9D%90',
    'city': '%E6%9D%AD%E5%B7%9E',
    'spec': '6%E9%AB%98%E7%BA%BFHPB300_:_HPB300_6%E9%AB%98%E7%BA%BF',
    'startTime': '2021-07-01',
    'endTime': '2021-10-01',
    'callback': 'json',
    'v': '1635252906571'
}

fieldnames = ['CityName', 'Date', 'Value']

response = requests.get(url, headers=headers, params=params)
print(response.json())

with open('钢铁.csv', 'w', encoding='utf-8') as w:
    name = response.json()['data'][0]['lineName']
    csv_writer = csv.DictWriter(w, fieldnames=fieldnames)
    csv_writer.writeheader()

    for data in response.json()['data'][0]['dateValueMap']:
        date = data['date']
        value = data['value']
        csv_writer.writerow(
            {
                'CityName': name,
                'Date': date,
                'Value': value
            }
        )

