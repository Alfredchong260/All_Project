students = [
    {'name': '正心', 'chinese': 59, 'math': 59, 'english': 59, 'total': 177},
    {'name': '张三', 'chinese': 59, 'math': 59, 'english': 59, 'total': 177},
    {'name': '李四', 'chinese': 59, 'math': 59, 'english': 59, 'total': 177},
    {'name': '王五', 'chinese': 59, 'math': 59, 'english': 59, 'total': 177},
]

# 如果要修改学生信息, 那么首先得找到

name = input('请输入你想要修改学生的姓名:')

for stu in students:  # 遍历所有学生
    if name == stu['name']: # 满足这个条件, 代表要查找的学生找到了
        # pass  # 语法占位
        print('回车代表使用原来的数据')
        name = input('请重新输入学生姓名:')
        chinese = input('请重新输入学生语文成绩:')
        math = input('请重新输入学生数学成绩:')
        english = input('请重新输入学生英语成绩:')
        #total = chinese + math + english
        if name:
            stu['name'] = name
        if chinese:
            stu['chinese'] = int(chinese)
        if math:
            stu['math'] = int(math)
        if english:
            stu['english'] = int(english)

        stu['total'] = stu['chinese'] + stu['math'] + stu['english']
        break

else:
    print('该学生不存在, 请检查名字是否输入正确')

print(students)