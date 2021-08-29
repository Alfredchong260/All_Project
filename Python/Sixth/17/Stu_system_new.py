# 数据库文档
import os

db_file = 'Stu_data_base.txt'


def menu():
    print('========== Student Management System ==========')
    print('==========       Option Menu         ==========')
    print('           1: Insert Student Info          ')
    print('           2: Search Student\'s Info')
    print('           3: Delete Student\'s Info')
    print('           4: Modify Student\'s Info')
    print('           5: Sort Student\'s Info')
    print('           6: Show All Students\' Info')
    print('           7: Check student\'s situation')
    print('           0: Exit System')
    print('===============================================')


# 添加函数
def add():
    # 声明列表保存原有的数据
    lst = []
    global c_result, python_result, html_result  # 将变量引用成全局变量
    while True:
        stu_id = input('Please enter Student\'s id : ')
        if stu_id == '':
            break
        stu_name = input('Please enter Student\'s name : ')
        if stu_name == '':
            break
        stu_sit = input('Please enter student\'s situation(suspend or normal) : ')
        if stu_sit == '':
            break
        elif stu_sit == 'suspend':
            pass
        elif stu_sit == 'normal':
            pass
        else:
            print('Please check the option and re-enter')
            continue

        # 以防用户输入错误信息
        try:
            c_result = input('Please enter result of C language : ')
            python_result = input('Please enter result of Python : ')
            html_result = input('Please enter result of HTML : ')
        except Exception:
            print("Please enter number for student\'s result")
            continue

        # 收集学生信息，将数据保存至字典数据
        Stu_dict = {'ID': stu_id, 'Name': stu_name, 'Situation': stu_sit,
                    'C language': c_result, 'Python': python_result, 'HTML': html_result}

        # 将以添加好的自带你保存到列表当中
        lst.append(Stu_dict)

        # 询问是否继续操作
        check = input('Do you want to add other info (y/n) : ')
        if check == 'y' or check == 'Y':
            add()
        elif check == 'n' or check == 'N':
            print('Info successfully insert')
            break
        elif check == '':
            print('You cannot insert nothing,we will forcibly exit current system')
            break
        else:
            print('The choice you choose is not in the option,we will '
                  'forcibly exit current system')
            break
        print(Stu_dict)
        break
    save(lst)


# 定义save函数，保存至txt文档中
def save(lst_data):
    try:
        # a表示追加数据，但是不能创建文件，利用w 创建文件 为a 追加
        stu_txt = open(db_file, mode='a+', encoding='utf-8')
    except:
        stu_txt = open(db_file, mode='w+', encoding='utf-8')
    for i in lst_data:
        stu_txt.write(str(i) + '\n')
    stu_txt.close()


# 查询函数
def select():
    '''
    根据学生id或姓名进行持续查询
    '''
    ''' 将id和name设置成全局变量，如果不讲变量声明成去那句变量的话，
        他就是局部变量，那么很有可能别的变量访问不到'''
    _id = ''
    _name = ''
    search_info = []
    while True:
        # alt + enter --> 自动导包
        # 判断文档是否存在的功能
        if os.path.exists(db_file):
            check = int(input('Please choose a matter for checking '
                              '1.Use id to check    2.Use name to check : '))
            if check == 1:
                _id = input('Please enter student\'s id : ')
            elif check == 2:
                _name = input('Please enter student\'s name : ')
            else:
                print('The value you insert is not in option,we will forcibly '
                      'exit current system')
                select()

            # 获取数据
            with open(db_file, mode='r', encoding='utf-8') as r_file:
                stu_lst = r_file.readlines()
                # 将用户和db.txt里面的数据进行匹配，先强转成dict类型
                for i in stu_lst:  # i -->
                    i = dict(eval(i))
                    if _id:
                        if i['ID'] == _id:
                            search_info.append(i)
                    elif _name:
                        if i['Name'] == _name:
                            search_info.append(i)
                    else:
                        print('There is no any data for the info you input')

            # 当后端匹配到了用户输入的信息一致时，我们将数据展现出来
            all(search_info)
            # 为了数据的匹配性，将原数据进行清空
            search_info.clear()
        else:
            print('Please enter student\'s data')
            add()

        check = input('Do you want to check another student\'s info?  (y/n) : ')
        if check == 'y' or check == 'Y':
            select()
        elif check == 'n' or check == 'N':
            print('Query is complete, exit the current system now')
            break


