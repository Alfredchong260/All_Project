"""
学生信息管理系统, 自己跟着案例录播实现一遍
"""
'''
    增删改查
'''
"""请在下方实现"""

welcome = '''***************************************************
欢迎使用学生管理系统 v1.0
    1. 增加学生信息
    2. 修改学生信息
    3. 查询学生信息
    4. 显示所有学生信息
    5. 删除学生信息
    0. 退出本系统
***************************************************'''

import json

with open('stu_info.json', 'r', encoding='utf-8') as f:
    data = f.read()
stu_list = json.loads(data)

def add():
    name = input('请输入学生姓名：')
    chinese = input('请输入语文成绩：')
    english = input('请输入英语成绩：')
    math = input('请输入数学成绩：')
    if chinese and english and math:
        total = int(chinese) + int(english) + int(math)
        stu_list.append({'name':name, '语文':chinese, '英语':english, '数学':math, '总分':total})
    else:
        print('输入无效成绩，请重新输入')
        add()

def modify():
    name = input('请输入学生姓名：')
    for info in stu_list:
        if info['name'] == name:
            new = input('请输入新的学生名字：')
            chinese = input('请输入新的语文成绩：')
            english = input('请输入新的英语成绩：')
            math = input('请输入新的数学成绩：')
            if new:
                info['name'] = new
                info['语文'] = int(chinese)
                info['英语'] = int(english)
                info['数学'] = int(math)
                info['总分'] = int(chinese) + int(english) + int(math)
            else:
                info['name'] = name
                info['语文'] = int(chinese)
                info['英语'] = int(english)
                info['数学'] = int(math)
                info['总分'] = int(chinese) + int(english) + int(math)

def search():
    name = input('请输入要修改的学生姓名：')
    for info in stu_list:
        if info['name'] == name:
            print('姓名\t语文\t英语\t数学\t总分')
            formatter(info['name'], info['语文'], info['英语'], info['数学'], info['总分'])
        # else:
        #     print('此学生信息并不存在，请确认后再输入')

def show_all():
    print('姓名\t语文\t英语\t数学\t总分')
    for info in stu_list:
        formatter(info['name'], info['语文'], info['英语'], info['数学'], info['总分'])

def formatter(name, chinese, english, math, total):
    print(f"{name}\t{chinese}\t{english}\t{math}\t{total}")

def delete():
    name = input('请输入要删除的学生姓名：')
    for info in stu_list:
        if info['name'] == name:
            stu_list.remove(info)

def end():
        print('感谢使用')
        print(stu_list)
        new_list = json.dumps(stu_list, ensure_ascii=False)
        with open('stu_info.json', 'w', encoding='utf-8') as w:
            w.write(new_list)

while True:
    print(welcome)
    choice = input('请输入操作号码：')
    if choice == '1':
        add()
    elif choice == '2':
        modify()
    elif choice == '3':
        search()
    elif choice == '4':
        show_all()
    elif choice == '5':
        delete()
    elif choice == '0':
        end()
        break
    else:
        print('输入不合法，请确认后重新输入')
