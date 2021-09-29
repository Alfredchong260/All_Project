"""
登录账号, 如果密码没有输入对就一直尝试,直到输入对为止
"""

while True:
    password = input('请输入密码:')

    if password == '123456':
        print('密码输入正确, 跳出循环!')
        break  # 在循环中遇到 break 那么就会结束整个循环

    print('密码输入错误, 请重新输入!')
