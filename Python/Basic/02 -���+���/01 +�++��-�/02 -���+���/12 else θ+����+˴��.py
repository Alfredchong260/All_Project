

for i in range(5):
    print(i)
    if i == 3:
        # 如果循环语句中有break, 那么代表这个循环没有正常结束, 就不会走else的逻辑
        # 如果循环语句中有continue, 那么代表这个循环是正常结束, 会走else的逻辑
        continue  # 终止整个循环

else:
    # 只有循环正常结束, 搭配了else语句的话, 才会执行else逻辑
    print('for循环正常执行完毕')

"""for/while  ...  else """
