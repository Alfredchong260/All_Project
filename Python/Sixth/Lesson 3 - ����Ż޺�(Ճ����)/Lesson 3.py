drink_jiangxiaobai=['江小白','20','0123','2023']
drink_erguotou=['二锅头','50','3210','2025']
'''         列表添加操作        '''
drink_jiangxiaobai.append('0123456789')
print(drink_jiangxiaobai)

drink_erguotou.insert(1,'十年纯酿')
print(drink_erguotou)

drink_jiangxiaobai.extend(drink_erguotou)
print(drink_jiangxiaobai)
'''         列表删除操作          '''
drink_jiangxiaobai.pop(1)
print(drink_jiangxiaobai)

drink_erguotou.remove('3210')
print(drink_erguotou)

drink_jiangxiaobai.clear()
print(drink_jiangxiaobai)

drink_xuebi=['雪碧','3','9876','2021']
drink_cola=['可乐','4','6789','2022']
'''         列表查找操作          '''
drinks_name= drink_xuebi[0]
print(drinks_name)

#查找索引
print(drink_cola.index('2022'))

'''         索引的切片操作         '''
#取 可乐以及4
print(drink_cola[:2])

#取 6789以及2022
print(drink_xuebi[2:])

'''         顺序的反向查询操作            '''
print(drink_cola[::-1])

'''         二维，三维，四维查询          '''
lst=['蜡笔小新',250,[1,3,5,7,9],{'蜡笔小新':'二货','age':'163','生日':'6/7'}]
#取 250
print(lst[1])
#取 5
print(lst[2][2])
#取 163
print(lst[3]['age'])