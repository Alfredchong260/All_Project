"""
    全局思路：
        一套系统
        能够让用户选择
        能够完成增，删，改，查的操作
"""

welcome = '''学生管理系统 Version 1.0
1.增加学生资料
2.查询学生信息
3.显示所有学生资料
4.删除指定学生信息
5.修改学生信息
6.退出本系统
\n'''

stu_info = [{'name':'Phang You Wei', 'age':18, 'Hobby':'Sleep'}, {'name':'Chen Han Zheng', 'age':0, "Hobby":"Eat"}]
for i in stu_info:
    print(i['name'])

x = ['1','2','3','4','5','6']

# while True:
#     print(welcome)
#     choice = input('请输入指定号码：')
#     if choice in x:
#         if choice == '1':
#             pass
#         elif choice == '2':
#             pass
#         elif choice == '3':
#             pass
#         elif choice == '4':
#             pass
#         elif choice == '5':
#             pass
#         elif choice == '6':
#             pass
#     else:
#         print('error')
