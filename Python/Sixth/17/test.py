dc = {'name': 'chong', 'age': 18, 'hobby': 'coding'}
# if dc['name'] == 'chong':
#     print('True')
import os
lst = []
db_file = 'Stu_data_base.txt'
if os.path.exists(db_file):
    stu_name = input('please enter name : ')
    with open(db_file, mode='r', encoding='utf-8') as r_file:
        read = r_file.readlines()
        length = len(read)
        with open(db_file, mode='w', encoding='utf-8') as w_file:
            for i in read:
                i = dict(eval(i))
                w_file.write(str(i))
                lst.append(i)
                if i['Name'] == stu_name:

                    print(i.get('Situation'))
                else:
                    print('There is not any data of %s in data base' % stu_name)
#             # stu_name = input('Name of the student who want to check : ')
#             if i['Name'] == 'chong':
#                 print(i.get('Situation'))

# a= 3
# if a == 5:
#     print('False')
# else:
#     print("True")