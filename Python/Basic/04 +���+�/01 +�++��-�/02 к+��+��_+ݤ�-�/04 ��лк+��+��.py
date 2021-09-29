students = [
    {'name': '正心', 'chinese': 59, 'math': 59, 'english': 59, 'total': 177},
    {'name': '张三', 'chinese': 59, 'math': 59, 'english': 59, 'total': 177},
    {'name': '李四', 'chinese': 59, 'math': 59, 'english': 59, 'total': 177},
    {'name': '王五', 'chinese': 59, 'math': 59, 'english': 59, 'total': 177},
]


# 姓名?
name = input('请输入你想要查找学生的姓名')

for stu in students:  # 遍历所有学生
    if name == stu['name']: # 满足这个条件, 代表要查找的学生找到了
        print('姓名\t\t语文\t数学\t英语\t总分')
        print(f'{stu["name"]}\t\t{stu["chinese"]}\t\t{stu["math"]}\t\t{stu["english"]}\t\t{stu["total"]}')
        # 整个系统没有重名的
        # 找到了学生我就不继续找了
        break

else:
    # 如果没有找到学生, 就会走else的逻辑
    print('该学生不存在, 请检查名字是否输入正确')