# 删除函数
def delete():
    '''根据学生的资料进行删除，好好的利用读写功能'''
    flag = 0
    while True:
        stu_id = input('Pleas enter student\'s id for delete action : ')
        if stu_id:
            # 读数据
            with open(db_file, mode='r', encoding='utf-8') as r_file:
                stu = r_file.readlines()
            if stu:
                with open(db_file, mode='w', encoding='utf-8') as w_file:
                    # 利用写的过程将用户选择的数据删掉
                    for i in stu:
                        i = dict(eval(i))
                        if i['ID'] == stu_id:
                            flag += 1
                            # 此时表示用户输入的id 和 数据资源中的id一致的，不用管它
                        elif i['ID'] != stu_id:
                            # 这些数据不需要删除，所有把它们重新写入
                            w_file.write(str(i) + '\n')

            if flag == 1:
                print('Info of student\'s ID %s deleted' % stu_id)
            else:
                print('There is no info of student who id is %s' % stu_id)
        else:
            print('The value you insert is not in option,we will forcibly '
                  'exit current system')
            break
        choose = input('Do you want to delete other student\'s info?  (y/n) : ')
        if choose == 'y' or choose == 'Y':
            delete()
        elif choose == 'n' or choose == 'N':
            break
        else:
            print('The value you insert is not in option,please check and re-enter')
            continue


# 此函数用于将数据进行格式化展示
def all(lst):
    # 显示找到的结果
    # print(type(lst))
    if len(lst) == 0:
        print('当前这个文档中没有数据！！')
    # 定义好了输出的格式
    format_title = '{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t'
    print(format_title.format('ID', 'Name', 'C language', 'Python', 'HTML'
                              , 'Average mark'))
    # 定义内容格式
    format_data = '{:^7.8}\t{:^7}\t{:^8}\t{:^6}\t{:^6}\t{:^9}\t'
    for item in lst:
        # print(type(lst))
        print(format_data.format(
            item.get('ID'),
            item.get('Name'),
            item.get('C language'),
            item.get('Python'),
            item.get('HTML'),
            # 平均总成绩
            (int(item.get('C language')) + int(item.get('Python')) +
             int(item.get('HTML'))) / 3
        ))


# 更新函数
def update():
    if os.path.exists(db_file):
        stu_id = input('Please enter student\'s id who you want to change data - - >')
        if stu_id != '':
            with open(db_file, mode='r', encoding='utf-8') as r_file:
                lst_data = r_file.readlines()
                # 利用读和写的功能来修改文档中的数据
                if lst_data:
                    with open(db_file, mode='w', encoding='utf-8') as w_file:
                        for i in lst_data:
                            i = dict(eval(i))
                            # 用户输入的id 和 字典中原有id的value一致，就进行修改操作
                            if i['ID'] == stu_id:
                                print('Please do the changes for %s' % i['Name'])
                                while True:
                                    try:
                                        choice = int(input(
                                            'What information you want to update ? ''\n''1.ID     2.Name     3.C language result   4.Python result    5.HTML result     6.Student\'s situation- - > '))
                                        if choice in [1, 2, 3, 4, 5, 6]:
                                            if choice == 1:
                                                if i['ID'] == stu_id:
                                                    new_id = input('The new id : ')
                                                    i['ID'] = new_id
                                            if choice == 2:
                                                if i['ID'] == stu_id:
                                                    new_name = input('The new name : ')
                                                    i['Name'] = new_name
                                                else:
                                                    print('The id you input is don\'t have any record')
                                            if choice == 3:
                                                if i['ID'] == stu_id:
                                                    new_c = input('The new C language result : ')
                                                    i['C language'] = new_c
                                                else:
                                                    print('The id you input is don\'t have any record')
                                            if choice == 4:
                                                if i['ID'] == stu_id:
                                                    new_python = input('The new python result : ')
                                                    i['Python'] = new_python
                                                else:
                                                    print('The id you input is don\'t have any record')
                                            if choice == 5:
                                                if i['ID'] == stu_id:
                                                    new_html = input('The new HTML result : ')
                                                    i['HTML'] = new_html
                                                else:
                                                    print('The id you input is don\'t have any record')
                                            if choice == 6:
                                                if i['ID'] == stu_id:
                                                    new_sit = input('The new situation(suspend or normal) : ')
                                                    if new_sit == 'suspend':
                                                        pass
                                                    elif new_sit == 'normal':
                                                        pass
                                                    else:
                                                        print('Please check the option and re-enter')
                                                        break

                                                    i['Situation'] = new_sit
                                            else:
                                                print('The id you input is don\'t have any record')
                                        else:
                                            print('Please check the option adn re-enter')
                                    except Exception:
                                        print('Please check the option and re-enter')
                                    else:
                                        break
                                w_file.write(str(i) + '\n')

                            else:
                                w_file.write(str(i) + '\n')
                    # 是否要继续修改
                    check = input('Do you want to change anything else?  (y/n)')
                    if check == 'y' or check == 'Y':
                        update()
                    elif check == 'n' or check == 'N':
                        print('Exit current system')
                else:
                    print('The current folder don\'t have any data')
        else:
            print('You cannot enter nothing')
    else:
        print('The is no any folder')


