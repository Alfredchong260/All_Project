
import csv  # 内置模块

ll = [[1, 2, 3, 4],
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [5, 6, 7, 8]]

with open('data.csv', mode='a', encoding='utf-8', newline='') as f:
    # 针对列表写表头, 只能用字符串普通方式写入
    f.write('字段1,字段2,字段3,字段4\n')

    """
    newline=''  指定新行, 消除csv数据的空行
    csv.writer(f)   通过csv模块实例化的数据写入对象, 括号内部传递打开的文件对象
    writerow(i)     整行写入数据, i 指代的是一个数据容器(元组,列表) 
    """
    csv_write = csv.writer(f)
    # print(csv_write)
    for i in ll:
        csv_write.writerow(i)
