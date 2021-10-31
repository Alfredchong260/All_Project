import csv

list_dict = [{'first_name': 'Baked', 'last_name': 'Beans'},
             {'first_name': 'Lovely'},
             {'first_name': 'Wonderful', 'last_name': 'Spam'}]

with open('dict.csv', mode='a', encoding='utf-8', newline='') as f:
    # csv 数据专门字典特有的一个方法
    # DictWriter
    #     第一个参数就是打开的文件对象
    #     第二个参数就是使用字典写数据的时候, 可以根据字典的键作为csv的表头
    fieldnames = ['first_name', 'last_name']
    csv_write = csv.DictWriter(f, fieldnames=fieldnames)

    # 写入表头
    csv_write.writeheader()
    # 写入数据
    for i in list_dict:
        csv_write.writerow(i)