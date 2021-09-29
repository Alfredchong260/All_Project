students = [
    {'name': '正心', 'chinese': 59, 'math': 59, 'english': 59, 'total': 177},
    {'name': '张三', 'chinese': 59, 'math': 59, 'english': 59, 'total': 177},
    {'name': '李四', 'chinese': 59, 'math': 59, 'english': 59, 'total': 177},
    {'name': '王五', 'chinese': 59, 'math': 59, 'english': 59, 'total': 177},
]
import pprint

# 如果要删除学生信息, 那么首先得找到
name = input('请输入你想要删除学生的姓名:')

for stu in students:  # 遍历所有学生
    if name == stu['name']:  # 满足这个条件, 代表要删除的学生找到了
        # pop  index
        students.remove(stu)
        break

else:
    print('该学生不存在, 请检查名字是否输入正确')

pprint.pprint(students)
