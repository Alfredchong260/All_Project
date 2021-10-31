
import csv  # 内置模块


with open('data.csv', mode='r', encoding='utf-8', newline='') as f:
    # print(f.read())

    csv_read = csv.reader(f)
    print(csv_read)

    for i in csv_read:
        print(i)

