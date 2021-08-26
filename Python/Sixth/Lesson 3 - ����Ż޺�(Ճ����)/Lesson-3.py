name=['大雄','小夫','胖虎']
number=[123,456,789]
a=('''====通讯录管理系统====
1.增加姓名和手机
2.删除姓名
3.修改手机
4.查询所有用户
5.根据姓名查找手机号
6.退出
=====================
请选择：''')
while True:
      print(a)
      b=input(a)
      if b not in('1','2','3','4','5','6'):
            input('输入无效，请重新输入:')
      elif b ==('1'):
            name1=str(input('请输入姓名:'))
            if name1 in name:
                  print('已有此联络人，请重新输入:')
                  # continue
            else:
                  name.append(name1)
                  number1=str(input('请输入联络号码:'))
                  number.append(number1)
                  print('输入完成')
      elif b ==('2'):
            name1=str(input('请输入要删除的联系人:'))
            name.remove(name1)
            print('删除完成')
      elif b==('3'):
            name1= str(input('请输入要修改的联系人:'))
            c=name.index(name1)
            d=str(input('要修改的联系人姓名:'))
            e=str(input('要修改的手机号:'))
            name[c]=d
            number[c]= e
            print(('修改完成'))
      elif b==('4'):
            #第一种
            # person=list(zip(name,number))
            # for p in person:
            #       print('所有用户为:',p)
            #第二种
            print('所有用户为:')
            for p in name:
                  index=name.index(p)
                  phone=number[index]
                  print(p,':',phone)
      elif b==('5'):
            name1=str(input('请输入您要查询的联系人:'))
            c=name.index(name1)
            print('您所查找的联系人号码为:',number[c])
      else:
            b==('6')
            print('感谢使用')
            break
