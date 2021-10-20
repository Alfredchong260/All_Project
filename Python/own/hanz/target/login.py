'''
login system
    思路：
        增删改查
'''

# Dictionary not allow duplicate, overwrite
# information = {"Username":"Alfred", 'Password': '123456789'}
# print(information['Username'])
# print(infos[4])

infos = [
    {'Username':'CheHin','Password':'123456'},
    {'Username':'John','Password':'John123'},
    {'Username':'Steven','Password':'Steven123'},
]

welcome = '''Welcome to the First Version of the Login System
    1. Login
    2. Delete
    3. Modify
    4. Search
    5. Exit
'''


flag = 1
while flag:
    print(welcome)
    choice = input('Please enter your choice:')
    if choice == '1':
        username = input('Please enter your username:')
        password = input('Please enter your password:')
        for info in infos:
            if info['Username'] == username:
                if info['Password'] == password:
                    print('Login')
                    flag = 0

                else:
                    print('Password Incorrect')

    elif choice == '2':
        username = input('Please enter your username:')
        password = input('Please enter your password:')
        for info in infos:
            if info['Username'] == username:
                print('Account found')
                double_confirm = input('Are you sure want to delete account ? Y/N :')
                if double_confirm.upper() == 'Y':
                    infos.remove(info)
                elif double_confirm.upper() == 'N':
                    continue
                else:
                    print('Invalid Input')

    elif choice == '3':
        username = input('Please enter your username:')
        password = input('Please enter your password:')
        for info in infos:
            if info['Username'] == username:
                if info['Password'] == password:
                    new_password = input('Please enter your new password:')
                    info['Password'] = new_password
                    print('Password changed')
                else:
                    print('Incorrect password')

    elif choice == '4':
        username = input('Please enter your username:')
        password = input('Please enter your password:')
        for info in infos:
            if info['Username'] == username:
                if info['Password'] == password:
                    print(f'Username:{username}\nPassword:{password}')
                else:
                    print('Incorrect password')

    if choice == '5':
        break
