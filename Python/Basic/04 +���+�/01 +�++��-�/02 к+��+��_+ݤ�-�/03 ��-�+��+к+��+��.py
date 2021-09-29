students = [
    {'name': '正心', 'chinese': 59, 'math': 59, 'english': 59, 'total': 177},
    {'name': '张三', 'chinese': 59, 'math': 59, 'english': 59, 'total': 177},
    {'name': '李四', 'chinese': 59, 'math': 59, 'english': 59, 'total': 177},
    {'name': '王五', 'chinese': 59, 'math': 59, 'english': 59, 'total': 177},
]

print('姓名\t\t语文\t数学\t英语\t总分')  # 汉字 和 字母/字符串
for stu in students:
    print(f'{stu["name"]}\t\t{stu["chinese"]}\t\t{stu["math"]}\t\t{stu["english"]}\t\t{stu["total"]}')

