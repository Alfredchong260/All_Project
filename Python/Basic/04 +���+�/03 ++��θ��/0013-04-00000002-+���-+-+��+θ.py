arr = ['1', '2', 3, 4, 5, '6', '7']

"""
请将 arr 保存到本地文件

文件名为: hello.txt
文件内容: 1,2,3,4,5,6,7
"""
import json

arr1 = []
for i in arr:
    new = int(i)
    arr1.append(new)

data = json.dumps(arr1)

with open('./hello.txt', 'w', encoding='utf-8') as w:
    w.write(data)

