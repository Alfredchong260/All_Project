'''         列表的筛选操作         '''
lst=['cola','sprite','100plus','sprite','kikaboo','fanta','cola']
drinks=[]
for i in lst:
    if i not in drinks:
        drinks.append(i)
print(drinks)

'''         屏蔽敏感词汇          '''
sensitive_word=['憨','笨','蛋','逼']
while True:
    a=input('请输入语句:')
    for i in sensitive_word:
        if i in a:
            print('*'.join(a.split(i)))
