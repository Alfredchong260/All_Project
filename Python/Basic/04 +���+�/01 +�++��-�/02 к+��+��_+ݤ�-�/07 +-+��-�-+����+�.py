
students = [
    {'name': '正心', 'chinese': 59, 'math': 59, 'english': 59, 'total': 177},
    {'name': '张三', 'chinese': 59, 'math': 59, 'english': 59, 'total': 177},
    {'name': '李四', 'chinese': 59, 'math': 59, 'english': 59, 'total': 177},
    {'name': '王五', 'chinese': 59, 'math': 59, 'english': 59, 'total': 177},
]

import json  # 对象和字符串的转换的模块, 内置模块


# with open('students.json', mode='w', encoding='utf-8') as f:
#     # 把对象<列表 字典>转换成字符串  编码 Unicode编码
#     # ensure_ascii=False  不使用Unicode编码
#     students_str = json.dumps(students, ensure_ascii=False)
#
#     f.write(students_str)

# 读取文件里面的数据
with open('students.json', mode='r', encoding='utf-8') as f:
    students_str = f.read()

    # print(students_str)
    # print(type(students_str))
# 保存的时候需要保存字符串
# 在系统中我们要对象
student = json.loads(students_str)
print(student)
print(type(student))




