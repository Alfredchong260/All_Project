
try:  # 是异常捕获的关键字, 有代码块, 代码块中需要把所有可能出现的代码放到代码块下
    # 放到try代码块下面的代码, 只要有一句报错了都不会执行
    # try代码块只要不报错任然能够执行
    score = input('请输入学生成绩:')
    score = int(score)
    result = 10 / score

# Exception  错误的总类
# e  报错的提示用 e 接受了
except Exception as e:  # except 如果try代码块下的代码发生了报错, 就会走except代码逻辑
    # print(e)
    pass

else:
    # try 代码块中没有报错就会走 else 的代码逻辑
    print('没有报错')

