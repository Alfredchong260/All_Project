import csv

fieldname = ['Name', 'Method', 'Contact']
filename = './NameList.csv'

with open(filename, 'a', encoding='utf-8', newline='\n') as f:
    csv_writer = csv.DictWriter(f, fieldnames=fieldname)
    # csv_writer.writeheader()

    while True:
        name = input('名字：')
        if name.upper() == 'Q':
            break
        method = input('联络方法：')
        if method.upper() == 'Q':
            break
        contact = input('资料：')
        if contact.upper() == 'Q':
            break
        print()
        dict1 = {'Name': name, 'Method':method, 'Contact':contact}
        csv_writer.writerow(dict1)