# 排列函数
def sort():
    flag = True
    new_lst = []
    # 检查文件是否存在
    if os.path.exists(db_file):
        # 读数据
        with open(db_file, mode='r', encoding='utf-8') as r_file:
            read = r_file.readlines()
            for i in read:
                i = dict(eval(i))
                new_lst.append(i)
            # 显示整个数据
            all(new_lst)
        check = int(input('According : 1, Descending : 2 - - > '))
        if check == 1:
            flag = False

        elif check == 2:
            flag = True

        choice = int(input('Please choose an option - C language : 1, Python : 2'
                           ', HTML : 3, Average mark : 4 - - > '))
        if choice == 1:
            # 根据用户的选择进行排序
            new_lst.sort(key=lambda x: int(x['C language']), reverse=flag)
        elif choice == 2:
            new_lst.sort(key=lambda x: int(x['Python']), reverse=flag)
        elif choice == 3:
            new_lst.sort(key=lambda x: int(x['HTML']), reverse=flag)
        elif choice == 4:
            new_lst.sort(key=lambda x: (int(x['C language']) + int(x['Python'])
                                        + int(x['HTML'])) / 3, reverse=flag)
        else:
            print('Please check and re-enter the option')
            sort()
        all(new_lst)
    else:
        print('There in no any file')


# 显示所有的函数
def show_all():
    lst = []
    if os.path.exists(db_file):
        with open(db_file, mode='r', encoding='utf-8') as r_file:
            l = r_file.readlines()
            print('Total there are %d data' % len(l))
            for i in l:
                i = dict(eval(i))
                lst.append(i)
            all(lst)


# 显示学生状况
def show_info(lst):
    if len(lst) == 0:
        print('There is no any data in folder')
    format_title = '{:^6}'
    format_data = '{:^18}'
    print(format_title.format('Student\'s Situation'))
    for item in lst:
        print(format_data.format(
            item.get('Situation')
        ))


# 分辨学生是否停学的函数
def suspension():
    stu_id = ''
    stu_name = ''
    search_info = []
    while True:
        if os.path.exists(db_file):
            choice = int(input('What matter you want to use for checking'
                               '    1.ID    2.Name - ->'))
            if choice == 1:
                stu_id = input('Please input student\'s ID : ')
            elif choice == 2:
                stu_name = input('Name of the student who want to check : ')

            with open(db_file, mode='r', encoding='utf-8') as r_file:
                read = r_file.readlines()
                for i in read:
                    i = dict(eval(i))
                    if stu_id:
                        if i['ID'] == stu_id:
                            search_info.append(i)
                    elif stu_name:
                        if i['Name'] == stu_name:
                            search_info.append(i)
                    else:
                        print('There is no any data for the info you input')
            show_info(search_info)
            search_info.clear()
        check = input('Do you want to check another student\'s situation  (y/n) : ')
        if check == 'y' or check == 'Y':
            suspension()
        elif check == 'n' or check == 'N':
            print('Exit the current system now')


# 编写主函数
def main():
    # 显示菜单，判断用户输入的序号是否ok，执行及调用函数
    while True:
        menu()
        ins = int(input('Please enter a number to activate system : '))
        if ins in [0, 1, 2, 3, 4, 5, 6, 7]:
            if ins == 0:
                check = input('Are you sure to Exit System? (y/n) : ')
                if check == 'y' or check == 'Y':
                    print('Welcome to use this system again')
                    break
                else:
                    main()
            elif ins == 1:
                add()
            elif ins == 2:
                select()
            elif ins == 3:
                delete()
            elif ins == 4:
                update()
            elif ins == 5:
                sort()
            elif ins == 6:
                show_all()
            elif ins == 7:
                suspension()
        else:
            print("The number you insert is not in the option")


if __name__ == '__main__':
    main()
