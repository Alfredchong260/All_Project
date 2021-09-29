"""
1. 程序启动，显示信息管理系统欢迎界面，并显示功能菜单(print)
2. 用户用数字选择不同的功能 (input  )
3. 根据功能选择，执行不同的功能( 多分支判断 )
4. 需要记录学生的 姓名、语文成绩、数学成绩、英语成绩 、总分 (input 学生信息怎么存储?)
5. 进入或退出时加载或保存数据(文件操作)
"""
import json

str_info = """**************************************************
欢迎使用【学生信息管理系统】V1.0
请选择你想要进行的操作
1. 新建学生信息
2. 显示全部信息
3. 查询学生信息
4. 修改学生信息
5. 删除学生信息

0. 退出系统
**************************************************"""

# 读取文件里面的数据
with open('students.json', mode='r', encoding='utf-8') as f:
    students_str = f.read()

students = json.loads(students_str)

# 循环
while True:  # 死循环<因为选择的功能要执行很多次>
    # 1.程序启动，显示信息管理系统欢迎界面，并显示功能菜单(print)
    print(str_info)
    # 2. 用户用数字选择不同的功能 (input)
    action = input('请输入你要执行的操作:')
    # 3. 根据功能选择，执行不同的功能( 多分支判断 )
    if action == '1':
        print('1. 新建学生信息')
        name = input('请输入学生姓名:')
        chinese = int(input('请输入学生语文成绩:'))
        math = int(input('请输入学生数学成绩:'))
        english = int(input('请输入学生英语成绩:'))
        total = chinese + math + english

        stu = {'name': name, 'chinese': chinese, 'math': math, 'english': english, 'total': total, }
        students.append(stu)  # 列表添加

    elif action == '2':
        print('2. 显示全部信息')
        print('姓名\t\t语文\t数学\t英语\t总分')  # 汉字 和 字母/字符串
        for stu in students:
            print(f'{stu["name"]}\t\t{stu["chinese"]}\t\t{stu["math"]}\t\t{stu["english"]}\t\t{stu["total"]}')

    elif action == '3':
        print('3. 查询学生信息')
        name = input('请输入你想要查找学生的姓名')
        for stu in students:  # 遍历所有学生
            if name == stu['name']:  # 满足这个条件, 代表要查找的学生找到了
                print('姓名\t\t语文\t数学\t英语\t总分')
                print(f'{stu["name"]}\t\t{stu["chinese"]}\t\t{stu["math"]}\t\t{stu["english"]}\t\t{stu["total"]}')
                # 整个系统没有重名的
                # 找到了学生我就不继续找了
                break
        else:
            # 如果没有找到学生, 就会走else的逻辑
            print('该学生不存在, 请检查名字是否输入正确')

    elif action == '4':
        print('4. 修改学生信息')
        name = input('请输入你想要修改学生的姓名:')
        for stu in students:  # 遍历所有学生
            if name == stu['name']:  # 满足这个条件, 代表要查找的学生找到了
                # pass  # 语法占位
                print('回车代表使用原来的数据')
                name = input('请重新输入学生姓名:')
                chinese = input('请重新输入学生语文成绩:')
                math = input('请重新输入学生数学成绩:')
                english = input('请重新输入学生英语成绩:')
                # total = chinese + math + english
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

    elif action == '5':
        print('5. 删除学生信息')
        # 如果要删除学生信息, 那么首先得找到
        name = input('请输入你想要删除学生的姓名:')
        for stu in students:  # 遍历所有学生
            if name == stu['name']:  # 满足这个条件, 代表要删除的学生找到了
                # pop  index
                students.remove(stu)
                break
        else:
            print('该学生不存在, 请检查名字是否输入正确')
    elif action == '0':
        print('0. 退出系统')
        with open('students.json', mode='w', encoding='utf-8') as f:
            # 把对象<列表 字典>转换成字符串  编码 Unicode编码
            # ensure_ascii=False  不使用Unicode编码
            students_str = json.dumps(students, ensure_ascii=False)
            f.write(students_str)
        break
    else:
        print('请输入正确的选择!出现未知情况!')
